

CREATE TABLE departments (
    dept_no VARCHAR(255)   NOT NULL,
    dept_name VARCHAR(255)   NOT NULL,
    CONSTRAINT pk_departments PRIMARY KEY (
        dept_no
     )
);

CREATE TABLE dept_employees (
    employee_no VARCHAR(255)   NOT NULL,
    dept_no VARCHAR(255)   NOT NULL
);

CREATE TABLE dept_manager (
    dept_no VARCHAR(255)   NOT NULL,
    employee_no VARCHAR(255)   NOT NULL
);

CREATE TABLE employees (
    employee_no INT   NOT NULL,
    title_id VARCHAR(255)   NOT NULL,
    birth_date VARCHAR (255)   NOT NULL,
    first_name VARCHAR(255)   NOT NULL,
    last_name VARCHAR(255)   NOT NULL,
    sex VARCHAR(255)   NOT NULL,
    hire_date VARCHAR (255)   NOT NULL,
    CONSTRAINT pk_employees PRIMARY KEY (
        employee_no
     )
);

CREATE TABLE salaries (
    employee_no INT   NOT NULL,
    salary INT   NOT NULL
);

CREATE TABLE titles (
    title_id INT   NOT NULL,
    titles VARCHAR(255)   NOT NULL,
    CONSTRAINT pk_titles PRIMARY KEY (
        title_id
     )
);

ALTER TABLE dept_employees ADD CONSTRAINT fk_dept_employees_employee_no FOREIGN KEY(employee_no)
REFERENCES employees (employee_no);

ALTER TABLE dept_employees ADD CONSTRAINT fk_dept_employees_dept_no FOREIGN KEY(dept_no)
REFERENCES departments (dept_no);

ALTER TABLE dept_manager ADD CONSTRAINT fk_dept_manager__employee_no FOREIGN KEY(employee_no)
REFERENCES employees (employee_no);

ALTER TABLE employees ADD CONSTRAINT fk_employees__title_id FOREIGN KEY(title_id)
REFERENCES titles (title_id);

ALTER TABLE salaries ADD CONSTRAINT fk_salaries_employee_no FOREIGN KEY(employee_no)
REFERENCES employees (employee_no);

