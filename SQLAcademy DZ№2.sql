USE Academy;
CREATE TABLE Groups (
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(10) NOT NULL UNIQUE, 
Rating int NOT NULL,
CHECK (0 <= Rating and Rating >=  5),
"Year" int NOT NULL,
CHECK (1 <=  "Year" and "Year" > =  5)
);
CREATE TABLE Departments (
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Financing money NOT NULL DEFAULT(0),
CHECK (0 <= Financing),
"Name" nvarchar(100) NOT NULL UNIQUE
);
CREATE TABLE Faculties (
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(100) NOT NULL UNIQUE
);
CREATE TABLE Teachers (
ID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
EmploymentDate date NOT NULL
CHECK (EmploymentDate >= '01.01.1990'),
"Name" nvarchar(max) NOT NULL,
Premium money NOT NULL DEFAULT(0),
CHECK (Premium >= 0),
Salary money NOT NULL
CHECK (Salary > 0),
Surname nvarchar(max) NOT NULL
);