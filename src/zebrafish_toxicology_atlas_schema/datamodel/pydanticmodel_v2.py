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



class ReadBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
        use_enum_values=True,
    )
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
                  'PUBCHEM.COMPOUND': {'prefix_prefix': 'PUBCHEM.COMPOUND',
                                       'prefix_reference': 'https://identifiers.org/pubchem.compound/'},
                  'UMLS': {'prefix_prefix': 'UMLS',
                           'prefix_reference': 'https://uts.nlm.nih.gov/uts/umls/concept/'},
                  'UNII': {'prefix_prefix': 'UNII',
                           'prefix_reference': 'https://fdasis.nlm.nih.gov/srs/unii/'},
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


class VehicleEnum(str, Enum):
    """
    An enumeration of vehicles used to deliver stressors in exposure events.
    """
    acetone = "acetone"
    """
    Acetone
    """
    acetonitrile = "acetonitrile"
    """
    Acetonitrile
    """
    albumin_bsa = "albumin_bsa"
    """
    Albumin (BSA)
    """
    butanone_mek = "butanone_mek"
    """
    Butanone (MEK)
    """
    cyclodextrin_hpbcd = "cyclodextrin_hpbcd"
    """
    Cyclodextrin (HPBCD)
    """
    dimethyl_formamide = "dimethyl_formamide"
    """
    Dimethyl formamide (DMF)
    """
    dmso = "dmso"
    """
    Dimethyl sulfoxide (DMSO)
    """
    embryonic_media = "embryonic_media"
    """
    Embryonic Media (EM/E3)
    """
    ethanol = "ethanol"
    """
    Ethanol
    """
    glycerol = "glycerol"
    """
    Glycerol
    """
    isopropanol = "isopropanol"
    """
    Isopropanol
    """
    methanol = "methanol"
    """
    Methanol
    """
    methylcellulose = "methylcellulose"
    """
    Methylcellulose
    """
    pbs = "pbs"
    """
    Phosphate-buffered saline (PBS)
    """
    polyethylene_glycol = "polyethylene_glycol"
    """
    Polyethylene glycol
    """
    propylene_glycol = "propylene_glycol"
    """
    Propylene glycol
    """
    solketal = "solketal"
    """
    Solketal
    """
    water = "water"
    """
    Water
    """


class ManufacturerEnum(str, Enum):
    """
    An enumeration of manufacturers and suppliers of chemicals used in exposure events.
    """
    sigma_aldrich = "sigma_aldrich"
    """
    Sigma-Aldrich
    """
    merck_kgaa = "merck_kgaa"
    """
    Merck KGaA
    """
    millipore_sigma = "millipore_sigma"
    """
    MilliporeSigma
    """
    thermo_fisher_scientific = "thermo_fisher_scientific"
    """
    Thermo Fisher Scientific
    """
    fisher_scientific = "fisher_scientific"
    """
    Fisher Scientific
    """
    avantor = "avantor"
    """
    Avantor
    """
    vwr = "vwr"
    """
    VWR
    """
    new_england_biolabs = "new_england_biolabs"
    """
    New England Biolabs
    """
    bio_rad_laboratories = "bio_rad_laboratories"
    """
    Bio-Rad Laboratories
    """
    promega_corporation = "promega_corporation"
    """
    Promega Corporation
    """
    corning_life_sciences = "corning_life_sciences"
    """
    Corning Life Sciences
    """
    lonza_group = "lonza_group"
    """
    Lonza Group
    """
    tocris_bioscience = "tocris_bioscience"
    """
    Tocris Bioscience
    """
    cayman_chemical_company = "cayman_chemical_company"
    """
    Cayman Chemical Company
    """
    selleck_chemicals = "selleck_chemicals"
    """
    Selleck Chemicals
    """
    medchemexpress = "medchemexpress"
    """
    MedChemExpress
    """
    enzo_life_sciences = "enzo_life_sciences"
    """
    Enzo Life Sciences
    """
    aquaneering_inc = "aquaneering_inc"
    """
    Aquaneering Inc.
    """
    pentair_aquatic_eco_systems = "pentair_aquatic_eco_systems"
    """
    Pentair Aquatic Eco-Systems
    """
    tecniplast = "tecniplast"
    """
    Tecniplast
    """
    zebrafish_international_resource_center = "zebrafish_international_resource_center"
    """
    Zebrafish International Resource Center
    """
    tokyo_chemical_industry = "tokyo_chemical_industry"
    """
    Tokyo Chemical Industry
    """
    alfa_aesar = "alfa_aesar"
    """
    Alfa Aesar
    """
    acros_organics = "acros_organics"
    """
    Acros Organics
    """
    honeywell = "honeywell"
    """
    Honeywell
    """
    abcam = "abcam"
    """
    Abcam
    """
    cell_signaling_technology = "cell_signaling_technology"
    """
    Cell Signaling Technology
    """
    genscript = "genscript"
    """
    GenScript
    """
    addgene = "addgene"
    """
    Addgene
    """
    thomas_scientific = "thomas_scientific"
    """
    Thomas Scientific
    """
    cole_parmer = "cole_parmer"
    """
    Cole-Parmer
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

    experiment: Optional[list[Experiment]] = Field(default=None, description="""The experiment in a study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publication: Optional[str] = Field(default=None, description="""The publication identifier (e.g., PMID, DOI) for the study or \"not published\" if the study is unpublished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    annotator: Optional[list[str]] = Field(default=None, description="""ORCID identifier of the indidvidual submitting the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    lab: Optional[str] = Field(default=None, description="""ZFIN lab identifier of the laboratory that produced the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
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


class StudyCreate(ConfiguredBaseModel):
    """
    Create schema for Study — id is server-generated.
    """
    experiment: Optional[list[ExperimentCreate]] = Field(default=None, description="""The experiment in a study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publication: Optional[str] = Field(default=None, description="""The publication identifier (e.g., PMID, DOI) for the study or \"not published\" if the study is unpublished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    annotator: Optional[list[str]] = Field(default=None, description="""ORCID identifier of the indidvidual submitting the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    lab: Optional[str] = Field(default=None, description="""ZFIN lab identifier of the laboratory that produced the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })

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


class StudyUpdate(ConfiguredBaseModel):
    """
    Update schema for Study — all fields optional for partial updates.
    """
    experiment: Optional[list[Experiment]] = Field(default=None, description="""The experiment in a study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publication: Optional[str] = Field(default=None, description="""The publication identifier (e.g., PMID, DOI) for the study or \"not published\" if the study is unpublished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    annotator: Optional[list[str]] = Field(default=None, description="""ORCID identifier of the indidvidual submitting the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    lab: Optional[str] = Field(default=None, description="""ZFIN lab identifier of the laboratory that produced the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })

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


class StudyRead(ReadBaseModel):
    """
    Read schema for Study — from_attributes=True, extra=ignore.
    """
    experiment: Optional[list[ExperimentRead]] = Field(default=None, description="""The experiment in a study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publication: Optional[str] = Field(default=None, description="""The publication identifier (e.g., PMID, DOI) for the study or \"not published\" if the study is unpublished.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    annotator: Optional[list[str]] = Field(default=None, description="""ORCID identifier of the indidvidual submitting the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    lab: Optional[str] = Field(default=None, description="""ZFIN lab identifier of the laboratory that produced the study data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
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
    A group of observations (phenotypic outcomes and their control) that are linked by a common exposure event and subject, and that are part of a study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    standard_rearing_condition: Optional[bool] = Field(default=None, description="""An indication of whether the subject was maintained under standard conditions, which are the established, consistent environmental and husbandry parameters (such as temperature, lighting, diet, and housing) designed to minimize variability and ensure reproducibility in experiments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    rearing_condition_comment: Optional[str] = Field(default=None, description="""Comments on rearing conditions, for example, about how conditions deviated from standard parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    fish: Optional[Fish] = Field(default=None, description="""The fish subject of the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    control: Optional[list[Control]] = Field(default=None, description="""An observation that serves as the reference for assessing phenotypic outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    exposure_event: Optional[list[ExposureEvent]] = Field(default=None, description="""The exposure event in an experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ExperimentCreate(ConfiguredBaseModel):
    """
    Create schema for Experiment — id is server-generated.
    """
    standard_rearing_condition: Optional[bool] = Field(default=None, description="""An indication of whether the subject was maintained under standard conditions, which are the established, consistent environmental and husbandry parameters (such as temperature, lighting, diet, and housing) designed to minimize variability and ensure reproducibility in experiments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    rearing_condition_comment: Optional[str] = Field(default=None, description="""Comments on rearing conditions, for example, about how conditions deviated from standard parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    fish: Optional[Fish] = Field(default=None, description="""The fish subject of the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    control: Optional[list[ControlCreate]] = Field(default=None, description="""An observation that serves as the reference for assessing phenotypic outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    exposure_event: Optional[list[ExposureEventCreate]] = Field(default=None, description="""The exposure event in an experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })


class ExperimentUpdate(ConfiguredBaseModel):
    """
    Update schema for Experiment — all fields optional for partial updates.
    """
    standard_rearing_condition: Optional[bool] = Field(default=None, description="""An indication of whether the subject was maintained under standard conditions, which are the established, consistent environmental and husbandry parameters (such as temperature, lighting, diet, and housing) designed to minimize variability and ensure reproducibility in experiments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    rearing_condition_comment: Optional[str] = Field(default=None, description="""Comments on rearing conditions, for example, about how conditions deviated from standard parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    fish: Optional[Fish] = Field(default=None, description="""The fish subject of the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    control: Optional[list[Control]] = Field(default=None, description="""An observation that serves as the reference for assessing phenotypic outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    exposure_event: Optional[list[ExposureEvent]] = Field(default=None, description="""The exposure event in an experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })


class ExperimentRead(ReadBaseModel):
    """
    Read schema for Experiment — from_attributes=True, extra=ignore.
    """
    standard_rearing_condition: Optional[bool] = Field(default=None, description="""An indication of whether the subject was maintained under standard conditions, which are the established, consistent environmental and husbandry parameters (such as temperature, lighting, diet, and housing) designed to minimize variability and ensure reproducibility in experiments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    rearing_condition_comment: Optional[str] = Field(default=None, description="""Comments on rearing conditions, for example, about how conditions deviated from standard parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    fish: Optional[FishRead] = Field(default=None, description="""The fish subject of the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    control: Optional[list[ControlRead]] = Field(default=None, description="""An observation that serves as the reference for assessing phenotypic outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    exposure_event: Optional[list[ExposureEventRead]] = Field(default=None, description="""The exposure event in an experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class PhenotypeObservationSet(ZappEntity):
    """
    An observation set containing control and phenotypic outcome resulting from an exposure event.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    image: Optional[list[Image]] = Field(default=None, description="""Images associated with this observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    phenotype: Optional[list[Phenotype]] = Field(default=None, description="""The phenotype observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    control_image: Optional[list[ControlImage]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class PhenotypeObservationSetCreate(ConfiguredBaseModel):
    """
    Create schema for PhenotypeObservationSet — id is server-generated.
    """
    image: Optional[list[ImageCreate]] = Field(default=None, description="""Images associated with this observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    phenotype: Optional[list[PhenotypeCreate]] = Field(default=None, description="""The phenotype observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    control_image: Optional[list[ControlImageCreate]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })


class PhenotypeObservationSetUpdate(ConfiguredBaseModel):
    """
    Update schema for PhenotypeObservationSet — all fields optional for partial updates.
    """
    image: Optional[list[Image]] = Field(default=None, description="""Images associated with this observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    phenotype: Optional[list[Phenotype]] = Field(default=None, description="""The phenotype observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    control_image: Optional[list[ControlImage]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })


class PhenotypeObservationSetRead(ReadBaseModel):
    """
    Read schema for PhenotypeObservationSet — from_attributes=True, extra=ignore.
    """
    image: Optional[list[ImageRead]] = Field(default=None, description="""Images associated with this observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    phenotype: Optional[list[PhenotypeRead]] = Field(default=None, description="""The phenotype observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet']} })
    control_image: Optional[list[ControlImageRead]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })
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


class PhenotypeCreate(ConfiguredBaseModel):
    """
    Create schema for Phenotype — id is server-generated.
    """
    stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when the phenotype was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    prevalence: Optional[QuantityValue] = Field(default=None, description="""The percentage of subject exhibiting this phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[SeverityEnum] = Field(default=None, description="""The intensity of the observed phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    phenotype_term_id: Optional[PhenotypeTerm] = Field(default=None, description="""The phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })


class PhenotypeUpdate(ConfiguredBaseModel):
    """
    Update schema for Phenotype — all fields optional for partial updates.
    """
    stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when the phenotype was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    prevalence: Optional[QuantityValue] = Field(default=None, description="""The percentage of subject exhibiting this phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[SeverityEnum] = Field(default=None, description="""The intensity of the observed phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    phenotype_term_id: Optional[PhenotypeTerm] = Field(default=None, description="""The phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })


class PhenotypeRead(ReadBaseModel):
    """
    Read schema for Phenotype — from_attributes=True, extra=ignore.
    """
    stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when the phenotype was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    prevalence: Optional[QuantityValueRead] = Field(default=None, description="""The percentage of subject exhibiting this phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[SeverityEnum] = Field(default=None, description="""The intensity of the observed phenotype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    phenotype_term_id: Optional[PhenotypeTermRead] = Field(default=None, description="""The phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class Control(ZappEntity):
    """
    A subject serves as a reference for assessing phenotypic outcome in the phenotype observation set.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    control_type: Optional[str] = Field(default=None, description="""Type of control (e.g., wildtype vs mutant, treated vs untreated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    vehicle_if_treated: Optional[VehicleOfTransmission] = Field(default=None, description="""The vehicle used in a control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    control_image: Optional[list[ControlImage]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ControlCreate(ConfiguredBaseModel):
    """
    Create schema for Control — id is server-generated.
    """
    control_type: Optional[str] = Field(default=None, description="""Type of control (e.g., wildtype vs mutant, treated vs untreated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    vehicle_if_treated: Optional[VehicleOfTransmissionCreate] = Field(default=None, description="""The vehicle used in a control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    control_image: Optional[list[ControlImageCreate]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })


class ControlUpdate(ConfiguredBaseModel):
    """
    Update schema for Control — all fields optional for partial updates.
    """
    control_type: Optional[str] = Field(default=None, description="""Type of control (e.g., wildtype vs mutant, treated vs untreated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    vehicle_if_treated: Optional[VehicleOfTransmission] = Field(default=None, description="""The vehicle used in a control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    control_image: Optional[list[ControlImage]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })


class ControlRead(ReadBaseModel):
    """
    Read schema for Control — from_attributes=True, extra=ignore.
    """
    control_type: Optional[str] = Field(default=None, description="""Type of control (e.g., wildtype vs mutant, treated vs untreated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    vehicle_if_treated: Optional[VehicleOfTransmissionRead] = Field(default=None, description="""The vehicle used in a control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    control_image: Optional[list[ControlImageRead]] = Field(default=None, description="""Image associated with this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservationSet', 'Control']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ExposureEvent(ZappEntity):
    """
    An occurrence in a study where a subject is exposed to a stressor under defined conditions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['biolink:ExposureEvent'],
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    stressor: Optional[list[StressorChemical]] = Field(default=None, description="""Substance, chemical or toxicant that elicits a response (a phenotype) in a subject when encountered through exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    vehicle: Optional[list[VehicleOfTransmission]] = Field(default=None, description="""The substance or medium used to deliver a stressor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    route: Optional[ExposureRoute] = Field(default=None, description="""The route of exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    regimen: Optional[Regimen] = Field(default=None, description="""The regimen for the exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_start_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_end_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    exposure_type: Optional[ExposureType] = Field(default=None, description="""An instance of exposure specifying the type of stressor a subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    additional_exposure_condition: Optional[str] = Field(default=None, description="""Additional information about the conditions under which exposure event occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    phenotype_observation: Optional[list[PhenotypeObservationSet]] = Field(default=None, description="""The phenotype observation resulting from an exposure event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ExposureEventCreate(ConfiguredBaseModel):
    """
    Create schema for ExposureEvent — id is server-generated.
    """
    stressor: Optional[list[StressorChemicalCreate]] = Field(default=None, description="""Substance, chemical or toxicant that elicits a response (a phenotype) in a subject when encountered through exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    vehicle: Optional[list[VehicleOfTransmissionCreate]] = Field(default=None, description="""The substance or medium used to deliver a stressor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    route: Optional[ExposureRoute] = Field(default=None, description="""The route of exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    regimen: Optional[RegimenCreate] = Field(default=None, description="""The regimen for the exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_start_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_end_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    exposure_type: Optional[ExposureType] = Field(default=None, description="""An instance of exposure specifying the type of stressor a subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    additional_exposure_condition: Optional[str] = Field(default=None, description="""Additional information about the conditions under which exposure event occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    phenotype_observation: Optional[list[PhenotypeObservationSetCreate]] = Field(default=None, description="""The phenotype observation resulting from an exposure event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })


class ExposureEventUpdate(ConfiguredBaseModel):
    """
    Update schema for ExposureEvent — all fields optional for partial updates.
    """
    stressor: Optional[list[StressorChemical]] = Field(default=None, description="""Substance, chemical or toxicant that elicits a response (a phenotype) in a subject when encountered through exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    vehicle: Optional[list[VehicleOfTransmission]] = Field(default=None, description="""The substance or medium used to deliver a stressor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    route: Optional[ExposureRoute] = Field(default=None, description="""The route of exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    regimen: Optional[Regimen] = Field(default=None, description="""The regimen for the exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_start_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_end_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    exposure_type: Optional[ExposureType] = Field(default=None, description="""An instance of exposure specifying the type of stressor a subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    additional_exposure_condition: Optional[str] = Field(default=None, description="""Additional information about the conditions under which exposure event occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    phenotype_observation: Optional[list[PhenotypeObservationSet]] = Field(default=None, description="""The phenotype observation resulting from an exposure event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })


class ExposureEventRead(ReadBaseModel):
    """
    Read schema for ExposureEvent — from_attributes=True, extra=ignore.
    """
    stressor: Optional[list[StressorChemicalRead]] = Field(default=None, description="""Substance, chemical or toxicant that elicits a response (a phenotype) in a subject when encountered through exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    vehicle: Optional[list[VehicleOfTransmissionRead]] = Field(default=None, description="""The substance or medium used to deliver a stressor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    route: Optional[ExposureRouteRead] = Field(default=None, description="""The route of exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    regimen: Optional[RegimenRead] = Field(default=None, description="""The regimen for the exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_start_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_end_stage: Optional[str] = Field(default=None, description="""The developmental stage of fish when exposure ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    exposure_type: Optional[ExposureTypeRead] = Field(default=None, description="""An instance of exposure specifying the type of stressor a subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    additional_exposure_condition: Optional[str] = Field(default=None, description="""Additional information about the conditions under which exposure event occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    phenotype_observation: Optional[list[PhenotypeObservationSetRead]] = Field(default=None, description="""The phenotype observation resulting from an exposure event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
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


class RegimenCreate(ConfiguredBaseModel):
    """
    Create schema for Regimen — id is server-generated.
    """
    exposure_regimen_type: Optional[ExposureRegimenTypeEnum] = Field(default=None, description="""The type of exposure regimen (e.g., continuous or repeated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    interval_between_individual_exposures: Optional[QuantityValue] = Field(default=None, description="""Interval between individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    total_exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Time between first and last individual exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    individual_exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Individual exposure duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    number_of_individual_exposure: Optional[int] = Field(default=None, description="""Total number of individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })


class RegimenUpdate(ConfiguredBaseModel):
    """
    Update schema for Regimen — all fields optional for partial updates.
    """
    exposure_regimen_type: Optional[ExposureRegimenTypeEnum] = Field(default=None, description="""The type of exposure regimen (e.g., continuous or repeated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    interval_between_individual_exposures: Optional[QuantityValue] = Field(default=None, description="""Interval between individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    total_exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Time between first and last individual exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    individual_exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Individual exposure duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    number_of_individual_exposure: Optional[int] = Field(default=None, description="""Total number of individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })


class RegimenRead(ReadBaseModel):
    """
    Read schema for Regimen — from_attributes=True, extra=ignore.
    """
    exposure_regimen_type: Optional[ExposureRegimenTypeEnum] = Field(default=None, description="""The type of exposure regimen (e.g., continuous or repeated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    interval_between_individual_exposures: Optional[QuantityValueRead] = Field(default=None, description="""Interval between individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    total_exposure_duration: Optional[QuantityValueRead] = Field(default=None, description="""Time between first and last individual exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    individual_exposure_duration: Optional[QuantityValueRead] = Field(default=None, description="""Individual exposure duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    number_of_individual_exposure: Optional[int] = Field(default=None, description="""Total number of individual exposures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Regimen']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class StressorChemical(ZappEntity):
    """
    A chemical that elicits a response (a phenotype) in a subject when encountered through exposure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    chemical_id: Optional[str] = Field(default=None, description="""Chemical identifier (e.g., a CHEBI or other ontology URI) for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    cas_id: Optional[str] = Field(default=None, description="""CAS identifier for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    chemical_name: Optional[str] = Field(default=None, description="""Name of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    synonym: Optional[list[str]] = Field(default=None, description="""Other names for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: QuantityValue = Field(default=..., description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class StressorChemicalCreate(ConfiguredBaseModel):
    """
    Create schema for StressorChemical — id is server-generated.
    """
    chemical_id: Optional[str] = Field(default=None, description="""Chemical identifier (e.g., a CHEBI or other ontology URI) for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    cas_id: Optional[str] = Field(default=None, description="""CAS identifier for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    chemical_name: Optional[str] = Field(default=None, description="""Name of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    synonym: Optional[list[str]] = Field(default=None, description="""Other names for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: QuantityValue = Field(default=..., description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })


class StressorChemicalUpdate(ConfiguredBaseModel):
    """
    Update schema for StressorChemical — all fields optional for partial updates.
    """
    chemical_id: Optional[str] = Field(default=None, description="""Chemical identifier (e.g., a CHEBI or other ontology URI) for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    cas_id: Optional[str] = Field(default=None, description="""CAS identifier for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    chemical_name: Optional[str] = Field(default=None, description="""Name of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    synonym: Optional[list[str]] = Field(default=None, description="""Other names for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: Optional[QuantityValue] = Field(default=None, description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })


class StressorChemicalRead(ReadBaseModel):
    """
    Read schema for StressorChemical — from_attributes=True, extra=ignore.
    """
    chemical_id: Optional[str] = Field(default=None, description="""Chemical identifier (e.g., a CHEBI or other ontology URI) for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    cas_id: Optional[str] = Field(default=None, description="""CAS identifier for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    chemical_name: Optional[str] = Field(default=None, description="""Name of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    synonym: Optional[list[str]] = Field(default=None, description="""Other names for the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: QuantityValueRead = Field(default=..., description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class VehicleOfTransmission(ZappEntity):
    """
    The substance or medium used to deliver a stressor to a subject during an exposure event.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema',
         'slot_usage': {'concentration': {'name': 'concentration', 'required': False}}})

    vehicle_type: VehicleEnum = Field(default=..., description="""The type of vehicle used to deliver a stressor, drawn from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VehicleOfTransmission']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: Optional[QuantityValue] = Field(default=None, description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class VehicleOfTransmissionCreate(ConfiguredBaseModel):
    """
    Create schema for VehicleOfTransmission — id is server-generated.
    """
    vehicle_type: VehicleEnum = Field(default=..., description="""The type of vehicle used to deliver a stressor, drawn from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VehicleOfTransmission']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: Optional[QuantityValue] = Field(default=None, description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })


class VehicleOfTransmissionUpdate(ConfiguredBaseModel):
    """
    Update schema for VehicleOfTransmission — all fields optional for partial updates.
    """
    vehicle_type: Optional[VehicleEnum] = Field(default=None, description="""The type of vehicle used to deliver a stressor, drawn from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VehicleOfTransmission']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: Optional[QuantityValue] = Field(default=None, description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })


class VehicleOfTransmissionRead(ReadBaseModel):
    """
    Read schema for VehicleOfTransmission — from_attributes=True, extra=ignore.
    """
    vehicle_type: VehicleEnum = Field(default=..., description="""The type of vehicle used to deliver a stressor, drawn from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VehicleOfTransmission']} })
    manufacturer: Optional[ManufacturerEnum] = Field(default=None, description="""The manufacturer or supplier of the chemical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    concentration: Optional[QuantityValueRead] = Field(default=None, description="""The dose or concentration of the chemical to which the subject was exposed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StressorChemical', 'VehicleOfTransmission']} })
    comment: Optional[str] = Field(default=None, description="""Additional comments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control',
                       'ExposureEvent',
                       'StressorChemical',
                       'VehicleOfTransmission']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class Image(ZappEntity):
    """
    An image associated with a phenotype observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ImageCreate(ConfiguredBaseModel):
    """
    Create schema for Image — id is server-generated.
    """
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })


class ImageUpdate(ConfiguredBaseModel):
    """
    Update schema for Image — all fields optional for partial updates.
    """
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })


class ImageRead(ReadBaseModel):
    """
    Read schema for Image — from_attributes=True, extra=ignore.
    """
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ControlImage(ZappEntity):
    """
    An image associated with a control, taken at the same developmental stage as the corresponding phenotype observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    phenotype_id: Optional[str] = Field(default=None, description="""Foreign key reference to the PhenotypeObservationSet uuid (for database representation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    phenotype_comments: Optional[str] = Field(default=None, description="""Comments about the phenotype in the control image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class ControlImageCreate(ConfiguredBaseModel):
    """
    Create schema for ControlImage — id is server-generated.
    """
    phenotype_id: Optional[str] = Field(default=None, description="""Foreign key reference to the PhenotypeObservationSet uuid (for database representation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    phenotype_comments: Optional[str] = Field(default=None, description="""Comments about the phenotype in the control image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })


class ControlImageUpdate(ConfiguredBaseModel):
    """
    Update schema for ControlImage — all fields optional for partial updates.
    """
    phenotype_id: Optional[str] = Field(default=None, description="""Foreign key reference to the PhenotypeObservationSet uuid (for database representation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    phenotype_comments: Optional[str] = Field(default=None, description="""Comments about the phenotype in the control image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })


class ControlImageRead(ReadBaseModel):
    """
    Read schema for ControlImage — from_attributes=True, extra=ignore.
    """
    phenotype_id: Optional[str] = Field(default=None, description="""Foreign key reference to the PhenotypeObservationSet uuid (for database representation).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    magnification: Optional[str] = Field(default=None, description="""The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    resolution: Optional[str] = Field(default=None, description="""The level of detail in the image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    scale_bar: Optional[str] = Field(default=None, description="""Scale bar information, including the physical length it represents and the unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image', 'ControlImage']} })
    phenotype_comments: Optional[str] = Field(default=None, description="""Comments about the phenotype in the control image.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlImage']} })
    id: int = Field(default=..., description="""Auto-generated integer identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZappEntity']} })


class PhenotypeTerm(OntologyEntity):
    """
    A phenotype ontology term from the Zebrafish Phenotype ontology (ZP).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['biolink:PhenotypicFeature'],
         'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema'})

    term_uri: str = Field(default=..., description="""The URI of the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })
    term_label: Optional[str] = Field(default=None, description="""The human-readable label for the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })


class PhenotypeTermRead(ReadBaseModel):
    """
    Read schema for PhenotypeTerm — from_attributes=True, extra=ignore.
    """
    term_uri: str = Field(default=..., description="""The URI of the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })
    term_label: Optional[str] = Field(default=None, description="""The human-readable label for the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })


class ExposureRoute(OntologyEntity):
    """
    A route-of-exposure term. Term URIs are expected to be reachable from
    EXO:0000154 (route of exposure) in the EXO ontology.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema',
         'slot_usage': {'term_label': {'name': 'term_label', 'required': True}}})

    term_uri: str = Field(default=..., description="""The URI of the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })
    term_label: str = Field(default=..., description="""The human-readable label for the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })


class ExposureRouteRead(ReadBaseModel):
    """
    Read schema for ExposureRoute — from_attributes=True, extra=ignore.
    """
    term_uri: str = Field(default=..., description="""The URI of the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })
    term_label: str = Field(default=..., description="""The human-readable label for the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })


class ExposureType(OntologyEntity):
    """
    An exposure-type term from ECTO.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema',
         'slot_usage': {'term_label': {'name': 'term_label', 'required': True}}})

    term_uri: str = Field(default=..., description="""The URI of the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })
    term_label: str = Field(default=..., description="""The human-readable label for the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })


class ExposureTypeRead(ReadBaseModel):
    """
    Read schema for ExposureType — from_attributes=True, extra=ignore.
    """
    term_uri: str = Field(default=..., description="""The URI of the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })
    term_label: str = Field(default=..., description="""The human-readable label for the phenotype ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeTerm', 'ExposureRoute', 'ExposureType']} })


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


class FishRead(ReadBaseModel):
    """
    Read schema for Fish — from_attributes=True, extra=ignore.
    """
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


class QuantityValueRead(ReadBaseModel):
    """
    Read schema for QuantityValue — from_attributes=True, extra=ignore.
    """
    unit: Optional[str] = Field(default=None, description="""The unit of the quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    numeric_value: Optional[str] = Field(default=None, description="""The numeric value of the quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ZappEntity.model_rebuild()
OntologyEntity.model_rebuild()
ZfinEntity.model_rebuild()
Study.model_rebuild()
StudyCreate.model_rebuild()
StudyUpdate.model_rebuild()
StudyRead.model_rebuild()
Experiment.model_rebuild()
ExperimentCreate.model_rebuild()
ExperimentUpdate.model_rebuild()
ExperimentRead.model_rebuild()
PhenotypeObservationSet.model_rebuild()
PhenotypeObservationSetCreate.model_rebuild()
PhenotypeObservationSetUpdate.model_rebuild()
PhenotypeObservationSetRead.model_rebuild()
Phenotype.model_rebuild()
PhenotypeCreate.model_rebuild()
PhenotypeUpdate.model_rebuild()
PhenotypeRead.model_rebuild()
Control.model_rebuild()
ControlCreate.model_rebuild()
ControlUpdate.model_rebuild()
ControlRead.model_rebuild()
ExposureEvent.model_rebuild()
ExposureEventCreate.model_rebuild()
ExposureEventUpdate.model_rebuild()
ExposureEventRead.model_rebuild()
Regimen.model_rebuild()
RegimenCreate.model_rebuild()
RegimenUpdate.model_rebuild()
RegimenRead.model_rebuild()
StressorChemical.model_rebuild()
StressorChemicalCreate.model_rebuild()
StressorChemicalUpdate.model_rebuild()
StressorChemicalRead.model_rebuild()
VehicleOfTransmission.model_rebuild()
VehicleOfTransmissionCreate.model_rebuild()
VehicleOfTransmissionUpdate.model_rebuild()
VehicleOfTransmissionRead.model_rebuild()
Image.model_rebuild()
ImageCreate.model_rebuild()
ImageUpdate.model_rebuild()
ImageRead.model_rebuild()
ControlImage.model_rebuild()
ControlImageCreate.model_rebuild()
ControlImageUpdate.model_rebuild()
ControlImageRead.model_rebuild()
PhenotypeTerm.model_rebuild()
PhenotypeTermRead.model_rebuild()
ExposureRoute.model_rebuild()
ExposureRouteRead.model_rebuild()
ExposureType.model_rebuild()
ExposureTypeRead.model_rebuild()
Fish.model_rebuild()
FishRead.model_rebuild()
QuantityValue.model_rebuild()
QuantityValueRead.model_rebuild()

