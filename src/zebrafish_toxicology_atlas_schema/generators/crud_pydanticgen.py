"""CRUD Pydantic model generator for zebrafish-toxicology-atlas-schema.

Extends LinkML's PydanticGenerator to produce Create and Update model variants
for ZappEntity subclasses. Create variants omit the server-generated ``id`` field
and swap nested entity references to their Create variants. Update variants make
all fields Optional for partial PATCH updates.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import click
from linkml.generators.pydanticgen.pydanticgen import PydanticGenerator
from linkml.generators.pydanticgen.template import (
    PydanticAttribute,
    PydanticClass,
    PydanticModule,
)
from linkml_runtime.utils.schemaview import SchemaView


def _get_zapp_entity_classes(template: PydanticModule, sv: SchemaView) -> set[str]:
    """Return class names that are concrete ZappEntity subclasses."""
    result: set[str] = set()
    for class_name in template.classes:
        cls_def = sv.get_class(class_name, strict=False)
        if cls_def is None or cls_def.abstract:
            continue
        if "ZappEntity" in sv.class_ancestors(class_name):
            result.add(class_name)
    return result


def _get_id_attr_name(class_name: str, sv: SchemaView) -> str:
    """Get the identifier attribute name for a class."""
    id_slot = sv.get_identifier_slot(class_name)
    if id_slot is None:
        return "id"
    return id_slot.name


def _make_create_variant(
    cls: PydanticClass,
    id_attr_name: str,
) -> PydanticClass:
    """Build a Create variant: no id, inherits from ConfiguredBaseModel."""
    new_attrs: dict[str, PydanticAttribute] = {}
    if cls.attributes:
        for attr_name, attr in cls.attributes.items():
            if attr_name == id_attr_name:
                continue
            new_attrs[attr_name] = attr.model_copy()

    return PydanticClass(
        name=f"{cls.name}Create",
        bases="ConfiguredBaseModel",
        description=f"Create schema for {cls.name} — id is server-generated.",
        attributes=new_attrs or None,
    )


def _make_update_variant(
    cls: PydanticClass,
    id_attr_name: str,
) -> PydanticClass:
    """Build an Update variant: no id, all fields Optional."""
    new_attrs: dict[str, PydanticAttribute] = {}
    if cls.attributes:
        for attr_name, attr in cls.attributes.items():
            if attr_name == id_attr_name:
                continue
            updates: dict[str, object] = {}
            if attr.required or attr.identifier or attr.key:
                updates["required"] = False
                updates["identifier"] = False
                updates["key"] = False
                if attr.range and not attr.range.startswith("Optional["):
                    updates["range"] = f"Optional[{attr.range}]"
            new_attrs[attr_name] = attr.model_copy(update=updates) if updates else attr.model_copy()

    return PydanticClass(
        name=f"{cls.name}Update",
        bases="ConfiguredBaseModel",
        description=f"Update schema for {cls.name} — all fields optional for partial updates.",
        attributes=new_attrs or None,
    )


def _swap_nested_references(
    attrs: dict[str, PydanticAttribute],
    create_class_names: set[str],
) -> dict[str, PydanticAttribute]:
    """Replace type references in range strings to point to Create variants."""
    new_attrs: dict[str, PydanticAttribute] = {}
    # Sort by length descending to avoid partial matches (e.g., ControlImage before Control)
    sorted_names = sorted(create_class_names, key=len, reverse=True)

    for attr_name, attr in attrs.items():
        if attr.range:
            new_range = attr.range
            for cls_name in sorted_names:
                new_range = re.sub(
                    r"\b" + re.escape(cls_name) + r"\b",
                    cls_name + "Create",
                    new_range,
                )
            if new_range != attr.range:
                new_attrs[attr_name] = attr.model_copy(update={"range": new_range})
            else:
                new_attrs[attr_name] = attr
        else:
            new_attrs[attr_name] = attr
    return new_attrs


@dataclass
class CrudPydanticGenerator(PydanticGenerator):
    """PydanticGenerator subclass that adds Create/Update model variants."""

    def before_render_template(
        self, template: PydanticModule, sv: SchemaView
    ) -> PydanticModule:
        zapp_classes = _get_zapp_entity_classes(template, sv)
        if not zapp_classes:
            return template

        new_classes: dict[str, PydanticClass] = {}
        create_variants: dict[str, PydanticClass] = {}

        for class_name, cls in template.classes.items():
            new_classes[class_name] = cls
            if class_name in zapp_classes:
                id_attr_name = _get_id_attr_name(class_name, sv)

                create_cls = _make_create_variant(cls, id_attr_name)
                update_cls = _make_update_variant(cls, id_attr_name)

                new_classes[create_cls.name] = create_cls
                new_classes[update_cls.name] = update_cls
                create_variants[create_cls.name] = create_cls

        # Swap nested references in Create variants
        for name, create_cls in create_variants.items():
            if create_cls.attributes:
                create_cls.attributes = _swap_nested_references(
                    create_cls.attributes, zapp_classes
                )

        template.classes = new_classes
        return template


@click.command()
@click.argument("yamlfile")
def cli(yamlfile: str) -> None:
    """Generate Pydantic models with CRUD variants."""
    gen = CrudPydanticGenerator(schema=yamlfile)
    print(gen.serialize())


if __name__ == "__main__":
    cli()
