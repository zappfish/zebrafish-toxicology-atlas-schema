
from typing import List, Optional
from decimal import Decimal
from datetime import date, datetime, time

from sqlalchemy import ForeignKey, Index, Table, String, Text, Integer, Float, Numeric, Boolean, Time, DateTime, Date, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy

class Base(DeclarativeBase):
    pass

metadata = Base.metadata


class ZappEntity(Base):
    """
    Internal entities with auto-generated integer IDs.
    """
    __tablename__ = 'ZappEntity'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    

    def __repr__(self):
        return f"ZappEntity(id={self.id},)"


    


class OntologyEntity(Base):
    """
    Entities representing ontology terms with URI identifiers.
    """
    __tablename__ = 'OntologyEntity'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    

    def __repr__(self):
        return f"OntologyEntity(id={self.id},)"


    


class ZfinEntity(Base):
    """
    Entities with ZFIN database identifiers.
    """
    __tablename__ = 'ZfinEntity'

    zfin_id: Mapped[str] = mapped_column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ZfinEntity(zfin_id={self.zfin_id},)"


    


class QuantityValue(Base):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    __tablename__ = 'QuantityValue'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    unit: Mapped[Optional[str]] = mapped_column(Text())
    numeric_value: Mapped[Optional[str]] = mapped_column(Text())
    

    def __repr__(self):
        return f"QuantityValue(id={self.id},unit={self.unit},numeric_value={self.numeric_value},)"


    


class StudyAnnotator(Base):
    """
    None
    """
    __tablename__ = 'Study_annotator'

    Study_id: Mapped[int] = mapped_column(Integer(), ForeignKey('Study.id'), primary_key=True)
    annotator: Mapped[str] = mapped_column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_annotator(Study_id={self.Study_id},annotator={self.annotator},)"


    


class ExposureEventVehicle(Base):
    """
    None
    """
    __tablename__ = 'ExposureEvent_vehicle'

    ExposureEvent_id: Mapped[int] = mapped_column(Integer(), ForeignKey('ExposureEvent.id'), primary_key=True)
    vehicle: Mapped[str] = mapped_column(Enum('ethanol', 'dmso', name='VehicleEnum'), primary_key=True)
    

    def __repr__(self):
        return f"ExposureEvent_vehicle(ExposureEvent_id={self.ExposureEvent_id},vehicle={self.vehicle},)"


    


class ChemicalEntitySynonym(Base):
    """
    None
    """
    __tablename__ = 'ChemicalEntity_synonym'

    ChemicalEntity_uri: Mapped[int] = mapped_column(Integer(), ForeignKey('ChemicalEntity.uri'), primary_key=True)
    synonym: Mapped[str] = mapped_column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ChemicalEntity_synonym(ChemicalEntity_uri={self.ChemicalEntity_uri},synonym={self.synonym},)"


    


class Study(ZappEntity):
    """
    A toxicological investigation, including the experimental conditions and phenotypic outcomes, with information provenance.
    """
    __tablename__ = 'Study'

    publication: Mapped[Optional[str]] = mapped_column(Text())
    lab: Mapped[Optional[str]] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    
    
    # One-To-Many: OneToAnyMapping(source_class='Study', source_slot='experiment', mapping_type=None, target_class='Experiment', target_slot='Study_id', join_class=None, uses_join_table=None, multivalued=False)
    experiment: Mapped[List["Experiment"]] = relationship(foreign_keys="[Experiment.Study_id]")
    
    
    annotator_rel: Mapped[List["StudyAnnotator"]] = relationship()
    annotator: AssociationProxy[List[str]] = association_proxy("annotator_rel", "annotator",
                                  creator=lambda x_: StudyAnnotator(annotator=x_))
    

    def __repr__(self):
        return f"Study(publication={self.publication},lab={self.lab},id={self.id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Experiment(ZappEntity):
    """
    Group of observations (phenotypic outcomes and their control) that are linked by a common experiment and subject that are part of a study.
    """
    __tablename__ = 'Experiment'

    standard_rearing_condition: Mapped[Optional[bool]] = mapped_column(Boolean())
    rearing_condition_comment: Mapped[Optional[str]] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    Study_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('Study.id'))
    fish_zfin_id: Mapped[Optional[str]] = mapped_column(Text(), ForeignKey('Fish.zfin_id'))
    fish: Mapped[Optional["Fish"]] = relationship(foreign_keys=[fish_zfin_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Experiment', source_slot='control', mapping_type=None, target_class='Control', target_slot='Experiment_id', join_class=None, uses_join_table=None, multivalued=False)
    control: Mapped[List["Control"]] = relationship(foreign_keys="[Control.Experiment_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Experiment', source_slot='exposure_event', mapping_type=None, target_class='ExposureEvent', target_slot='Experiment_id', join_class=None, uses_join_table=None, multivalued=False)
    exposure_event: Mapped[List["ExposureEvent"]] = relationship(foreign_keys="[ExposureEvent.Experiment_id]")
    

    def __repr__(self):
        return f"Experiment(standard_rearing_condition={self.standard_rearing_condition},rearing_condition_comment={self.rearing_condition_comment},id={self.id},Study_id={self.Study_id},fish_zfin_id={self.fish_zfin_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PhenotypeObservationSet(ZappEntity):
    """
    A phenotypic outcome resulting from an exposure event.
    """
    __tablename__ = 'PhenotypeObservationSet'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    ExposureEvent_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('ExposureEvent.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PhenotypeObservationSet', source_slot='image', mapping_type=None, target_class='Image', target_slot='PhenotypeObservationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    image: Mapped[List["Image"]] = relationship(foreign_keys="[Image.PhenotypeObservationSet_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PhenotypeObservationSet', source_slot='phenotype', mapping_type=None, target_class='Phenotype', target_slot='PhenotypeObservationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    phenotype: Mapped[List["Phenotype"]] = relationship(foreign_keys="[Phenotype.PhenotypeObservationSet_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PhenotypeObservationSet', source_slot='control_image', mapping_type=None, target_class='ControlImage', target_slot='PhenotypeObservationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    control_image: Mapped[List["ControlImage"]] = relationship(foreign_keys="[ControlImage.PhenotypeObservationSet_id]")
    

    def __repr__(self):
        return f"PhenotypeObservationSet(id={self.id},ExposureEvent_id={self.ExposureEvent_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Phenotype(ZappEntity):
    """
    Any measurable or visible trait change in the subject as a result of exposure.
    """
    __tablename__ = 'Phenotype'

    stage: Mapped[Optional[str]] = mapped_column(Text())
    severity: Mapped[Optional[str]] = mapped_column(Enum('mild', 'moderate', 'severe', name='SeverityEnum'))
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    PhenotypeObservationSet_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('PhenotypeObservationSet.id'))
    prevalence_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('QuantityValue.id'))
    prevalence: Mapped[Optional["QuantityValue"]] = relationship(foreign_keys=[prevalence_id])
    phenotype_term_id_term_uri: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('PhenotypeTerm.term_uri'))
    phenotype_term_id: Mapped[Optional["PhenotypeTerm"]] = relationship(foreign_keys=[phenotype_term_id_term_uri])
    

    def __repr__(self):
        return f"Phenotype(stage={self.stage},severity={self.severity},id={self.id},PhenotypeObservationSet_id={self.PhenotypeObservationSet_id},prevalence_id={self.prevalence_id},phenotype_term_id_term_uri={self.phenotype_term_id_term_uri},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Control(ZappEntity):
    """
    Information about controls used in the experiment, including the type of control (wildtype vs mutant, treated vs untreated) and vehicle information if applicable.
    """
    __tablename__ = 'Control'

    control_type: Mapped[Optional[str]] = mapped_column(Text())
    vehicle_if_treated: Mapped[Optional[str]] = mapped_column(Enum('ethanol', 'dmso', name='VehicleEnum'))
    comment: Mapped[Optional[str]] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    Experiment_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('Experiment.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Control', source_slot='control_image', mapping_type=None, target_class='ControlImage', target_slot='Control_id', join_class=None, uses_join_table=None, multivalued=False)
    control_image: Mapped[List["ControlImage"]] = relationship(foreign_keys="[ControlImage.Control_id]")
    

    def __repr__(self):
        return f"Control(control_type={self.control_type},vehicle_if_treated={self.vehicle_if_treated},comment={self.comment},id={self.id},Experiment_id={self.Experiment_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ExposureEvent(ZappEntity):
    """
    An occurrence in a study where a subject is exposed to a stressor under defined conditions.
    """
    __tablename__ = 'ExposureEvent'

    route: Mapped[Optional[str]] = mapped_column(Enum(name='ExposureRouteEnum'))
    exposure_start_stage: Mapped[Optional[str]] = mapped_column(Text())
    exposure_end_stage: Mapped[Optional[str]] = mapped_column(Text())
    comment: Mapped[Optional[str]] = mapped_column(Text())
    exposure_type: Mapped[Optional[str]] = mapped_column(Enum(name='ExposureTypeEnum'))
    additional_exposure_condition: Mapped[Optional[str]] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    Experiment_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('Experiment.id'))
    regimen_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('Regimen.id'))
    regimen: Mapped[Optional["Regimen"]] = relationship(foreign_keys=[regimen_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ExposureEvent', source_slot='stressor', mapping_type=None, target_class='StressorChemical', target_slot='ExposureEvent_id', join_class=None, uses_join_table=None, multivalued=False)
    stressor: Mapped[List["StressorChemical"]] = relationship(foreign_keys="[StressorChemical.ExposureEvent_id]")
    
    
    vehicle_rel: Mapped[List["ExposureEventVehicle"]] = relationship()
    vehicle: AssociationProxy[List[str]] = association_proxy("vehicle_rel", "vehicle",
                                  creator=lambda x_: ExposureEventVehicle(vehicle=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ExposureEvent', source_slot='phenotype_observation', mapping_type=None, target_class='PhenotypeObservationSet', target_slot='ExposureEvent_id', join_class=None, uses_join_table=None, multivalued=False)
    phenotype_observation: Mapped[List["PhenotypeObservationSet"]] = relationship(foreign_keys="[PhenotypeObservationSet.ExposureEvent_id]")
    

    def __repr__(self):
        return f"ExposureEvent(route={self.route},exposure_start_stage={self.exposure_start_stage},exposure_end_stage={self.exposure_end_stage},comment={self.comment},exposure_type={self.exposure_type},additional_exposure_condition={self.additional_exposure_condition},id={self.id},Experiment_id={self.Experiment_id},regimen_id={self.regimen_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Regimen(ZappEntity):
    """
    The schedule and pattern of an exposure event.
    """
    __tablename__ = 'Regimen'

    exposure_regimen_type: Mapped[Optional[str]] = mapped_column(Enum('continuous', 'repeated', name='ExposureRegimenTypeEnum'))
    number_of_individual_exposure: Mapped[Optional[int]] = mapped_column(Integer())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    interval_between_individual_exposures_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('QuantityValue.id'))
    interval_between_individual_exposures: Mapped[Optional["QuantityValue"]] = relationship(foreign_keys=[interval_between_individual_exposures_id])
    total_exposure_duration_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('QuantityValue.id'))
    total_exposure_duration: Mapped[Optional["QuantityValue"]] = relationship(foreign_keys=[total_exposure_duration_id])
    individual_exposure_duration_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('QuantityValue.id'))
    individual_exposure_duration: Mapped[Optional["QuantityValue"]] = relationship(foreign_keys=[individual_exposure_duration_id])
    

    def __repr__(self):
        return f"Regimen(exposure_regimen_type={self.exposure_regimen_type},number_of_individual_exposure={self.number_of_individual_exposure},id={self.id},interval_between_individual_exposures_id={self.interval_between_individual_exposures_id},total_exposure_duration_id={self.total_exposure_duration_id},individual_exposure_duration_id={self.individual_exposure_duration_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class StressorChemical(ZappEntity):
    """
    A chemical, that elicit a response (a phenotype) in a subject when when encountered through exposure.
    """
    __tablename__ = 'StressorChemical'

    manufacturer: Mapped[Optional[str]] = mapped_column(Text())
    comment: Mapped[Optional[str]] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    ExposureEvent_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('ExposureEvent.id'))
    chemical_id_uri: Mapped[int] = mapped_column(Integer(), ForeignKey('ChemicalEntity.uri'))
    chemical_id: Mapped[Optional["ChemicalEntity"]] = relationship(foreign_keys=[chemical_id_uri])
    concentration_id: Mapped[int] = mapped_column(Integer(), ForeignKey('QuantityValue.id'))
    concentration: Mapped[Optional["QuantityValue"]] = relationship(foreign_keys=[concentration_id])
    

    def __repr__(self):
        return f"StressorChemical(manufacturer={self.manufacturer},comment={self.comment},id={self.id},ExposureEvent_id={self.ExposureEvent_id},chemical_id_uri={self.chemical_id_uri},concentration_id={self.concentration_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Image(ZappEntity):
    """
    An image associated with a phenotype observation.
    """
    __tablename__ = 'Image'

    magnification: Mapped[Optional[str]] = mapped_column(Text())
    resolution: Mapped[Optional[str]] = mapped_column(Text())
    scale_bar: Mapped[Optional[str]] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    PhenotypeObservationSet_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('PhenotypeObservationSet.id'))
    

    def __repr__(self):
        return f"Image(magnification={self.magnification},resolution={self.resolution},scale_bar={self.scale_bar},id={self.id},PhenotypeObservationSet_id={self.PhenotypeObservationSet_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ControlImage(ZappEntity):
    """
    An image associated with a control, taken at the same developmental stage as the corresponding phenotype observation.
    """
    __tablename__ = 'ControlImage'

    phenotype_id: Mapped[Optional[str]] = mapped_column(Text())
    magnification: Mapped[Optional[str]] = mapped_column(Text())
    resolution: Mapped[Optional[str]] = mapped_column(Text())
    scale_bar: Mapped[Optional[str]] = mapped_column(Text())
    phenotype_comments: Mapped[Optional[str]] = mapped_column(Text())
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    PhenotypeObservationSet_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('PhenotypeObservationSet.id'))
    Control_id: Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey('Control.id'))
    

    def __repr__(self):
        return f"ControlImage(phenotype_id={self.phenotype_id},magnification={self.magnification},resolution={self.resolution},scale_bar={self.scale_bar},phenotype_comments={self.phenotype_comments},id={self.id},PhenotypeObservationSet_id={self.PhenotypeObservationSet_id},Control_id={self.Control_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ChemicalEntity(OntologyEntity):
    """
    The chemical used as the stressor chemical in an exposure event.
    """
    __tablename__ = 'ChemicalEntity'

    uri: Mapped[str] = mapped_column(Text(), primary_key=True)
    chebi_id: Mapped[str] = mapped_column(Text(), primary_key=True)
    cas_id: Mapped[str] = mapped_column(Text(), primary_key=True)
    chemical_name: Mapped[str] = mapped_column(Text(), primary_key=True)
    
    
    synonym_rel: Mapped[List["ChemicalEntitySynonym"]] = relationship()
    synonym: AssociationProxy[List[str]] = association_proxy("synonym_rel", "synonym",
                                  creator=lambda x_: ChemicalEntitySynonym(synonym=x_))
    

    def __repr__(self):
        return f"ChemicalEntity(uri={self.uri},chebi_id={self.chebi_id},cas_id={self.cas_id},chemical_name={self.chemical_name},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PhenotypeTerm(OntologyEntity):
    """
    A phenotype ontology term from the Zebrafish Phenotype ontology (ZP).
    """
    __tablename__ = 'PhenotypeTerm'

    term_uri: Mapped[str] = mapped_column(Text(), primary_key=True)
    term_label: Mapped[str] = mapped_column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"PhenotypeTerm(term_uri={self.term_uri},term_label={self.term_label},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Fish(ZfinEntity):
    """
    Zebrafish used as subject in the study.
    """
    __tablename__ = 'Fish'

    name: Mapped[str] = mapped_column(Text())
    zfin_id: Mapped[str] = mapped_column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Fish(name={self.name},zfin_id={self.zfin_id},)"


    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


