/* 
There are 17 tables for this exercise:
Employee, Specialist, AlmaMaters, Skill, JobPositionHistory, Credential, Patient, MedicalHistory, Complaint, Appointment, InsuranceClaim,
Vendor, Purchase, OrderItem, Inventory, Insurance, MedicalUse
*/

-- Delete Employee, Specialist, AlmaMaters, Skill, JobPositionHistory, Credential, Patient, MedicalHistory, Complaint, Appointment, InsuranceClaim,Vendor, Purchase, OrderItem, Inventory, Insurance, MedicalUse tables if they already exist

DROP TABLE IF EXISTS Employee, Specialist, AlmaMaters, Skill, JobPositionHistory, Credential, Patient, MedicalHistory, Complaint, Appointment, InsuranceClaim,
Vendor, Purchase, OrderItem, Inventory, Insurance, MedicalUse;


-- Create Employee

CREATE TABLE Employee
(
  EmployeeID            varchar(5)            PRIMARY KEY,
  EmployeeName          varchar(20)       NOT NULL,
  EmployeeAddress       varchar(50)        NOT NULL,
  EmployeePhone        varchar(14)        NOT NULL,
  EmployeeEmail        varchar(30)        NOT NULL,
  JobTitle           varchar(30)         NOT NULL,
  EmployeeBirthDate     date             NOT NULL,
  JobType           varchar(25)         NOT NULL
);
-- Create Specialist

CREATE TABLE Specialist
(
  EmployeeID            varchar(5)             NOT NULL,
  Specialty            varchar(30)            NOT NULL
);
-- Create AlmaMater

CREATE TABLE AlmaMaters
(
  EmployeeID            varchar(5)             NOT NULL,
  SchoolName            varchar(100)            NOT NULL 
);
-- Create Skill

CREATE TABLE Skill
(
  EmployeeID            varchar(5)             NOT NULL,
  Skill            varchar(50)            NOT NULL
);
-- Create Credential

CREATE TABLE Credential
(
  EmployeeID            varchar(5)             NOT NULL,
  Credential            varchar(50)            NOT NULL
);
-- Create Job Position History

CREATE TABLE JobPositionHistory
(
  EmployeeID            varchar(5)             NOT NULL,
  JobTitle             varchar(30)            NOT NULL,
  StartingDate            date               NOT NULL,
  EndingDate             date
);
-- Create Job Patient

CREATE TABLE Patient
(
  PatientID            varchar(5)            PRIMARY KEY,
  InsurancePolicy     varchar(6)            NOT NUlL,  
  PatientName          varchar(20)          NOT NULL,  
  PatientAddress       varchar(50)          NOT NULL,
  PatientPhone        varchar(14)           NOT NULL,
  PatientEmail        varchar(30)           NOT NULL,
  PatientBirthDate      date                NOT NULL,
  PatientGender     VARCHAR(5)              NOT NULL,
  OHIP              INTEGER                 NOT NULL,
  NextofKin         varchar(40)             NOT NULL,
  FamilyDoctorName  varchar(20)      NOT NULL,
  FamilyDoctorContactInfo VARCHAR(20) NOT NULL
);

-- Create Appointment

CREATE TABLE Appointment 
(
  AppointID            varchar(20)            PRIMARY KEY,
  ComplaintID            varchar(6)           NOT NULL,
  PatientID            varchar(10)            NOT NULL,
  EmployeeID          varchar(20)             NOT NULL,
  ScheduleDate       date                     NOT NULL,
  ScheduleTime      time                      NOT NULL,
  ActualDate        date,
  ActualTime        time,
  TreatmentDetails           varchar(100),
  MedicalEmployeeNotes     varchar(100)               
);
-- Create MedicalHistory

CREATE TABLE MedicalHistory
(
  PatientID            varchar(10)            NOT NULL,
  MedicalDetails            varchar(100)
);
-- Create Complaint

CREATE TABLE Complaint
(
  ComplaintID            varchar(6)         PRIMARY KEY,
  ClaimID            varchar(20)            NOT NULL, 
  StartDate          date                   NOT NULL,
  EndDate            date                   NOT NULL,
  Complaint          varchar(200)           NOT NULL
);

-- Create Insurance

CREATE TABLE Insurance
(
  InsurancePolicyNumber    varchar(6)      PRIMARY KEY,
  CompanyName              varchar(30)       NOT NULL,
  CompanyPhone             varchar(20)       NOT NULL,
  CompanyEmail             varchar(30)       NOT NULL,
  EDILink                  varchar(30)       NOT NULL,
  PatientID                varchar(5)        NOT NULL
);

-- Create Insurance Claim

CREATE TABLE InsuranceClaim
(
  ClaimID                 varchar(4)           PRIMARY KEY,
  InsurancePolicyNumber   varchar(6)           NOT NULL,
  ComplaintID             varchar(6)           NOT NULL,
  ProcedureName           varchar(50)          NOT NULL,
  InsuranceCode           varchar(15)          NOT NULL,
  InsurancePartner        varchar(30)          NOT NULL,
  SubmissionDate          date                 NOT NULL,
  SubmissionPayment       VARCHAR(10)         NOT NULL,
  CoveredPayment          VARCHAR(10)         NOT NULL
);

-- Create Inventory

CREATE TABLE Inventory
(
  MedicalID                 varchar(6)            PRIMARY KEY,
  VendorID                  varchar(4)            NOT NULL,
  MedicalName               varchar(30)           NOT NULL,
  MedicationType             varchar(30)          NOT NULL,
  MedicalQuantity            INTEGER           NOT NULL,
  MinimumLevel               INTEGER           NOT NULL
);

-- Create Vendor

CREATE TABLE Vendor
(
  VendorID                 varchar(4)             PRIMARY KEY,
  VendorName               varchar(30)          NOT NULL,
  VendorAddress            varchar(50)          NOT NULL,
  VendorPhone              varchar(20)          NOT NULL,
  VendorEmail              varchar(30)           NOT NULL
);

-- Create Purchase

CREATE TABLE Purchase
(
  PurchaseID           varchar(4)            PRIMARY KEY,
  PurchaseDate         date                  NOT NULL
);

-- Create Order Item

CREATE TABLE OrderItem
(
  PurchaseID               varchar(4)            NOT NULL,
  VendorID                 varchar(4)             NOT NULL,
  MedicalID               varchar(6)          NOT NULL,
  OrderQuantity            Integer          NOT NULL
);

-- Create Medical Use

CREATE TABLE MedicalUse
(
  AppointID               varchar(3)            NOT NULL,
  ComplaintID             varchar(6)            NOT NULL,
  MedicalID               varchar(6)           NOT NULL,
  QuantityUsed            INTEGER          NOT NULL,
  AppointDate             date                 NOT NULL 
);








