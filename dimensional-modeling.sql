create table employee_dimensiontable(emp_key int primary key, emp_name varchar(10),emp_age int);
create table role_dimensiontable(role_key int primary key, role_name varchar(10));
create table department_dimensiontable(department_key int primary key,department_name varchar(10));
create table time_dimensiontable(time_key int primary key, day varchar(10), month varchar(10), year int);
insert into employee_dimensiontable values(110,'Glavin',20);
insert into employee_dimensiontable values(111,'Valour',21);
insert into role_dimensiontable values(110,'Professor');
insert into role_dimensiontable values(111,'Accountant');
insert into department_dimensiontable values(110,'Finance');
insert into department_dimensiontable values(111,'Marketing');
insert into time_dimensiontable values(111,'Monday','April',2024)
insert into time_dimensiontable values(113,'Tuesday','May',2023);
select * from employee_dimensiontable;
select * from role_dimensiontable;
select * from department_dimensiontable;
select * from time_dimensiontable;
create table company_facttable( emp_key int, role_key int,department_key int,time_key int, no_of_hours int,no_of_leaves int,foreign key (emp_key) references employee_dimensiontable,foreign key (role_key) references role_dimensiontable,foreign key (department_key) references department_dimensiontable,foreign key (time_key) references time_dimensiontable);
insert into company_facttable values(110,111,110,111,6,7);
select * from company_facttable;
--Show Total Hours Worked by Each Employee 
select emp_key, SUM(no_of_hours) as Total_number_of_hours from company_facttable group by emp_key;
--Find Total Leaves Taken by Each Role 
select role_key, SUM(no_of_leaves) as Total_leaves_taken from company_facttable group by role_key;
--Total Hours Worked in Each Department
select department_key, SUM(no_of_hours) as Total_hours_worked from company_facttable group by department_key;
--List Employees with Their Departments 
select e.emp_name,d.department_name from employee_dimensiontable e join company_facttable c ON e.emp_key = c.emp_key join department_dimensiontable d ON c.department_key = d.department_key;
--Show Total Hours Worked by Each Employee with name 
select e.emp_name, SUM(no_of_hours) as total_hours_worked from employee_dimensiontable e join company_facttable c ON e.emp_key=c.emp_key group by e.emp_name;