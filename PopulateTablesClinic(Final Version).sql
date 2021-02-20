/*
This document is used for populating data in 17 tables created for this project:
Employee, Specialist, AlmaMaters, Skill, JobPositionHistory, Credential, Patient, MedicalHistory, Complaint, Appointment, InsuranceClaim,
Vendor, Purchase, OrderItem, Inventory, Insurance, MedicalUse
*/

-- Populate Employee

INSERT INTO EMPLOYEE (EmployeeID, EmployeeName, EmployeeAddress, EmployeePhone, EmployeeEmail, JobTitle, EmployeeBirthDate, JobType)
VALUES
('E1001','Juan Carlos','315 St Germain Ave Toronto ON M5M 1W4', '(416) 322-7518','juan@gmail.com', 'Pharmacist', '1971-08-05', 'Non Medical'),
('E1002','Mike Jones','234 Willow Ave Toronto ON M4E 3K7','(416) 699-8444','mike@gmail.com','Surgeon','1960-02-03','Medical'),
('E1003','Chris Williams', '500 Kingston Rd Toronto ON M4L 1V3','(416) 699-8071','chris@gmail.com','Director Physician','1970-06-23','Medical'),
('E1004','Mark Brown','26 Goodwood Park Cres East York ON M4C 2G5','(416) 304-0129','mark@gmail.com','Medical Admission Clerk','1988-04-02','Non Medical'),
('E1005','Maria Gacia','48 St Clair Ave W Toronto ON M4V 2Z2','(416) 698-9608','maria@gmail.com','Human Resources Manager','1979-05-13','Non Medical'),
('E1006','James Potter','8 Adelaide Street West Toronto ON M5H 0A9','(416) 698-9609','jamesp@gmail.com','Surgeon','1968-01-01','Medical'),
('E1007','Lily Potter','55 Bloor St W Toronto ON M4W 1A5','(416) 698-9610','lilypt@gmail.com','Surgeon','1967-05-14','Medical'),
('E1008','Severus Snape','60 Yorkville Ave Toronto ON M4W 0A4','(416) 698-7711','snapesv@gmail.com','physician','1980-07-02','Medical'),
('E1009','Arya Stark11','Polson Street Toronto ON M5A 1A4','(416) 698-5612','aryasta@gmail.com','accountant','1990-11-12','Non Medical'),
('E1010','Cersei Lannister','225 Richmond St West Toronto ON M5V 1W2','(416) 698-8813','cerseila@gmail.com','Medical Admission Clerk','1992-04-06','Non Medical')
;
-- Populate Specialist
INSERT INTO Specialist(EmployeeID, Specialty)
VALUES
('E1002','Dermatology'),
('E1002','Urology'),
('E1002','Surgery'),
('E1003','Cardiology'),
('E1003','Respirology'),
('E1003','X-Ray'),
('E1006','Pediatrics'),
('E1006','Anesthesiology'),
('E1006','Emergency Medicine'), 
('E1007','Pathology'), 
('E1007','Urology'),
('E1007','Dermatology'),
('E1008','Allergy and Immunology'), 
('E1008','Respirology'),
('E1008','Cardiology');


-- Populate Alma Maters
INSERT INTO AlmaMaters (EmployeeID,SchoolName)
VALUES
('E1002','University of Toronto'),
('E1003','McGill University'),
('E1003','University of California, Irvine School of Medicine'),
('E1003','McMaster University'), 
('E1006','University of Alberta Faculty of Medicine and Dentistry'),
('E1006','Dalhousie University Faculty of Medicine'),
('E1007','McMaster University'), 
('E1008','University of Toronto');

-- Populate Skill
INSERT INTO Skill (EmployeeID,Skill)
VALUES
('E1001','Analytical Skills'),
('E1001','Problem-Solving Skills'),
('E1001','Observation Skills'),
('E1002','Teamwork Skills'),
('E1002','Physical Skills'),
('E1003','Decision-Making Skills'),
('E1003','Training Skills'),
('E1004','Communication and Social Skills'),
('E1004','Strong Numerical Skills'),
('E1005','Empathetic Skills'),
('E1005','Developmental Skills'),
('E1006','Communication and Social Skills'),
('E1006','Teamwork Skills'),
('E1006','Problem Solving Skills'),
('E1007','Leadership Skills'),
('E1007','Empathetic Skills'),
('E1008','Decision-Making Skills'),
('E1008','Leadership Skills'),
('E1008','Problem-Solving Skills'),
('E1009','Leadership Skills'),
('E1010','Empathetic Skills'),
('E1009','Training Skills'),
('E1010','Teamwork Skills');

--Populate Job Position History
INSERT INTO JobPositionHistory(EmployeeID,JobTitle,StartingDate,EndingDate)
VALUES
('E1001','Pharmacist','2000-09-06',NULL),
('E1002','Assistant Surgeon','1994-02-14','1999-01-31'),
('E1002','Surgeon','1990-02-01',NULL),
('E1003','Physician','1986-05-02','1989-09-03'),
('E1003','Assistant Director Physician','1989-09-04','1992-01-12'),
('E1003','Director Physician','1992-01-13',NULL),
('E1004','Medical Admission Clerk','2018-12-20',NULL),
('E1005','Human Resources Manager','1992-06-23',NULL),
('E1006','Surgeon','2001-09-02',NULL),
('E1007','Surgeon','2002-09-02',NULL),
('E1008','Physician','1992-08-15','1998-6-12'),
('E1008','Assistant Director Physician','1998-06-13',NULL),
('E1019','Accountant','2011-09-10','2016-09-11'),
('E1009','Senior Accountant','2016-09-12',NULL),
('E1010','IT Personnel','2012-09-15',NULL);

--Populate Credential
INSERT INTO Credential (EmployeeID,Credential)
VALUES
('E1001','BCACP'),
('E1001','BCPP'),
('E1002','MD'),
('E1002','MBBS'),
('E1003','MD'),
('E1003','PA'),
('E1003','DO'),
('E1004','CCAP'),
('E1005','CPHR'),
('E1006','MD'),
('E1007','MD'),
('E1008','MD'),
('E1009','BS'),
('E1010','BA');

-- Populate Patient

INSERT INTO Patient (PatientID, InsurancePolicy, PatientName, PatientAddress, PatientPhone, PatientEmail, PatientBirthDate, PatientGender, OHIP,NextofKin, FamilyDoctorName, FamilyDoctorContactInfo)
VALUES
('P2001','IN1011','John Smith','300 St Germain Ave Toronto ON M5M 1W4','(416) 222-7518','john@gmail.com','1998-08-05','M','3000','Dan Smith','Sarah','NULL'),
('P2002','IN1012','Ashley Anne','200 Willow Ave Toronto ON M4E 3K7','(416) 222-8444','ashley@gmail.com','1970-02-03','F','3001','Amanda Anne','Mike','(416) 200-8445'),
('P2003','IN1013','Jim Mcdoanld','100 Kingston Rd Toronto ON M4L 1V3','(416) 333-8071','jim@gmail.com','1950-06-23','M','3002','Sally Mcdoanld','Johnny','(416) 912-8099'),
('P2004','IN1014','Henry Shien','10 Goodwood Park Cres East York ON M4C 2G5','(416) 333-0129','henry@gmail.com','1986-04-02','M','3003','Jill Shien','Sam','NULL'),
('P2005','IN1015','Jimmy Campbell','90 St Clair Ave W Toronto ON M4V 2Z2','(416) 444-9608','jimmy@gmail.com','1989-05-13','M','3004','Ally Campbell','Tori','(416) 414-9001'),
('P2006','IN1016','Carmen Wong','70 Adelaide Street West Toronto ON M5H 0A9','(416) 444-9609','carmen@gmail.com','1990-01-01','F','3005','Joseph Wong','Daniel','(416) 494-9111'),
('P2007','IN1017','Sally Anderson','35 Bloor St W Toronto ON M4W 1A5','(416) 555-9610','sally@gmail.com','1981-05-14','F','3006','Gill Anderson','John','(416) 511-9333'),
('P2008','IN1018','Lee Chong','30 Yorkville Ave Toronto ON M4W 0A4','(416) 555-7711','lee@gmail.com','1969-07-02','M','3007','Jo Chong','Amanda','(416) 505-9633'),
('P2009','IN1019','Micheal Miller','20 Polson Street Toronto ON M5A 1A4','(416) 555-5612','micheal@gmail.com','1992-11-12','M','3008','Mike Miller','Anthony','(416) 565-5666'),
('P2010','IN1020','Jack Broen','10 Richmond St West Toronto ON M5V 1W2','(416) 666-8813','jack@gmail.com','1994-04-06','M','3009','Henry Broen','Robby','(416) 636-8822')
;

--Populate Medical History
INSERT INTO MedicalHistory(PatientID,MedicalDetails)
VALUES
('P2001','hypertension'),
('P2001','hyperlipidemia'),
('P2001','diabetes'),
('P2002',NULL),
('P2003','back pain'),
('P2003','obesity'),
('P2004','paint in joints'),
('P2005','asthma'),
('P2005','heart disease'),
('P2006',NULL),
('P2007','anxiety'), 
('P2008','tree nut allergy'),
('P2009','asthma'), 
('P2010',NULL);

--Populate Complaint
INSERT INTO Complaint(ComplaintID,ClaimID,StartDate,EndDate,Complaint)
VALUES
('CT1111','2100','2011-09-06','2020-09-07','mole on scalp'),
('CT1112','2101','2020-08-07','2020-09-07','trouble breathing and chest pain'),
('CT1113','2102','2018-09-01','2020-09-08','needs annual checkup'),
('CT1114','2103','2017-09-09','2020-09-09','swollen forearm'),
('CT1115','2104','2018-09-10','2020-09-10','annual checkup'),
('CT1116','2105','2015-09-11','2020-09-11','uncontrollable bleeding'),
('CT1117','2106','2018-05-12','2020-09-20','conegenital heart failure, heart issues, chest pain, trouble breathing'),
('CT1118','2107','2017-03-13','2020-09-13','itchy and red skin'),
('CT1119','2108','2019-09-14','2020-09-14','bladder issues, infections'),
('CT1121','2110','2020-06-09','2020-09-16','senstive to light headache has been consistantly hurting'),
('CT1122','2111','2020-08-01','2020-09-17','throwing up and unable to keep solid food down');


--Populate Appointment
INSERT INTO Appointment (AppointID,ComplaintID,PatientID,EmployeeID,ScheduleDate,ScheduleTime,ActualDate,ActualTime,TreatmentDetails,MedicalEmployeeNotes)
VALUES
('A01','CT1111','P2001','E1003','2020-09-06','08:30','2020-09-06','08:30','scalp biopsy to check for irregular tissue patterns','Record the complaint'),
('A02','CT1112','P2001','E1007','2020-09-07','09:30','2020-09-07','09:30','triple coronary artery bypass patient had heart attack','Discuss options for fixing the problem'),
('A03','CT1113','P2002','E1003','2020-09-08','10:30','2020-09-08','10:30','simple prostate exam done annually','Accept ownership of the problem'),
('A04','CT1114','P2002','E1002','2020-09-09','11:30','2020-09-09','11:30','xray on right forarm to check for broken humerus','Dealing with complaints'),
('A05','CT1115','P2003','E1003','2020-09-10','12:30','2020-09-10','12:30','patient inneed of booster shots','Record the complaint'),
('A06','CT1116','P2004','E1006','2020-09-11','13:30','2020-09-11','13:30','deep wound requiring 4 sutures to close','Provide a free product'),
('A07','CT1117','P2005','E1007','2020-09-12','14:30','2020-09-12','14:30','schdeuled procedure as per patient treatment plan','Discount a future service'),
('A08','CT1118','P2006','E1008','2020-09-13','15:30','2020-09-13','15:30','to check for allergy to tree nuts and all other nuts','Resolving the problem'),
('A09','CT1119','P2007','E1002','2020-09-14','16:30','2020-09-14','16:30','drain build up of bladder fluids','Discuss options for fixing the problem'),
('A10','CT1120','P2008','E1006','2020-09-15','17:30',NULL,NULL,NULL,'patient cancelled appointment'),
('A11','CT1121','P2009','E1007','2020-09-16','18:30','2020-09-16','18:30','migrains adminstred 150g advil','Record the complaint'),
('A12','CT1122','P2010','E1003','2020-09-17','19:30','2020-09-17','19:30','needs to eat fibre','Discuss options for fixing the problem'),
('A13','CT1117','P2005','E1007','2020-09-20','14:00','2020-09-20','14:00','delay the procedure that was planned before','Need to check your complaint next month');

-- Populate Insurance Claim
INSERT INTO InsuranceClaim(ClaimID, InsurancePolicyNumber, ComplaintID, ProcedureName, InsuranceCode,InsurancePartner, SubmissionDate, SubmissionPayment, CoveredPayment)
VALUES

('2100','IN1011','CT1111','skin biopsy','1001000011','great west life','2020-09-06','1000','949'),
('2101','IN1012','CT1112','coronary atery bypass graft surgery','1001000012','sun life','2020-09-07','1905','832'),
('2102','IN1013','CT1113','prostate exam','1001000013','manulife','2020-09-08','1020','583'),
('2103','IN1014','CT1114','humerus xray','1001000014','desjardins','2020-09-09','1004','937'),
('2104','IN1015','CT1115','immunization','1001000015','medavie','2020-09-10','1989','729'),
('2105','IN1016','CT1116','sutures','1001000016','ssq','2020-09-11','1039','425'),
('2106','IN1017','CT1117','Pre-surgery check','1001000017','blue cross','2020-09-12','1037','645'),
('2107','IN1018','CT1118','allergy test','1001000018','empire life','2020-09-13','1053','264'),
('2108','IN1019','CT1119','urethral catheterization','1001000019','green shield','2020-09-14','1943','735'),
('2109','IN1020','CT1120','ankle xray','1001000020','equitable life','2020-09-15','1832','842'),
('2110','IN1011','CT1121','headache','1001000021','great west life','2020-09-16','1234','800'),
('2111','IN1012','CT1122','stomach ache','1001000022','sun life','2020-09-17','500','350'),
('2112','IN1017','CT1117','Heart Value Surgery','1001000017','blue cross','2020-09-20','2000','400')
;


-- Populate Vendor
INSERT INTO Vendor (VendorID, VendorName, VendorAddress, VendorPhone, VendorEmail)
VALUES
('3100','CCC Medical','711 Nulla St Mankato Mississippi','(850) 676-5117','ccc@gmail.com'),
('3101','CrossPoint','3727 Ullamcorper. Street Roseville','(490) 936-4694','CP@gmail.com'),
('3102','Phillips','4366 Lacinia Avenue Idaho Falls Ohio','(176) 805-4108','GH@gmail.com'),
('3103','Gold Medical','4407 Et Rd Santa Monica FL','(516) 745-4496','GoldMedic@gmail.com'),
('3104','Nightwatch','859 Sit Rd Azusa New York 39531','(715) 912-6931','NW@gmail.com'),
('3105','Medi-Cab','103 Integer Rd Corona New Mexico','(750) 558-3965','meci@gmail.com'),
('3106','Code Right','1670 Neque. St Centennial Delaware','(985) 834-8285','CoRight@gmail.com'),
('3107','Castle Health','8679 Sodales Av Tamuning','(357) 616-5411','CHTH@gmail.com'),
('3108','Priority Medical','1599 Curabitur Rd Bandera South Dakota','(414) 876-0865','Peod@gmail.com'),
('3109','VulcanMed','9940 Tortor Street Santa Rosa','(304) 506-6314','VulcanMed@gmail.com');


-- Populate Purchase
INSERT INTO Purchase (PurchaseID, PurchaseDate)
VALUES
('1234', '2020-09-09'),
('1235', '2020-09-11'),
('1236', '2020-09-13'),
('1237', '2020-09-14'),
('1238', '2020-09-17');

--Populate OrderItem
INSERT INTO OrderItem(PurchaseID, VendorID, MedicalID, OrderQuantity)
VALUES
('1234','3105','MC2231','21'),
('1235','3103','MU2225','21'),
('1236','3107','MC2333','37'),
('1236','3102','MU2224','28'),
('1237','3106','MC2232','23'),
('1238','3105','MC2231','21');

--Populate Inventory
INSERT INTO Inventory (MedicalID, VendorID, MedicalName, MedicationType, MedicalQuantity, MinimumLevel)
VALUES
('MU2222','3100','Naproxen', 'Medical Medication','50','30'),
('MU2223','3101','Lyrica', 'Medical Medication','50','30'),
('MU2224','3102','Januvia', 'Medical Medication','50','30'),
('MU2225','3103','Caphalexin', 'Medical Medication','50','30'),
('MU2226','3104','Ibuprofen', 'Medical Medication','50','30'),
('MC2231','3105','Medical Mask', 'Medical Consumable','50','30'),
('MC2232','3106','Medical Glove', 'Medical Consumable','50','30'),
('MC2233','3107','Surgical Clips', 'Medical Consumable','50','30'),
('MC2234','3108','Surgical Thread', 'Medical Consumable','50','30'),
('MC2235','3109','Syringes for injections', 'Medical Consumable','50','30');

INSERT INTO MedicalUse (AppointID, ComplaintID, MedicalID, QuantityUsed, AppointDate)
VALUES
('A01', 'CT1111','MU2224','6','2020-09-06'),
('A01', 'CT1111','MC2231','5','2020-09-06'),
('A01', 'CT1111','MU2225','6','2020-09-06'),
('A02', 'CT1112','MU2226','3','2020-09-07'),
('A02', 'CT1112','MC2233','10','2020-09-07'),
('A03', 'CT1113','MU2225','6','2020-09-08'),
('A04', 'CT1114','MC2231','16','2020-09-09'),
('A04', 'CT1114','MC2233','9','2020-09-09'),
('A04', 'CT1114','MU2226','8','2020-09-09'),
('A05', 'CT1115','MU2226','4','2020-09-10'),
('A06', 'CT1116','MU2225','9','2020-09-11'),
('A07', 'CT1117','MC2232','13','2020-09-12'),
('A07', 'CT1117','MU2224','10','2020-09-12'),
('A08', 'CT1118','MC2233','18','2020-09-13'),
('A08', 'CT1118','MU2224','12','2020-09-13'),
('A09', 'CT1119','MU2225','10','2020-09-14'),
('A09', 'CT1119','MU2232','10','2020-09-14'),
('A11', 'CT1121','MC2231','10','2020-09-16'),
('A12', 'CT1122','MC2231','11','2020-09-17'),
('A13', 'CT1117','MC2235','2','2020-09-20');

-- Populate Insurance
INSERT INTO INSURANCE (InsurancePolicyNumber, CompanyName, CompanyPhone, CompanyEmail, EDILink, PatientID)
VALUES
('IN1011','great west life','(416) 522-7518','gwl@gmail.com', 'GS*PO*SEND*01', 'P2001'),
('IN1012','sun life','(416) 699-8344','insurance@sunlife.com', 'GS*PO*SEND*02', 'P2002'),
('IN1013','manulife','((416) 669-8071','claim@manulife.com', 'GS*PO*SEND*03', 'P2003'),
('IN1014','desjardins','(416) 314-0129','dj.ins@desjardins.com', 'GS*PO*SEND*04', 'P2004'),
('IN1015','medavie','(416) 698-9678','cvs@gmail.com', 'GS*PO*SEND*05', 'P2005'),
('IN1016','ssq','(416) 332-7518','ccp@gmail.com', 'GS*PO*SEND*06', 'P2006'),
('IN1017','blue cross','(416) 689-8444','chw@gmail.com', 'GS*PO*SEND*07', 'P2007'),
('IN1018','empire life','(416) 699-0071','wc@gmail.com', 'GS*PO*SEND*08', 'P2008'),
('IN1019','green shield','(416) 354-0129','hgp@gmail.com', 'GS*PO*SEND*09', 'P2009'),
('IN1020','equitable life','(416) 698-9654','csc@gmail.com', 'GS*PO*SEND*10', 'P2010');







