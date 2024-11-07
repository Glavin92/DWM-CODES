--Doctor dimension table
CREATE TABLE Doctor (
 DoctorID INT PRIMARY KEY,
 DoctorName VARCHAR(10),
 Specialty VARCHAR(20),
 Gender varchar(6),
 Experience INT);
--Patient dimension table
CREATE TABLE Patient (
 PatientID INT PRIMARY KEY,
 PatientName VARCHAR(10),
 Age INT,
 Gender varchar(6),
 MedicalHistory varchar(20));
--Medical Records dimension table
CREATE TABLE MedicalRecords (
 MedicalRecordID INT PRIMARY KEY,
 Diagnosis VARCHAR(20),
 Treatment VARCHAR(20),
 Medication VARCHAR(20),
 PatientID INT,
 DoctorID INT,
 FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
 FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID));
--Admin dimension table
CREATE TABLE Admin (
 AdminID INT PRIMARY KEY,
 AdminName VARCHAR(10),
 Role VARCHAR(15),
 Gender varchar(6),
 Department VARCHAR(20) );
--Hospital fact table
CREATE TABLE HospitalVisits (
 VisitID INT PRIMARY KEY,
 DoctorID INT,
 PatientID INT,
 MedicalRecordID INT,
 AdminID INT,
 VisitDate DATE,
 Duration INT,
 Cost INT,
 FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
 FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
 FOREIGN KEY (MedicalRecordID) REFERENCES MedicalRecords(MedicalRecordID),
 FOREIGN KEY (AdminID) REFERENCES Admin(AdminID) );
--1) How many hospital visits were recorded in the fact table?
SELECT COUNT(*) AS TotalVisits FROM HospitalVisits;
--2) What is the total cost of all visits recorded in the fact table?
SELECT SUM(Cost) AS TotalCost FROM HospitalVisits;
--3) How many unique patients visited the hospital?
SELECT COUNT(DISTINCT PatientID) AS UniquePatients FROM HospitalVisits;
--4) List all the doctors along with their specialties.
SELECT DoctorName, Specialty FROM Doctor;
--5) What is the average duration of hospital visits?
SELECT AVG(Duration) AS AverageDuration 
 FROM HospitalVisits;
--6) Show the total cost of visits for each doctor&#39;s specialty, with a grand total for all specialties combined
SELECT
 NVL(d.Specialty, 'Grand Total') AS Specialty,
 SUM(hv.Cost) AS TotalCost
 FROM
 HospitalVisits hv
 JOIN
 Doctor d ON hv.DoctorID = d.DoctorID
 GROUP BY
 ROLLUP(d.Specialty)
 ORDER BY
 GROUPING(d.Specialty), d.Specialty;
