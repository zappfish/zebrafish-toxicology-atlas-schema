# LinkML-specific recipes

# Generate infores catalog
infores:
    uv run gen-python {{source_schema_path}} > {{pymodel}}/{{schema_name}}.py

# Generate all project files
gen-project:
    uv run gen-project \
        --exclude excel \
        --include graphql \
        --include jsonld \
        --exclude markdown \
        --include prefixmap \
        --include proto \
        --include shacl \
        --include shex \
        --include sqlddl \
        --include jsonldcontext \
        --include jsonschema \
        --exclude owl \
        --include python \
        --include rdf \
        -d {{dest}} {{source_schema_path}}
    uv run python -m zebrafish_toxicology_atlas_schema.generators.crud_pydanticgen {{source_schema_path}} > {{pymodel}}/pydanticmodel_v2.py
    uv run gen-owl --mergeimports --no-metaclasses --no-type-objects --add-root-classes --mixins-as-expressions {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl
    uv run gen-sqla --declarative --sqla-style 2 {{source_schema_path}} > {{pymodel}}/sqla.py

# Generate Pydantic models with CRUD variants
gen-crud-pydantic:
    uv run python -m zebrafish_toxicology_atlas_schema.generators.crud_pydanticgen \
        {{source_schema_path}} > {{pymodel}}/pydanticmodel_v2.py