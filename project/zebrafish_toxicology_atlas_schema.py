# Auto generated from zebrafish_toxicology_atlas_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-17T20:49:53
# Schema: zebrafish-toxicology-atlas-schema
#
# id: https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema
# description: Schema to represent metadatcha associated with the Zebrafish Toxicology Atlas
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
CAS = CurieNamespace('CAS', 'https://commonchemistry.cas.org/detail?cas_rn=')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EXO = CurieNamespace('EXO', 'http://purl.obolibrary.org/obo/EXO_')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ZFIN = CurieNamespace('ZFIN', 'https://zfin.org/')
ZP = CurieNamespace('ZP', 'http://purl.obolibrary.org/obo/ZP_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA = CurieNamespace('zebrafish_toxicology_atlas_schema', 'https://w3id.org/sierra-moxon/zebrafish-toxicology-atlas-schema/')
DEFAULT_ = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA


# Types

# Class references
class ZappEntityId(extended_int):
    pass


class ZfinEntityZfinId(extended_str):
    pass


class ChemicalEntityUri(URIorCURIE):
    pass


class PhenotypeTermTermUri(URIorCURIE):
    pass


class ExposureRouteTermUri(URIorCURIE):
    pass


class ExposureTypeTermUri(URIorCURIE):
    pass


class StudyId(ZappEntityId):
    pass


class ExperimentId(ZappEntityId):
    pass


class PhenotypeObservationSetId(ZappEntityId):
    pass


class PhenotypeId(ZappEntityId):
    pass


class ControlId(ZappEntityId):
    pass


class ExposureEventId(ZappEntityId):
    pass


class RegimenId(ZappEntityId):
    pass


class StressorChemicalId(ZappEntityId):
    pass


class ImageId(ZappEntityId):
    pass


class ControlImageId(ZappEntityId):
    pass


class FishZfinId(ZfinEntityZfinId):
    pass


@dataclass(repr=False)
class ZappEntity(YAMLRoot):
    """
    Internal entities with auto-generated integer IDs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["ZappEntity"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:ZappEntity"
    class_name: ClassVar[str] = "ZappEntity"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ZappEntity

    id: Union[int, ZappEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ZappEntityId):
            self.id = ZappEntityId(self.id)

        super().__post_init__(**kwargs)


class OntologyEntity(YAMLRoot):
    """
    Entities representing ontology terms with URI identifiers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["OntologyEntity"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:OntologyEntity"
    class_name: ClassVar[str] = "OntologyEntity"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.OntologyEntity


@dataclass(repr=False)
class ZfinEntity(YAMLRoot):
    """
    Entities with ZFIN database identifiers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["ZfinEntity"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:ZfinEntity"
    class_name: ClassVar[str] = "ZfinEntity"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ZfinEntity

    zfin_id: Union[str, ZfinEntityZfinId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.zfin_id):
            self.MissingRequiredField("zfin_id")
        if not isinstance(self.zfin_id, ZfinEntityZfinId):
            self.zfin_id = ZfinEntityZfinId(self.zfin_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(ZappEntity):
    """
    A toxicological investigation, including the experimental conditions and phenotypic outcomes, with information
    provenance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["Study"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Study

    id: Union[int, StudyId] = None
    experiment: Optional[Union[dict[Union[int, ExperimentId], Union[dict, "Experiment"]], list[Union[dict, "Experiment"]]]] = empty_dict()
    publication: Optional[str] = None
    annotator: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    lab: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        self._normalize_inlined_as_list(slot_name="experiment", slot_type=Experiment, key_name="id", keyed=True)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if not isinstance(self.annotator, list):
            self.annotator = [self.annotator] if self.annotator is not None else []
        self.annotator = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.annotator]

        if self.lab is not None and not isinstance(self.lab, URIorCURIE):
            self.lab = URIorCURIE(self.lab)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(ZappEntity):
    """
    A group of observations (phenotypic outcomes and their control) that are linked by a common exposure event and
    subject, and that are part of a study.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["Experiment"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Experiment

    id: Union[int, ExperimentId] = None
    standard_rearing_condition: Optional[Union[bool, Bool]] = None
    rearing_condition_comment: Optional[str] = None
    fish: Optional[Union[dict, "Fish"]] = None
    control: Optional[Union[dict[Union[int, ControlId], Union[dict, "Control"]], list[Union[dict, "Control"]]]] = empty_dict()
    exposure_event: Optional[Union[dict[Union[int, ExposureEventId], Union[dict, "ExposureEvent"]], list[Union[dict, "ExposureEvent"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentId):
            self.id = ExperimentId(self.id)

        if self.standard_rearing_condition is not None and not isinstance(self.standard_rearing_condition, Bool):
            self.standard_rearing_condition = Bool(self.standard_rearing_condition)

        if self.rearing_condition_comment is not None and not isinstance(self.rearing_condition_comment, str):
            self.rearing_condition_comment = str(self.rearing_condition_comment)

        if self.fish is not None and not isinstance(self.fish, Fish):
            self.fish = Fish(**as_dict(self.fish))

        self._normalize_inlined_as_list(slot_name="control", slot_type=Control, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="exposure_event", slot_type=ExposureEvent, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeObservationSet(ZappEntity):
    """
    An observation set containing control and phenotypic outcome resulting from an exposure event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["PhenotypeObservationSet"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:PhenotypeObservationSet"
    class_name: ClassVar[str] = "PhenotypeObservationSet"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.PhenotypeObservationSet

    id: Union[int, PhenotypeObservationSetId] = None
    image: Optional[Union[dict[Union[int, ImageId], Union[dict, "Image"]], list[Union[dict, "Image"]]]] = empty_dict()
    phenotype: Optional[Union[dict[Union[int, PhenotypeId], Union[dict, "Phenotype"]], list[Union[dict, "Phenotype"]]]] = empty_dict()
    control_image: Optional[Union[dict[Union[int, ControlImageId], Union[dict, "ControlImage"]], list[Union[dict, "ControlImage"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeObservationSetId):
            self.id = PhenotypeObservationSetId(self.id)

        self._normalize_inlined_as_list(slot_name="image", slot_type=Image, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="phenotype", slot_type=Phenotype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="control_image", slot_type=ControlImage, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(ZappEntity):
    """
    Any measurable or visible trait change in the subject as a result of exposure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["Phenotype"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Phenotype

    id: Union[int, PhenotypeId] = None
    stage: Optional[Union[str, URIorCURIE]] = None
    prevalence: Optional[Union[dict, "QuantityValue"]] = None
    severity: Optional[Union[str, "SeverityEnum"]] = None
    phenotype_term_id: Optional[Union[dict, "PhenotypeTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        if self.stage is not None and not isinstance(self.stage, URIorCURIE):
            self.stage = URIorCURIE(self.stage)

        if self.prevalence is not None and not isinstance(self.prevalence, QuantityValue):
            self.prevalence = QuantityValue(**as_dict(self.prevalence))

        if self.severity is not None and not isinstance(self.severity, SeverityEnum):
            self.severity = SeverityEnum(self.severity)

        if self.phenotype_term_id is not None and not isinstance(self.phenotype_term_id, PhenotypeTerm):
            self.phenotype_term_id = PhenotypeTerm(**as_dict(self.phenotype_term_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Control(ZappEntity):
    """
    A subject serves as a reference for assessing phenotypic outcome in the phenotype observation set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["Control"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:Control"
    class_name: ClassVar[str] = "Control"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Control

    id: Union[int, ControlId] = None
    control_type: Optional[str] = None
    vehicle_if_treated: Optional[Union[str, "VehicleEnumeration"]] = None
    comment: Optional[str] = None
    control_image: Optional[Union[dict[Union[int, ControlImageId], Union[dict, "ControlImage"]], list[Union[dict, "ControlImage"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlId):
            self.id = ControlId(self.id)

        if self.control_type is not None and not isinstance(self.control_type, str):
            self.control_type = str(self.control_type)

        if self.vehicle_if_treated is not None and not isinstance(self.vehicle_if_treated, VehicleEnumeration):
            self.vehicle_if_treated = VehicleEnumeration(self.vehicle_if_treated)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        self._normalize_inlined_as_list(slot_name="control_image", slot_type=ControlImage, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureEvent(ZappEntity):
    """
    An occurrence in a study where a subject is exposed to a stressor under defined conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["ExposureEvent"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:ExposureEvent"
    class_name: ClassVar[str] = "ExposureEvent"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ExposureEvent

    id: Union[int, ExposureEventId] = None
    stressor: Optional[Union[dict[Union[int, StressorChemicalId], Union[dict, "StressorChemical"]], list[Union[dict, "StressorChemical"]]]] = empty_dict()
    vehicle: Optional[Union[Union[str, "VehicleEnumeration"], list[Union[str, "VehicleEnumeration"]]]] = empty_list()
    route: Optional[Union[str, ExposureRouteTermUri]] = None
    regimen: Optional[Union[dict, "Regimen"]] = None
    exposure_start_stage: Optional[Union[str, URIorCURIE]] = None
    exposure_end_stage: Optional[Union[str, URIorCURIE]] = None
    comment: Optional[str] = None
    exposure_type: Optional[Union[str, ExposureTypeTermUri]] = None
    additional_exposure_condition: Optional[str] = None
    phenotype_observation: Optional[Union[dict[Union[int, PhenotypeObservationSetId], Union[dict, PhenotypeObservationSet]], list[Union[dict, PhenotypeObservationSet]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventId):
            self.id = ExposureEventId(self.id)

        self._normalize_inlined_as_list(slot_name="stressor", slot_type=StressorChemical, key_name="id", keyed=True)

        if not isinstance(self.vehicle, list):
            self.vehicle = [self.vehicle] if self.vehicle is not None else []
        self.vehicle = [v if isinstance(v, VehicleEnumeration) else VehicleEnumeration(v) for v in self.vehicle]

        if self.route is not None and not isinstance(self.route, ExposureRouteTermUri):
            self.route = ExposureRouteTermUri(self.route)

        if self.regimen is not None and not isinstance(self.regimen, Regimen):
            self.regimen = Regimen(**as_dict(self.regimen))

        if self.exposure_start_stage is not None and not isinstance(self.exposure_start_stage, URIorCURIE):
            self.exposure_start_stage = URIorCURIE(self.exposure_start_stage)

        if self.exposure_end_stage is not None and not isinstance(self.exposure_end_stage, URIorCURIE):
            self.exposure_end_stage = URIorCURIE(self.exposure_end_stage)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.exposure_type is not None and not isinstance(self.exposure_type, ExposureTypeTermUri):
            self.exposure_type = ExposureTypeTermUri(self.exposure_type)

        if self.additional_exposure_condition is not None and not isinstance(self.additional_exposure_condition, str):
            self.additional_exposure_condition = str(self.additional_exposure_condition)

        self._normalize_inlined_as_list(slot_name="phenotype_observation", slot_type=PhenotypeObservationSet, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Regimen(ZappEntity):
    """
    The schedule and pattern of an exposure event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["Regimen"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:Regimen"
    class_name: ClassVar[str] = "Regimen"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Regimen

    id: Union[int, RegimenId] = None
    exposure_regimen_type: Optional[Union[str, "ExposureRegimenTypeEnum"]] = None
    interval_between_individual_exposures: Optional[Union[dict, "QuantityValue"]] = None
    total_exposure_duration: Optional[Union[dict, "QuantityValue"]] = None
    individual_exposure_duration: Optional[Union[dict, "QuantityValue"]] = None
    number_of_individual_exposure: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegimenId):
            self.id = RegimenId(self.id)

        if self.exposure_regimen_type is not None and not isinstance(self.exposure_regimen_type, ExposureRegimenTypeEnum):
            self.exposure_regimen_type = ExposureRegimenTypeEnum(self.exposure_regimen_type)

        if self.interval_between_individual_exposures is not None and not isinstance(self.interval_between_individual_exposures, QuantityValue):
            self.interval_between_individual_exposures = QuantityValue(**as_dict(self.interval_between_individual_exposures))

        if self.total_exposure_duration is not None and not isinstance(self.total_exposure_duration, QuantityValue):
            self.total_exposure_duration = QuantityValue(**as_dict(self.total_exposure_duration))

        if self.individual_exposure_duration is not None and not isinstance(self.individual_exposure_duration, QuantityValue):
            self.individual_exposure_duration = QuantityValue(**as_dict(self.individual_exposure_duration))

        if self.number_of_individual_exposure is not None and not isinstance(self.number_of_individual_exposure, int):
            self.number_of_individual_exposure = int(self.number_of_individual_exposure)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StressorChemical(ZappEntity):
    """
    A chemical, that elicit a response (a phenotype) in a subject when when encountered through exposure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["StressorChemical"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:StressorChemical"
    class_name: ClassVar[str] = "StressorChemical"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.StressorChemical

    id: Union[int, StressorChemicalId] = None
    chemical_id: Union[dict, "ChemicalEntity"] = None
    concentration: Union[dict, "QuantityValue"] = None
    manufacturer: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StressorChemicalId):
            self.id = StressorChemicalId(self.id)

        if self._is_empty(self.chemical_id):
            self.MissingRequiredField("chemical_id")
        if not isinstance(self.chemical_id, ChemicalEntity):
            self.chemical_id = ChemicalEntity(**as_dict(self.chemical_id))

        if self._is_empty(self.concentration):
            self.MissingRequiredField("concentration")
        if not isinstance(self.concentration, QuantityValue):
            self.concentration = QuantityValue(**as_dict(self.concentration))

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image(ZappEntity):
    """
    An image associated with a phenotype observation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["Image"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Image

    id: Union[int, ImageId] = None
    magnification: Optional[str] = None
    resolution: Optional[str] = None
    scale_bar: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImageId):
            self.id = ImageId(self.id)

        if self.magnification is not None and not isinstance(self.magnification, str):
            self.magnification = str(self.magnification)

        if self.resolution is not None and not isinstance(self.resolution, str):
            self.resolution = str(self.resolution)

        if self.scale_bar is not None and not isinstance(self.scale_bar, str):
            self.scale_bar = str(self.scale_bar)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlImage(ZappEntity):
    """
    An image associated with a control, taken at the same developmental stage as the corresponding phenotype
    observation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["ControlImage"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:ControlImage"
    class_name: ClassVar[str] = "ControlImage"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ControlImage

    id: Union[int, ControlImageId] = None
    phenotype_id: Optional[str] = None
    magnification: Optional[str] = None
    resolution: Optional[str] = None
    scale_bar: Optional[str] = None
    phenotype_comments: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlImageId):
            self.id = ControlImageId(self.id)

        if self.phenotype_id is not None and not isinstance(self.phenotype_id, str):
            self.phenotype_id = str(self.phenotype_id)

        if self.magnification is not None and not isinstance(self.magnification, str):
            self.magnification = str(self.magnification)

        if self.resolution is not None and not isinstance(self.resolution, str):
            self.resolution = str(self.resolution)

        if self.scale_bar is not None and not isinstance(self.scale_bar, str):
            self.scale_bar = str(self.scale_bar)

        if self.phenotype_comments is not None and not isinstance(self.phenotype_comments, str):
            self.phenotype_comments = str(self.phenotype_comments)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(OntologyEntity):
    """
    The chemical used as the stressor chemical in an exposure event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ChemicalEntity

    uri: Union[str, ChemicalEntityUri] = None
    chebi_id: Optional[Union[str, URIorCURIE]] = None
    cas_id: Optional[str] = None
    chemical_name: Optional[str] = None
    synonym: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uri):
            self.MissingRequiredField("uri")
        if not isinstance(self.uri, ChemicalEntityUri):
            self.uri = ChemicalEntityUri(self.uri)

        if self.chebi_id is not None and not isinstance(self.chebi_id, URIorCURIE):
            self.chebi_id = URIorCURIE(self.chebi_id)

        if self.cas_id is not None and not isinstance(self.cas_id, str):
            self.cas_id = str(self.cas_id)

        if self.chemical_name is not None and not isinstance(self.chemical_name, str):
            self.chemical_name = str(self.chemical_name)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, str) else str(v) for v in self.synonym]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeTerm(OntologyEntity):
    """
    A phenotype ontology term from the Zebrafish Phenotype ontology (ZP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["PhenotypeTerm"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:PhenotypeTerm"
    class_name: ClassVar[str] = "PhenotypeTerm"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.PhenotypeTerm

    term_uri: Union[str, PhenotypeTermTermUri] = None
    term_label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term_uri):
            self.MissingRequiredField("term_uri")
        if not isinstance(self.term_uri, PhenotypeTermTermUri):
            self.term_uri = PhenotypeTermTermUri(self.term_uri)

        if self.term_label is not None and not isinstance(self.term_label, str):
            self.term_label = str(self.term_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureRoute(OntologyEntity):
    """
    A route-of-exposure term. Term URIs are expected to be reachable from
    EXO:0000154 (route of exposure) in the EXO ontology; the API enforces
    this at insert time by querying OLS/oaklib.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["ExposureRoute"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:ExposureRoute"
    class_name: ClassVar[str] = "ExposureRoute"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ExposureRoute

    term_uri: Union[str, ExposureRouteTermUri] = None
    term_label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term_uri):
            self.MissingRequiredField("term_uri")
        if not isinstance(self.term_uri, ExposureRouteTermUri):
            self.term_uri = ExposureRouteTermUri(self.term_uri)

        if self._is_empty(self.term_label):
            self.MissingRequiredField("term_label")
        if not isinstance(self.term_label, str):
            self.term_label = str(self.term_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureType(OntologyEntity):
    """
    An exposure-type term from ECTO. The API enforces ECTO membership at
    insert time by querying OLS/oaklib.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["ExposureType"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:ExposureType"
    class_name: ClassVar[str] = "ExposureType"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ExposureType

    term_uri: Union[str, ExposureTypeTermUri] = None
    term_label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term_uri):
            self.MissingRequiredField("term_uri")
        if not isinstance(self.term_uri, ExposureTypeTermUri):
            self.term_uri = ExposureTypeTermUri(self.term_uri)

        if self._is_empty(self.term_label):
            self.MissingRequiredField("term_label")
        if not isinstance(self.term_label, str):
            self.term_label = str(self.term_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fish(ZfinEntity):
    """
    Zebrafish used as subject in the study.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["Fish"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:Fish"
    class_name: ClassVar[str] = "Fish"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Fish

    zfin_id: Union[str, FishZfinId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.zfin_id):
            self.MissingRequiredField("zfin_id")
        if not isinstance(self.zfin_id, FishZfinId):
            self.zfin_id = FishZfinId(self.zfin_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA["QuantityValue"]
    class_class_curie: ClassVar[str] = "zebrafish_toxicology_atlas_schema:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.QuantityValue

    unit: Optional[str] = None
    numeric_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.numeric_value is not None and not isinstance(self.numeric_value, str):
            self.numeric_value = str(self.numeric_value)

        super().__post_init__(**kwargs)


# Enumerations
class SeverityEnum(EnumDefinitionImpl):
    """
    An enumeration of severity levels for phenotypes.
    """
    mild = PermissibleValue(
        text="mild",
        description="Mild severity")
    moderate = PermissibleValue(
        text="moderate",
        description="Moderate severity")
    severe = PermissibleValue(
        text="severe",
        description="Severe severity")

    _defn = EnumDefinition(
        name="SeverityEnum",
        description="An enumeration of severity levels for phenotypes.",
    )

class ExposureRegimenTypeEnum(EnumDefinitionImpl):
    """
    An enumeration of exposure regimen types.
    """
    continuous = PermissibleValue(
        text="continuous",
        description="Continuous exposure",
        meaning=EXO["0000109"])
    repeated = PermissibleValue(
        text="repeated",
        description="Repeated exposure",
        meaning=EXO["0000110"])

    _defn = EnumDefinition(
        name="ExposureRegimenTypeEnum",
        description="An enumeration of exposure regimen types.",
    )

class VehicleEnumeration(EnumDefinitionImpl):
    """
    An enumeration of vehicles used in exposures.
    """
    ethanol = PermissibleValue(
        text="ethanol",
        description="Ethanol",
        meaning=CHEBI["00000000"])
    dmso = PermissibleValue(
        text="dmso",
        description="DMSO",
        meaning=CHEBI["00000000"])

    _defn = EnumDefinition(
        name="VehicleEnumeration",
        description="An enumeration of vehicles used in exposures.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.id, name="id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.id, domain=None, range=URIRef)

slots.uri = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.uri, name="uri", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('uri'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.uri, domain=None, range=URIRef)

slots.term_uri = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.term_uri, name="term_uri", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('term_uri'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.term_uri, domain=None, range=URIRef)

slots.zfin_id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.zfin_id, name="zfin_id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('zfin_id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.zfin_id, domain=None, range=URIRef,
                   pattern=re.compile(r'^ZFIN:ZDB-[A-Z]+-\d{6}-\d+$'))

slots.publication = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.publication, name="publication", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('publication'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.publication, domain=None, range=Optional[str])

slots.synonym = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.synonym, name="synonym", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('synonym'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.synonym, domain=None, range=Optional[Union[str, list[str]]])

slots.name = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.name, name="name", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('name'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.name, domain=None, range=Optional[str])

slots.exposure_type = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_type, name="exposure_type", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('exposure_type'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_type, domain=None, range=Optional[Union[str, ExposureTypeTermUri]])

slots.unit = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.unit, name="unit", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('unit'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.unit, domain=None, range=Optional[str])

slots.numeric_value = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.numeric_value, name="numeric_value", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('numeric_value'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.numeric_value, domain=None, range=Optional[str])

slots.experiment = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.experiment, name="experiment", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('experiment'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.experiment, domain=None, range=Optional[Union[dict[Union[int, ExperimentId], Union[dict, Experiment]], list[Union[dict, Experiment]]]])

slots.phenotype_observation = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_observation, name="phenotype_observation", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('phenotype_observation'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_observation, domain=None, range=Optional[Union[dict[Union[int, PhenotypeObservationSetId], Union[dict, PhenotypeObservationSet]], list[Union[dict, PhenotypeObservationSet]]]])

slots.control = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control, name="control", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('control'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control, domain=None, range=Optional[Union[dict[Union[int, ControlId], Union[dict, Control]], list[Union[dict, Control]]]])

slots.fish = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.fish, name="fish", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('fish'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.fish, domain=None, range=Optional[Union[dict, Fish]])

slots.image = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.image, name="image", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('image'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.image, domain=None, range=Optional[Union[dict[Union[int, ImageId], Union[dict, Image]], list[Union[dict, Image]]]])

slots.phenotype = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype, name="phenotype", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('phenotype'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype, domain=None, range=Optional[Union[dict[Union[int, PhenotypeId], Union[dict, Phenotype]], list[Union[dict, Phenotype]]]])

slots.stage = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.stage, name="stage", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('stage'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.stage, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.prevalence = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.prevalence, name="prevalence", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('prevalence'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.prevalence, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.severity = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.severity, name="severity", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('severity'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.severity, domain=None, range=Optional[Union[str, "SeverityEnum"]])

slots.phenotype_term_id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_term_id, name="phenotype_term_id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('phenotype_term_id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_term_id, domain=None, range=Optional[Union[dict, PhenotypeTerm]])

slots.term_label = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.term_label, name="term_label", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('term_label'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.term_label, domain=None, range=Optional[str])

slots.control_type = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control_type, name="control_type", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('control_type'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control_type, domain=None, range=Optional[str])

slots.vehicle_if_treated = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.vehicle_if_treated, name="vehicle_if_treated", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('vehicle_if_treated'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.vehicle_if_treated, domain=None, range=Optional[Union[str, "VehicleEnumeration"]])

slots.control_id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control_id, name="control_id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('control_id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control_id, domain=None, range=Optional[str])

slots.control_image = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control_image, name="control_image", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('control_image'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.control_image, domain=None, range=Optional[Union[dict[Union[int, ControlImageId], Union[dict, ControlImage]], list[Union[dict, ControlImage]]]])

slots.phenotype_id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_id, name="phenotype_id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('phenotype_id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_id, domain=None, range=Optional[str])

slots.exposure_event = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_event, name="exposure_event", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('exposure_event'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_event, domain=None, range=Optional[Union[dict[Union[int, ExposureEventId], Union[dict, ExposureEvent]], list[Union[dict, ExposureEvent]]]])

slots.standard_rearing_condition = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.standard_rearing_condition, name="standard_rearing_condition", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('standard_rearing_condition'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.standard_rearing_condition, domain=None, range=Optional[Union[bool, Bool]])

slots.number_of_individual_exposure = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.number_of_individual_exposure, name="number_of_individual_exposure", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('number_of_individual_exposure'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.number_of_individual_exposure, domain=None, range=Optional[int])

slots.rearing_condition_comment = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.rearing_condition_comment, name="rearing_condition_comment", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('rearing_condition_comment'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.rearing_condition_comment, domain=None, range=Optional[str])

slots.stressor = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.stressor, name="stressor", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('stressor'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.stressor, domain=None, range=Optional[Union[dict[Union[int, StressorChemicalId], Union[dict, StressorChemical]], list[Union[dict, StressorChemical]]]])

slots.vehicle = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.vehicle, name="vehicle", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('vehicle'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.vehicle, domain=None, range=Optional[Union[Union[str, "VehicleEnumeration"], list[Union[str, "VehicleEnumeration"]]]])

slots.route = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.route, name="route", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('route'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.route, domain=None, range=Optional[Union[str, ExposureRouteTermUri]])

slots.regimen = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.regimen, name="regimen", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('regimen'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.regimen, domain=None, range=Optional[Union[dict, Regimen]])

slots.exposure_start_stage = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_start_stage, name="exposure_start_stage", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('exposure_start_stage'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_start_stage, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.exposure_end_stage = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_end_stage, name="exposure_end_stage", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('exposure_end_stage'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_end_stage, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.comment = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.comment, name="comment", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('comment'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.comment, domain=None, range=Optional[str])

slots.additional_exposure_condition = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.additional_exposure_condition, name="additional_exposure_condition", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('additional_exposure_condition'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.additional_exposure_condition, domain=None, range=Optional[str])

slots.chebi_id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.chebi_id, name="chebi_id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('chebi_id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.chebi_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.cas_id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.cas_id, name="cas_id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('cas_id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.cas_id, domain=None, range=Optional[str])

slots.chemical_name = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.chemical_name, name="chemical_name", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('chemical_name'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.chemical_name, domain=None, range=Optional[str])

slots.chemical_id = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.chemical_id, name="chemical_id", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('chemical_id'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.chemical_id, domain=None, range=Union[dict, ChemicalEntity])

slots.manufacturer = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.manufacturer, name="manufacturer", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('manufacturer'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.manufacturer, domain=None, range=Optional[str])

slots.concentration = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.concentration, name="concentration", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('concentration'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.concentration, domain=None, range=Union[dict, QuantityValue])

slots.interval_between_individual_exposures = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.interval_between_individual_exposures, name="interval_between_individual_exposures", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('interval_between_individual_exposures'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.interval_between_individual_exposures, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_exposure_duration = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.total_exposure_duration, name="total_exposure_duration", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('total_exposure_duration'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.total_exposure_duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.individual_exposure_duration = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.individual_exposure_duration, name="individual_exposure_duration", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('individual_exposure_duration'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.individual_exposure_duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exposure_regimen_type = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_regimen_type, name="exposure_regimen_type", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('exposure_regimen_type'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.exposure_regimen_type, domain=None, range=Optional[Union[str, "ExposureRegimenTypeEnum"]])

slots.magnification = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.magnification, name="magnification", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('magnification'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.magnification, domain=None, range=Optional[str])

slots.resolution = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.resolution, name="resolution", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('resolution'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.resolution, domain=None, range=Optional[str])

slots.scale_bar = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.scale_bar, name="scale_bar", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('scale_bar'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.scale_bar, domain=None, range=Optional[str])

slots.annotator = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.annotator, name="annotator", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('annotator'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.annotator, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^ORCID:[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$'))

slots.lab = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.lab, name="lab", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('lab'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.lab, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^ZFIN:ZDB-LAB-[0-9]+-[0-9]+$'))

slots.phenotype_comments = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_comments, name="phenotype_comments", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('phenotype_comments'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.phenotype_comments, domain=None, range=Optional[str])

slots.ExposureRoute_term_label = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.term_label, name="ExposureRoute_term_label", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('term_label'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ExposureRoute_term_label, domain=ExposureRoute, range=str)

slots.ExposureType_term_label = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.term_label, name="ExposureType_term_label", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('term_label'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.ExposureType_term_label, domain=ExposureType, range=str)

slots.Fish_name = Slot(uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.name, name="Fish_name", curie=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.curie('name'),
                   model_uri=ZEBRAFISH_TOXICOLOGY_ATLAS_SCHEMA.Fish_name, domain=Fish, range=str)
