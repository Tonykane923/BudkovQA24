create database praktika_2;
use Hospital;
create table Diseases
(
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(100) NOT NULL UNIQUE,
Severity int NOT NULL default(1),
check (Severity >= 0),
);