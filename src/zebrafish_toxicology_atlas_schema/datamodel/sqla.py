from __future__ import annotations

from datetime import date, datetime, time
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    Text,
    Time,
)
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class ZappEntity(Base):
    """
    Internal entities with auto-generated integer IDs.
    """

    __tablename__ = "ZappEntity"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)

    def __repr__(self):
        return f"ZappEntity(id={self.id},)"


class OntologyEntity(Base):
    """
    Entities representing ontology terms with URI identifiers.
    """

    __tablename__ = "OntologyEntity"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)

    def __repr__(self):
        return f"OntologyEntity(id={self.id},)"


class ZfinEntity(Base):
    """
    Entities with ZFIN database identifiers.
    """

    __tablename__ = "ZfinEntity"

    zfin_id: Mapped[str] = mapped_column(Text(), primary_key=True)

    def __repr__(self):
        return f"ZfinEntity(zfin_id={self.zfin_id},)"


class QuantityValue(Base):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """

    __tablename__ = "QuantityValue"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    unit: Mapped[str | None] = mapped_column(Text())
    numeric_value: Mapped[str | None] = mapped_column(Text())

    def __repr__(self):
        return f"QuantityValue(id={self.id},unit={self.unit},numeric_value={self.numeric_value},)"


class StudyAnnotator(Base):
    """
    None
    """

    __tablename__ = "Study_annotator"

    Study_id: Mapped[int] = mapped_column(Integer(), ForeignKey("Study.id"), primary_key=True)
    annotator: Mapped[str] = mapped_column(Text(), primary_key=True)

    def __repr__(self):
        return f"Study_annotator(Study_id={self.Study_id},annotator={self.annotator},)"


class ExposureEventVehicle(Base):
    """
    None
    """

    __tablename__ = "ExposureEvent_vehicle"

    ExposureEvent_id: Mapped[int] = mapped_column(Integer(), ForeignKey("ExposureEvent.id"), primary_key=True)
    vehicle: Mapped[str] = mapped_column(Enum('ethanol', 'dmso', name='VehicleEnumeration'), primary_key=True)

    def __repr__(self):
        return f"ExposureEvent_vehicle(ExposureEvent_id={self.ExposureEvent_id},vehicle={self.vehicle},)"


class ChemicalEntitySynonym(Base):
    """
    None
    """

    __tablename__ = "ChemicalEntity_synonym"

    ChemicalEntity_uri: Mapped[str] = mapped_column(Text(), ForeignKey("ChemicalEntity.uri"), primary_key=True)
    synonym: Mapped[str] = mapped_column(Text(), primary_key=True)

    def __repr__(self):
        return f"ChemicalEntity_synonym(ChemicalEntity_uri={self.ChemicalEntity_uri},synonym={self.synonym},)"


class Study(ZappEntity):
    """
    A toxicological investigation, including the experimental conditions and phenotypic outcomes, with information provenance.
    """

    __tablename__ = "Study"

    publication: Mapped[str | None] = mapped_column(Text())
    lab: Mapped[str | None] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)

    # One-To-Many: OneToAnyMapping(source_class='Study', source_slot='experiment', mapping_type=None, target_class='Experiment', target_slot='Study_id', join_class=None, uses_join_table=None, multivalued=False)
    experiment: Mapped[list[Experiment]] = relationship(foreign_keys="[Experiment.Study_id]")

    annotator_rel: Mapped[list[StudyAnnotator]] = relationship()
    annotator: AssociationProxy[list[str]] = association_proxy(
        "annotator_rel",
        "annotator",
        creator=lambda x_: StudyAnnotator(annotator=x_),
    )

    def __repr__(self):
        return f"Study(publication={self.publication},lab={self.lab},id={self.id},)"

    __mapper_args__ = {"concrete": True}


class Experiment(ZappEntity):
    """
    A group of observations (phenotypic outcomes and their control) that are linked by a common exposure event and subject, and that are part of a study.
    """

    __tablename__ = "Experiment"

    standard_rearing_condition: Mapped[bool | None] = mapped_column(Boolean())
    rearing_condition_comment: Mapped[str | None] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    Study_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("Study.id"))
    fish_zfin_id: Mapped[str | None] = mapped_column(Text(), ForeignKey("Fish.zfin_id"))
    fish: Mapped[Fish | None] = relationship(foreign_keys=[fish_zfin_id])

    # One-To-Many: OneToAnyMapping(source_class='Experiment', source_slot='control', mapping_type=None, target_class='Control', target_slot='Experiment_id', join_class=None, uses_join_table=None, multivalued=False)
    control: Mapped[list[Control]] = relationship(foreign_keys="[Control.Experiment_id]")

    # One-To-Many: OneToAnyMapping(source_class='Experiment', source_slot='exposure_event', mapping_type=None, target_class='ExposureEvent', target_slot='Experiment_id', join_class=None, uses_join_table=None, multivalued=False)
    exposure_event: Mapped[list[ExposureEvent]] = relationship(foreign_keys="[ExposureEvent.Experiment_id]")

    def __repr__(self):
        return f"Experiment(standard_rearing_condition={self.standard_rearing_condition},rearing_condition_comment={self.rearing_condition_comment},id={self.id},Study_id={self.Study_id},fish_zfin_id={self.fish_zfin_id},)"

    __mapper_args__ = {"concrete": True}


class PhenotypeObservationSet(ZappEntity):
    """
    An observation set containing control and phenotypic outcome resulting from an exposure event.
    """

    __tablename__ = "PhenotypeObservationSet"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    ExposureEvent_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("ExposureEvent.id"))

    # One-To-Many: OneToAnyMapping(source_class='PhenotypeObservationSet', source_slot='image', mapping_type=None, target_class='Image', target_slot='PhenotypeObservationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    image: Mapped[list[Image]] = relationship(foreign_keys="[Image.PhenotypeObservationSet_id]")

    # One-To-Many: OneToAnyMapping(source_class='PhenotypeObservationSet', source_slot='phenotype', mapping_type=None, target_class='Phenotype', target_slot='PhenotypeObservationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    phenotype: Mapped[list[Phenotype]] = relationship(foreign_keys="[Phenotype.PhenotypeObservationSet_id]")

    # One-To-Many: OneToAnyMapping(source_class='PhenotypeObservationSet', source_slot='control_image', mapping_type=None, target_class='ControlImage', target_slot='PhenotypeObservationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    control_image: Mapped[list[ControlImage]] = relationship(foreign_keys="[ControlImage.PhenotypeObservationSet_id]")

    def __repr__(self):
        return f"PhenotypeObservationSet(id={self.id},ExposureEvent_id={self.ExposureEvent_id},)"

    __mapper_args__ = {"concrete": True}


class Phenotype(ZappEntity):
    """
    Any measurable or visible trait change in the subject as a result of exposure.
    """

    __tablename__ = "Phenotype"

    stage: Mapped[str | None] = mapped_column(Text())
    severity: Mapped[str | None] = mapped_column(Enum('mild', 'moderate', 'severe', name='SeverityEnum'))
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    PhenotypeObservationSet_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("PhenotypeObservationSet.id"))
    prevalence_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("QuantityValue.id"))
    prevalence: Mapped[QuantityValue | None] = relationship(foreign_keys=[prevalence_id])
    phenotype_term_id_term_uri: Mapped[str | None] = mapped_column(Text(), ForeignKey("PhenotypeTerm.term_uri"))
    phenotype_term_id: Mapped[PhenotypeTerm | None] = relationship(foreign_keys=[phenotype_term_id_term_uri])

    def __repr__(self):
        return f"Phenotype(stage={self.stage},severity={self.severity},id={self.id},PhenotypeObservationSet_id={self.PhenotypeObservationSet_id},prevalence_id={self.prevalence_id},phenotype_term_id_term_uri={self.phenotype_term_id_term_uri},)"

    __mapper_args__ = {"concrete": True}


class Control(ZappEntity):
    """
    A subject serves as a reference for assessing phenotypic outcome in the phenotype observation set.
    """

    __tablename__ = "Control"

    control_type: Mapped[str | None] = mapped_column(Text())
    vehicle_if_treated: Mapped[str | None] = mapped_column(Enum('ethanol', 'dmso', name='VehicleEnumeration'))
    comment: Mapped[str | None] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    Experiment_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("Experiment.id"))

    # One-To-Many: OneToAnyMapping(source_class='Control', source_slot='control_image', mapping_type=None, target_class='ControlImage', target_slot='Control_id', join_class=None, uses_join_table=None, multivalued=False)
    control_image: Mapped[list[ControlImage]] = relationship(foreign_keys="[ControlImage.Control_id]")

    def __repr__(self):
        return f"Control(control_type={self.control_type},vehicle_if_treated={self.vehicle_if_treated},comment={self.comment},id={self.id},Experiment_id={self.Experiment_id},)"

    __mapper_args__ = {"concrete": True}


class ExposureEvent(ZappEntity):
    """
    An occurrence in a study where a subject is exposed to a stressor under defined conditions.
    """

    __tablename__ = "ExposureEvent"

    exposure_start_stage: Mapped[str | None] = mapped_column(Text())
    exposure_end_stage: Mapped[str | None] = mapped_column(Text())
    comment: Mapped[str | None] = mapped_column(Text())
    additional_exposure_condition: Mapped[str | None] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    Experiment_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("Experiment.id"))
    route_term_uri: Mapped[str | None] = mapped_column(Text(), ForeignKey("ExposureRoute.term_uri"))
    route: Mapped[ExposureRoute | None] = relationship(foreign_keys=[route_term_uri])
    regimen_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("Regimen.id"))
    regimen: Mapped[Regimen | None] = relationship(foreign_keys=[regimen_id])
    exposure_type_term_uri: Mapped[str | None] = mapped_column(Text(), ForeignKey("ExposureType.term_uri"))
    exposure_type: Mapped[ExposureType | None] = relationship(foreign_keys=[exposure_type_term_uri])

    # One-To-Many: OneToAnyMapping(source_class='ExposureEvent', source_slot='stressor', mapping_type=None, target_class='StressorChemical', target_slot='ExposureEvent_id', join_class=None, uses_join_table=None, multivalued=False)
    stressor: Mapped[list[StressorChemical]] = relationship(foreign_keys="[StressorChemical.ExposureEvent_id]")

    vehicle_rel: Mapped[list[ExposureEventVehicle]] = relationship()
    vehicle: AssociationProxy[list[str]] = association_proxy(
        "vehicle_rel",
        "vehicle",
        creator=lambda x_: ExposureEventVehicle(vehicle=x_),
    )

    # One-To-Many: OneToAnyMapping(source_class='ExposureEvent', source_slot='phenotype_observation', mapping_type=None, target_class='PhenotypeObservationSet', target_slot='ExposureEvent_id', join_class=None, uses_join_table=None, multivalued=False)
    phenotype_observation: Mapped[list[PhenotypeObservationSet]] = relationship(foreign_keys="[PhenotypeObservationSet.ExposureEvent_id]")

    def __repr__(self):
        return f"ExposureEvent(exposure_start_stage={self.exposure_start_stage},exposure_end_stage={self.exposure_end_stage},comment={self.comment},additional_exposure_condition={self.additional_exposure_condition},id={self.id},Experiment_id={self.Experiment_id},route_term_uri={self.route_term_uri},regimen_id={self.regimen_id},exposure_type_term_uri={self.exposure_type_term_uri},)"

    __mapper_args__ = {"concrete": True}


class Regimen(ZappEntity):
    """
    The schedule and pattern of an exposure event.
    """

    __tablename__ = "Regimen"

    exposure_regimen_type: Mapped[str | None] = mapped_column(Enum('continuous', 'repeated', name='ExposureRegimenTypeEnum'))
    number_of_individual_exposure: Mapped[int | None] = mapped_column(Integer())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    interval_between_individual_exposures_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("QuantityValue.id"))
    interval_between_individual_exposures: Mapped[QuantityValue | None] = relationship(foreign_keys=[interval_between_individual_exposures_id])
    total_exposure_duration_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("QuantityValue.id"))
    total_exposure_duration: Mapped[QuantityValue | None] = relationship(foreign_keys=[total_exposure_duration_id])
    individual_exposure_duration_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("QuantityValue.id"))
    individual_exposure_duration: Mapped[QuantityValue | None] = relationship(foreign_keys=[individual_exposure_duration_id])

    def __repr__(self):
        return f"Regimen(exposure_regimen_type={self.exposure_regimen_type},number_of_individual_exposure={self.number_of_individual_exposure},id={self.id},interval_between_individual_exposures_id={self.interval_between_individual_exposures_id},total_exposure_duration_id={self.total_exposure_duration_id},individual_exposure_duration_id={self.individual_exposure_duration_id},)"

    __mapper_args__ = {"concrete": True}


class StressorChemical(ZappEntity):
    """
    A chemical, that elicit a response (a phenotype) in a subject when when encountered through exposure.
    """

    __tablename__ = "StressorChemical"

    manufacturer: Mapped[str | None] = mapped_column(Text())
    comment: Mapped[str | None] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    ExposureEvent_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("ExposureEvent.id"))
    chemical_id_uri: Mapped[str] = mapped_column(Text(), ForeignKey("ChemicalEntity.uri"))
    chemical_id: Mapped[ChemicalEntity | None] = relationship(foreign_keys=[chemical_id_uri])
    concentration_id: Mapped[int] = mapped_column(Integer(), ForeignKey("QuantityValue.id"))
    concentration: Mapped[QuantityValue | None] = relationship(foreign_keys=[concentration_id])

    def __repr__(self):
        return f"StressorChemical(manufacturer={self.manufacturer},comment={self.comment},id={self.id},ExposureEvent_id={self.ExposureEvent_id},chemical_id_uri={self.chemical_id_uri},concentration_id={self.concentration_id},)"

    __mapper_args__ = {"concrete": True}


class Image(ZappEntity):
    """
    An image associated with a phenotype observation.
    """

    __tablename__ = "Image"

    magnification: Mapped[str | None] = mapped_column(Text())
    resolution: Mapped[str | None] = mapped_column(Text())
    scale_bar: Mapped[str | None] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    PhenotypeObservationSet_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("PhenotypeObservationSet.id"))

    def __repr__(self):
        return f"Image(magnification={self.magnification},resolution={self.resolution},scale_bar={self.scale_bar},id={self.id},PhenotypeObservationSet_id={self.PhenotypeObservationSet_id},)"

    __mapper_args__ = {"concrete": True}


class ControlImage(ZappEntity):
    """
    An image associated with a control, taken at the same developmental stage as the corresponding phenotype observation.
    """

    __tablename__ = "ControlImage"

    phenotype_id: Mapped[str | None] = mapped_column(Text())
    magnification: Mapped[str | None] = mapped_column(Text())
    resolution: Mapped[str | None] = mapped_column(Text())
    scale_bar: Mapped[str | None] = mapped_column(Text())
    phenotype_comments: Mapped[str | None] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    PhenotypeObservationSet_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("PhenotypeObservationSet.id"))
    Control_id: Mapped[int | None] = mapped_column(Integer(), ForeignKey("Control.id"))

    def __repr__(self):
        return f"ControlImage(phenotype_id={self.phenotype_id},magnification={self.magnification},resolution={self.resolution},scale_bar={self.scale_bar},phenotype_comments={self.phenotype_comments},id={self.id},PhenotypeObservationSet_id={self.PhenotypeObservationSet_id},Control_id={self.Control_id},)"

    __mapper_args__ = {"concrete": True}


class ChemicalEntity(OntologyEntity):
    """
    The chemical used as the stressor chemical in an exposure event.
    """

    __tablename__ = "ChemicalEntity"

    uri: Mapped[str] = mapped_column(Text(), primary_key=True)
    chebi_id: Mapped[str] = mapped_column(Text(), primary_key=True)
    cas_id: Mapped[str] = mapped_column(Text(), primary_key=True)
    chemical_name: Mapped[str] = mapped_column(Text(), primary_key=True)

    synonym_rel: Mapped[list[ChemicalEntitySynonym]] = relationship()
    synonym: AssociationProxy[list[str]] = association_proxy(
        "synonym_rel",
        "synonym",
        creator=lambda x_: ChemicalEntitySynonym(synonym=x_),
    )

    def __repr__(self):
        return f"ChemicalEntity(uri={self.uri},chebi_id={self.chebi_id},cas_id={self.cas_id},chemical_name={self.chemical_name},)"

    __mapper_args__ = {"concrete": True}


class PhenotypeTerm(OntologyEntity):
    """
    A phenotype ontology term from the Zebrafish Phenotype ontology (ZP).
    """

    __tablename__ = "PhenotypeTerm"

    term_uri: Mapped[str] = mapped_column(Text(), primary_key=True)
    term_label: Mapped[str] = mapped_column(Text(), primary_key=True)

    def __repr__(self):
        return f"PhenotypeTerm(term_uri={self.term_uri},term_label={self.term_label},)"

    __mapper_args__ = {"concrete": True}


class ExposureRoute(OntologyEntity):
    """
    A route-of-exposure term. Term URIs are expected to be reachable from
EXO:0000154 (route of exposure) in the EXO ontology; the API enforces
this at insert time by querying OLS/oaklib.

    """

    __tablename__ = "ExposureRoute"

    term_uri: Mapped[str] = mapped_column(Text(), primary_key=True)
    term_label: Mapped[str] = mapped_column(Text(), primary_key=True)

    def __repr__(self):
        return f"ExposureRoute(term_uri={self.term_uri},term_label={self.term_label},)"

    __mapper_args__ = {"concrete": True}


class ExposureType(OntologyEntity):
    """
    An exposure-type term from ECTO. The API enforces ECTO membership at
insert time by querying OLS/oaklib.

    """

    __tablename__ = "ExposureType"

    term_uri: Mapped[str] = mapped_column(Text(), primary_key=True)
    term_label: Mapped[str] = mapped_column(Text(), primary_key=True)

    def __repr__(self):
        return f"ExposureType(term_uri={self.term_uri},term_label={self.term_label},)"

    __mapper_args__ = {"concrete": True}


class Fish(ZfinEntity):
    """
    Zebrafish used as subject in the study.
    """

    __tablename__ = "Fish"

    name: Mapped[str] = mapped_column(Text())
    zfin_id: Mapped[str] = mapped_column(Text(), primary_key=True)

    def __repr__(self):
        return f"Fish(name={self.name},zfin_id={self.zfin_id},)"

    __mapper_args__ = {"concrete": True}

