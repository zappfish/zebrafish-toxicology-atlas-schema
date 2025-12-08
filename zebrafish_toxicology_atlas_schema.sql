-- # Abstract Class: Entity Description: The base class for all entities in the Zebrafish Toxicology Atlas Schema.
--     * Slot: uuid Description: UUID identifier.
-- # Class: Study Description: A toxicological investigation, including the experimental conditions and phenotypic outcomes, with information provenance.
--     * Slot: publication Description: The publication identifier (e.g., PMID, DOI) for the study or "not published" if the study is unpublished.
--     * Slot: lab Description: ZFIN lab identifier of the laboratory that produced the study data.
--     * Slot: uuid Description: UUID identifier.
-- # Class: Experiment Description: A group of observations (phenotypic outcomes and their control) that are linked by a common exposure event and subject, and that are part of a study.
--     * Slot: standard_rearing_condition Description: An indication of whether the subject was maintained under standard conditions, which are the established, consistent environmental and husbandry parameters (such as temperature, lighting, diet, and housing) designed to minimize variability and ensure reproducibility in experiments.
--     * Slot: rearing_condition_comment Description: Comments on rearing conditions, for example, about how conditions deviated from standard parameters.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: Study_uuid Description: Autocreated FK slot
--     * Slot: fish_uuid Description: The fish subject of the experiment.
-- # Class: PhenotypeObservationSet Description: An observation set containing control and phenotypic outcome resulting from an exposure event.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: ExposureEvent_uuid Description: Autocreated FK slot
-- # Class: Phenotype Description: Any measurable or visible trait change in the subject as a result of exposure.
--     * Slot: stage Description: The developmental stage of fish when the phenotype was observed.
--     * Slot: severity Description: The intensity of the observed phenotype.
--     * Slot: phenotype_term_id Description: The phenotype ontology term identifier.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: PhenotypeObservationSet_uuid Description: Autocreated FK slot
--     * Slot: prevalence_id Description: The percentage of subject exhibiting this phenotype.
-- # Class: Control Description: A subject serves as a reference for assessing phenotypic outcome in the phenotype observation set.
--     * Slot: control_type Description: Type of control (e.g., wildtype vs mutant, treated vs untreated).
--     * Slot: vehicle_if_treated Description: The vehicle used in a control.
--     * Slot: comment Description: Additional comments.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: Experiment_uuid Description: Autocreated FK slot
-- # Class: ExposureEvent Description: An occurrence in a study where a subject is exposed to a stressor under defined conditions.
--     * Slot: route Description: The route of exposure.
--     * Slot: exposure_start_stage Description: The developmental stage of fish when exposure started.
--     * Slot: exposure_end_stage Description: The developmental stage of fish when exposure ended.
--     * Slot: comment Description: Additional comments.
--     * Slot: exposure_type Description: An instance of exposure specifying the type of stressor a subject was exposed to.
--     * Slot: additional_exposure_condition Description: Additional information about the conditions under which exposure event occurred.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: Experiment_uuid Description: Autocreated FK slot
--     * Slot: regimen_uuid Description: The regimen for the exposure.
-- # Class: Regimen Description: The schedule and pattern of an exposure event.
--     * Slot: exposure_regimen_type Description: The type of exposure regimen (e.g., continuous or repeated).
--     * Slot: number_of_individual_exposure Description: Total number of individual exposures.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: interval_between_individual_exposures_id Description: Interval between individual exposures.
--     * Slot: total_exposure_duration_id Description: Time between first and last individual exposure.
--     * Slot: individual_exposure_duration_id Description: Individual exposure duration.
-- # Class: StressorChemical Description: A chemical, that elicit a response (a phenotype) in a subject when when encountered through exposure.
--     * Slot: manufacturer Description: The manufacturer of the chemical.
--     * Slot: comment Description: Additional comments.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: ExposureEvent_uuid Description: Autocreated FK slot
--     * Slot: chemical_id_uuid Description: Chemical identifier (CHEBI, CAS, or UUID).
--     * Slot: concentration_id Description: The dose or concentration of the chemical to which the subject was exposed to.
-- # Class: ChemicalEntity Description: The chemical used as the stressor chemical in an exposure event.
--     * Slot: chebi_id Description: CHEBI identifier for the chemical.
--     * Slot: cas_id Description: CAS identifier for the chemical.
--     * Slot: chemical_name Description: Name of the chemical.
--     * Slot: uuid Description: UUID identifier.
-- # Class: Image Description: An image associated with a phenotype observation.
--     * Slot: magnification Description: The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.
--     * Slot: resolution Description: The level of detail in the image.
--     * Slot: scale_bar Description: Scale bar information, including the physical length it represents and the unit of measurement.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: PhenotypeObservationSet_uuid Description: Autocreated FK slot
-- # Class: ControlImage Description: An image associated with a control, taken at the same developmental stage as the corresponding phenotype observation.
--     * Slot: phenotype_id Description: Foreign key reference to the PhenotypeObservationSet uuid (for database representation).
--     * Slot: magnification Description: The factor by which a microscope enlarges the apparent size of a subject compared to its actual size.
--     * Slot: resolution Description: The level of detail in the image.
--     * Slot: scale_bar Description: Scale bar information, including the physical length it represents and the unit of measurement.
--     * Slot: phenotype_comments Description: Comments about the phenotype in the control image.
--     * Slot: uuid Description: UUID identifier.
--     * Slot: PhenotypeObservationSet_uuid Description: Autocreated FK slot
--     * Slot: Control_uuid Description: Autocreated FK slot
-- # Class: Fish Description: Zebrafish used as subject in the study.
--     * Slot: id
--     * Slot: name Description: Name or label of an entity.
--     * Slot: uuid Description: UUID identifier.
-- # Class: QuantityValue Description: A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
--     * Slot: id
--     * Slot: unit Description: The unit of the quantity value.
--     * Slot: numeric_value Description: The numeric value of the quantity value.
-- # Class: Study_annotator
--     * Slot: Study_uuid Description: Autocreated FK slot
--     * Slot: annotator Description: ORCID identifier of the indidvidual submitting the study data.
-- # Class: ExposureEvent_vehicle
--     * Slot: ExposureEvent_uuid Description: Autocreated FK slot
--     * Slot: vehicle Description: The substance or medium used to deliver a stressor.
-- # Class: ChemicalEntity_synonym
--     * Slot: ChemicalEntity_uuid Description: Autocreated FK slot
--     * Slot: synonym Description: Other names for the chemical.

CREATE TABLE "Entity" (
	uuid TEXT NOT NULL,
	PRIMARY KEY (uuid)
);CREATE INDEX "ix_Entity_uuid" ON "Entity" (uuid);
CREATE TABLE "Study" (
	publication TEXT,
	lab TEXT,
	uuid TEXT NOT NULL,
	PRIMARY KEY (uuid)
);CREATE INDEX "ix_Study_uuid" ON "Study" (uuid);
CREATE TABLE "ChemicalEntity" (
	chebi_id TEXT,
	cas_id TEXT,
	chemical_name TEXT,
	uuid TEXT NOT NULL,
	PRIMARY KEY (uuid)
);CREATE INDEX "ix_ChemicalEntity_uuid" ON "ChemicalEntity" (uuid);
CREATE TABLE "Fish" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	uuid TEXT NOT NULL,
	PRIMARY KEY (uuid)
);CREATE INDEX "ix_Fish_uuid" ON "Fish" (uuid);
CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL,
	unit TEXT,
	numeric_value TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_QuantityValue_id" ON "QuantityValue" (id);
CREATE TABLE "Experiment" (
	standard_rearing_condition BOOLEAN,
	rearing_condition_comment TEXT,
	uuid TEXT NOT NULL,
	"Study_uuid" TEXT,
	fish_uuid TEXT,
	PRIMARY KEY (uuid),
	FOREIGN KEY("Study_uuid") REFERENCES "Study" (uuid),
	FOREIGN KEY(fish_uuid) REFERENCES "Fish" (uuid)
);CREATE INDEX "ix_Experiment_uuid" ON "Experiment" (uuid);
CREATE TABLE "Regimen" (
	exposure_regimen_type VARCHAR(10),
	number_of_individual_exposure INTEGER,
	uuid TEXT NOT NULL,
	interval_between_individual_exposures_id INTEGER,
	total_exposure_duration_id INTEGER,
	individual_exposure_duration_id INTEGER,
	PRIMARY KEY (uuid),
	FOREIGN KEY(interval_between_individual_exposures_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_exposure_duration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(individual_exposure_duration_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Regimen_uuid" ON "Regimen" (uuid);
CREATE TABLE "Study_annotator" (
	"Study_uuid" TEXT,
	annotator TEXT,
	PRIMARY KEY ("Study_uuid", annotator),
	FOREIGN KEY("Study_uuid") REFERENCES "Study" (uuid)
);CREATE INDEX "ix_Study_annotator_Study_uuid" ON "Study_annotator" ("Study_uuid");CREATE INDEX "ix_Study_annotator_annotator" ON "Study_annotator" (annotator);
CREATE TABLE "ChemicalEntity_synonym" (
	"ChemicalEntity_uuid" TEXT,
	synonym TEXT,
	PRIMARY KEY ("ChemicalEntity_uuid", synonym),
	FOREIGN KEY("ChemicalEntity_uuid") REFERENCES "ChemicalEntity" (uuid)
);CREATE INDEX "ix_ChemicalEntity_synonym_synonym" ON "ChemicalEntity_synonym" (synonym);CREATE INDEX "ix_ChemicalEntity_synonym_ChemicalEntity_uuid" ON "ChemicalEntity_synonym" ("ChemicalEntity_uuid");
CREATE TABLE "Control" (
	control_type TEXT,
	vehicle_if_treated VARCHAR(7),
	comment TEXT,
	uuid TEXT NOT NULL,
	"Experiment_uuid" TEXT,
	PRIMARY KEY (uuid),
	FOREIGN KEY("Experiment_uuid") REFERENCES "Experiment" (uuid)
);CREATE INDEX "ix_Control_uuid" ON "Control" (uuid);
CREATE TABLE "ExposureEvent" (
	route VARCHAR,
	exposure_start_stage TEXT,
	exposure_end_stage TEXT,
	comment TEXT,
	exposure_type VARCHAR,
	additional_exposure_condition TEXT,
	uuid TEXT NOT NULL,
	"Experiment_uuid" TEXT,
	regimen_uuid TEXT,
	PRIMARY KEY (uuid),
	FOREIGN KEY("Experiment_uuid") REFERENCES "Experiment" (uuid),
	FOREIGN KEY(regimen_uuid) REFERENCES "Regimen" (uuid)
);CREATE INDEX "ix_ExposureEvent_uuid" ON "ExposureEvent" (uuid);
CREATE TABLE "PhenotypeObservationSet" (
	uuid TEXT NOT NULL,
	"ExposureEvent_uuid" TEXT,
	PRIMARY KEY (uuid),
	FOREIGN KEY("ExposureEvent_uuid") REFERENCES "ExposureEvent" (uuid)
);CREATE INDEX "ix_PhenotypeObservationSet_uuid" ON "PhenotypeObservationSet" (uuid);
CREATE TABLE "StressorChemical" (
	manufacturer TEXT,
	comment TEXT,
	uuid TEXT NOT NULL,
	"ExposureEvent_uuid" TEXT,
	chemical_id_uuid TEXT NOT NULL,
	concentration_id INTEGER NOT NULL,
	PRIMARY KEY (uuid),
	FOREIGN KEY("ExposureEvent_uuid") REFERENCES "ExposureEvent" (uuid),
	FOREIGN KEY(chemical_id_uuid) REFERENCES "ChemicalEntity" (uuid),
	FOREIGN KEY(concentration_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_StressorChemical_uuid" ON "StressorChemical" (uuid);
CREATE TABLE "ExposureEvent_vehicle" (
	"ExposureEvent_uuid" TEXT,
	vehicle VARCHAR(7),
	PRIMARY KEY ("ExposureEvent_uuid", vehicle),
	FOREIGN KEY("ExposureEvent_uuid") REFERENCES "ExposureEvent" (uuid)
);CREATE INDEX "ix_ExposureEvent_vehicle_ExposureEvent_uuid" ON "ExposureEvent_vehicle" ("ExposureEvent_uuid");CREATE INDEX "ix_ExposureEvent_vehicle_vehicle" ON "ExposureEvent_vehicle" (vehicle);
CREATE TABLE "Phenotype" (
	stage TEXT,
	severity VARCHAR(8),
	phenotype_term_id TEXT,
	uuid TEXT NOT NULL,
	"PhenotypeObservationSet_uuid" TEXT,
	prevalence_id INTEGER,
	PRIMARY KEY (uuid),
	FOREIGN KEY("PhenotypeObservationSet_uuid") REFERENCES "PhenotypeObservationSet" (uuid),
	FOREIGN KEY(prevalence_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Phenotype_uuid" ON "Phenotype" (uuid);
CREATE TABLE "Image" (
	magnification TEXT,
	resolution TEXT,
	scale_bar TEXT,
	uuid TEXT NOT NULL,
	"PhenotypeObservationSet_uuid" TEXT,
	PRIMARY KEY (uuid),
	FOREIGN KEY("PhenotypeObservationSet_uuid") REFERENCES "PhenotypeObservationSet" (uuid)
);CREATE INDEX "ix_Image_uuid" ON "Image" (uuid);
CREATE TABLE "ControlImage" (
	phenotype_id TEXT,
	magnification TEXT,
	resolution TEXT,
	scale_bar TEXT,
	phenotype_comments TEXT,
	uuid TEXT NOT NULL,
	"PhenotypeObservationSet_uuid" TEXT,
	"Control_uuid" TEXT,
	PRIMARY KEY (uuid),
	FOREIGN KEY("PhenotypeObservationSet_uuid") REFERENCES "PhenotypeObservationSet" (uuid),
	FOREIGN KEY("Control_uuid") REFERENCES "Control" (uuid)
);CREATE INDEX "ix_ControlImage_uuid" ON "ControlImage" (uuid);

