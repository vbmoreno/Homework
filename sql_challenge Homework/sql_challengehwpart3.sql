﻿--1. List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT employees.emp_no, employees.first_name, employees.last_name, employees.sex, salaries.salary
FROM employees
Inner Join Salaries ON
employees.emp_no = salaries.employee_no;

--2. List first name, last name, and hire date for employees who were hired in 1986.
SELECT employees.first_name, employees.last_name, employees.hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
SELECT departments.dept_no, departments.dept_name, dept_manager.employee_no, employees.first_name, employees.last_name
FROM departments JOIN dept_manager on departments.dept_no = dept_manager.dept_no 
JOIN employees on dept_manager.employee_no = employees.emp_no;

--4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT employees.emp_no, employees.first_name, employees.last_name, dept_employees.employee_no
FROM employees
Inner Join dept_employees ON
employees.emp_no = dept_employees.employee_no;

--5. List first name, last name and sex for all people whose first name is Herculas but last name starts with B.
SELECT employees.first_name, employees.last_name, employees.sex
FROM employees
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT departments.dept_name, dept_employees.employee_no, employees.first_name, employees.last_name 
FROM dept_employees 
JOIN employees on dept_employees.employee_no = employees.emp_no 
JOIN departments on dept_employees.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales';

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT departments.dept_name, dept_employees.employee_no, employees.first_name, employees.last_name 
FROM dept_employees 
JOIN employees on dept_employees.employee_no = employees.emp_no 
JOIN departments on dept_employees.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales' or departments.dept_name = 'Development';


--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT employees.last_name, COUNT (last_name) AS "frequency"
FROM employees
GROUP BY last_name
ORDER BY 
Count (last_name) DESC;


