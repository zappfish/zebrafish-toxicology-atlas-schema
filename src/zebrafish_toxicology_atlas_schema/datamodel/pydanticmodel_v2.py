from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'zebrafish_toxicology_atlas_schema',
     'default_range': 'string',
     'description': 'Schema to represent metadatcha associated with the Zebrafish '
                    'Toxicology Atlas',
     'id': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'zebrafish-toxicology-atlas-schema',
     'prefixes': {'CAS': {'prefix_prefix': 'CAS',
                          'prefix_reference': 'https://commonchemistry.cas.org/detail?cas_rn='},
                  'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'ECTO': {'prefix_prefix': 'ECTO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ECTO_'},
                  'EXO': {'prefix_prefix': 'EXO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/EXO_'},
                  'ORCID': {'prefix_prefix': 'ORCID',
                            'prefix_reference': 'https://orcid.org/'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'ZFIN': {'prefix_prefix': 'ZFIN',
                           'prefix_reference': 'https://zfin.org/'},
                  'ZP': {'prefix_prefix': 'ZP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/ZP_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'zebrafish_toxicology_atlas_schema': {'prefix_prefix': 'zebrafish_toxicology_atlas_schema',
                                                        'prefix_reference': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema/'}},
     'see_also': ['https://sierra-moxon.github.io/zebrafish-toxicology-atlas-schema'],
     'source_file': 'src/zebrafish_toxicology_atlas_schema/schema/zebrafish_toxicology_atlas_schema.yaml',
     'title': 'zebrafish-toxicology-atlas-schema'} )

class SeverityEnum(str, Enum):
    """
    An enumeration of severity levels for phenotypes.
    """
    mild = "mild"
    """
    Mild severity
    """
    moderate = "moderate"
    """
    Moderate severity
    """
    severe = "severe"
    """
    Severe severity
    """


class ExposureTypeEnum(str):
    """
    An enumeration of exposure types derived from the ECTO ontology.
    """
    pass


class ExposureRouteEnum(str):
    """
    An enumeration of exposure routes derived from the EXO ontology.
    """
    pass


class ExposureRegimenTypeEnum(str, Enum):
    """
    An enumeration of exposure regimen types.
    """
    continuous = "continuous"
    """
    Continuous exposure
    """
    repeated = "repeated"
    """
    Repeated exposure
    """


class VehicleEnumeration(str, Enum):
    """
    An enumeration of vehicles used in exposures.
    """
    ethanol = "ethanol"
    """
    Ethanol
    """
    dmso = "dmso"
    """
    DMSO
    """



class ZappEntity(ConfiguredBaseModel):
    """
    Internal entities with auto-generated integer IDs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class OntologyEntity(ConfiguredBaseModel):
    """
    Entities representing ontology terms with URI identifiers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    pass


class ZfinEntity(ConfiguredBaseModel):
    """
    Entities with ZFIN database identifiers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    zfin_id: str = Field(default=..., description="""ZFIN database identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZfinEntity']} })

    @field_validator('zfin_id')
    def pattern_zfin_id(cls, v):
        pattern=re.compile(r"^ZFIN:ZDB-[A-Z]+-\d{6}-\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid zfin_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid zfin_id format: {v}"
            raise ValueError(err_msg)
        return v


class Study(ZappEntity):
    """
    A toxicological investigation, including the experimental conditions and phenotypic outcomes, with information provenance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    experiment: Optional[list[Experiment]] = Field(default=None, description="""The experiments in a study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publication: Optional[str] = Field(default=None, description="""The publication identifier (e.g., PMID, DOI) for the study or \"not published\" if the study is unpublished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    annotator: Optional[list[str]] = Field(default=None, description="""ORCID identifier of the indidvidual submitting the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    lab: Optional[str] = Field(default=None, description="""The lab where the experiment originated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })

    @field_validator('annotator')
    def pattern_annotator(cls, v):
        pattern=re.compile(r"^ORCID:[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid annotator format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid annotator format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('lab')
    def pattern_lab(cls, v):
        pattern=re.compile(r"^ZFIN:ZDB-LAB-[0-9]+-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid lab format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid lab format: {v}"
            raise ValueError(err_msg)
        return v


class Experiment(ZappEntity):
    """
    Group of observations (phenotypic outcomes and their control) that are linked by a common experiment and subject that are part of a study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    standard_rearing_condition: Optional[bool] = Field(default=None, description="""An indication if the subject was maintained under standard conditions, which are the established, consistent environmental and husbandry parameters (such as temperature, lighting, diet, and housing) designed to minimize variability and ensure reproducibility in experiments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    rearing_condition_comment: Optional[str] = Field(default=None, description="""Comments on rearing conditions, for example, about how conditions deviated from standard parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    fish: Optional[Fish] = Field(default=None, description="""The fish subject of the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    control: Optional[list[Control]] = Field(default=None, description="""The controls for this experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    exposure_event: Optional[list[ExposureEvent]] = Field(default=None, description="""The exposure events in this experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class PhenotypeObservationSet(ZappEntity):
    """
    A phenotypic outcome resulting from an exposure event.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    image: Optional[list[Image]] = Field(default=None, description="""Images associated with this observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    phenotype: Optional[list[Phenotype]] = Field(default=None, description="""The phenotype observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    control_image: Optional[list[ControlImage]] = Field(default=None, description="""Images associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class Phenotype(ZappEntity):
    """
    Any measurable or visible trait change in the subject as a result of exposure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when the phenotype was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    prevalence: Optional[QuantityValue] = Field(default=None, description="""The percentage of subject exhibiting this phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[SeverityEnum] = Field(default=None, description="""The intensity of the observed phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    phenotype_term_id: Optional[PhenotypeTerm] = Field(default=None, description="""The phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class Control(ZappEntity):
    """
    Information about controls used in the experiment, including the type of control (wildtype vs mutant, treated vs untreated) and vehicle information if applicable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    control_type: Optional[str] = Field(default=None, description="""Type of control (e.g., wildtype vs mutant, treated vs untreated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    vehicle_if_treated: Optional[VehicleEnumeration] = Field(default=None, description="""Vehicle used if this is a treated control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control', 'ExposureEvent', 'StressorChemical']} })
    control_image: Optional[list[ControlImage]] = Field(default=None, description="""Images associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ExposureEvent(ZappEntity):
    """
    An occurrence in a study where a subject is exposed to a stressor under defined conditions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['biolink:ExposureEvent'],
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    stressor: Optional[list[StressorChemical]] = Field(default=None, description="""Substance, chemical or toxicant, that elicit a response (a phenotype) in a subject when encountered through exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    vehicle: Optional[list[VehicleEnumeration]] = Field(default=None, description="""The substance or medium used deliver a stressor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    route: Optional[ExposureRouteEnum] = Field(default=None, description="""The route of exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    regimen: Optional[Regimen] = Field(default=None, description="""The regimen for the exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_start_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_end_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control', 'ExposureEvent', 'StressorChemical']} })
    exposure_type: Optional[ExposureTypeEnum] = Field(default=None, description="""An instance of exposure specifying the type of stressor a subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    additional_exposure_condition: Optional[str] = Field(default=None, description="""Additional information about the conditions under which exposure event occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    phenotype_observation: Optional[list[PhenotypeObservationSet]] = Field(default=None, description="""The phenotype observations from this exposure event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class Regimen(ZappEntity):
    """
    The schedule and pattern of an exposure event.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    exposure_regimen_type: Optional[ExposureRegimenTypeEnum] = Field(default=None, description="""The type of exposure regimen (e.g., continuous or repeated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    interval_between_individual_exposures: Optional[QuantityValue] = Field(default=None, description="""Interval between individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    total_exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Time between first and last individual exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    individual_exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Individual exposure duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    number_of_individual_exposure: Optional[int] = Field(default=None, description="""Total number of individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class StressorChemical(ZappEntity):
    """
    A chemical, that elicit a response (a phenotype) in a subject when when encountered through exposure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    chemical_id: ChemicalEntity = Field(default=..., description="""Chemical identifier (CHEBI, CAS, or UUID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    manufacturer: Optional[str] = Field(default=None, description="""The manufacturer of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    concentration: QuantityValue = Field(default=..., description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control', 'ExposureEvent', 'StressorChemical']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class Image(ZappEntity):
    """
    An image associated with a phenotype observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""Level of detail of the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ControlImage(ZappEntity):
    """
    An image associated with a control, taken at the same developmental stage as the corresponding phenotype observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    phenotype_id: Optional[str] = Field(default=None, description="""Foreign key reference to the PhenotypeObservationSet uuid (for database representation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""Level of detail of the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    phenotype_comments: Optional[str] = Field(default=None, description="""Comments about the phenotype in the control image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ChemicalEntity(OntologyEntity):
    """
    The chemical used as the stressor chemical in an exposure event.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['biolink:ChemicalEntity'],
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    uri: str = Field(default=..., description="""URI identifier for the chemical entity (CHEBI or CAS URI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    chebi_id: Optional[str] = Field(default=None, description="""CHEBI identifier for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    cas_id: Optional[str] = Field(default=None, description="""CAS identifier for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    chemical_name: Optional[str] = Field(default=None, description="""Name of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    synonym: Optional[list[str]] = Field(default=None, description="""Other names for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })


class PhenotypeTerm(OntologyEntity):
    """
    A phenotype ontology term from the Zebrafish Phenotype ontology (ZP).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['biolink:PhenotypicFeature'],
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    term_uri: str = Field(default=..., description="""The URI of the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm']} })
    term_label: Optional[str] = Field(default=None, description="""The human-readable label for the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm']} })


class Fish(ZfinEntity):
    """
    Zebrafish used as subject in the study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    name: str = Field(default=..., description="""Name or label of an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Fish']} })
    zfin_id: str = Field(default=..., description="""ZFIN database identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZfinEntity']} })

    @field_validator('zfin_id')
    def pattern_zfin_id(cls, v):
        pattern=re.compile(r"^ZFIN:ZDB-[A-Z]+-\d{6}-\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid zfin_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid zfin_id format: {v}"
            raise ValueError(err_msg)
        return v


class QuantityValue(ConfiguredBaseModel):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    unit: Optional[str] = Field(default=None, description="""The unit of the quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    numeric_value: Optional[str] = Field(default=None, description="""The numeric value of the quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ZappEntity.model_rebuild()
OntologyEntity.model_rebuild()
ZfinEntity.model_rebuild()
Study.model_rebuild()
Experiment.model_rebuild()
PhenotypeObservationSet.model_rebuild()
Phenotype.model_rebuild()
Control.model_rebuild()
ExposureEvent.model_rebuild()
Regimen.model_rebuild()
StressorChemical.model_rebuild()
Image.model_rebuild()
ControlImage.model_rebuild()
ChemicalEntity.model_rebuild()
PhenotypeTerm.model_rebuild()
Fish.model_rebuild()
QuantityValue.model_rebuild()
