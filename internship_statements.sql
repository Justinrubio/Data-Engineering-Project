--Selects for Student by username/id for log in

SELECT *
    FROM student
    WHERE id = '11111'; -- variable, needs where because of variable


--List of prior submissions for a student by username/id

SELECT *
    FROM internship
    WHERE s_id = '11111'; -- variable, needs where because of variable


--List of companies for a pick-list field

SELECT name
    FROM companies;

--List of tags

SELECT *
    FROM tags;


--Insert statement for a new internship submission

INSERT INTO internship (ID, title, s_id, t_id, t_name, start_date, end_date, c_id)
    VALUES (54321, 'Title', '11111', '22222', 'TagName', 'YYYY-MM-DD', 'YYYY-MM-DD', '33333');  -- values will be variables


--Update statement for an existing internship submission

UPDATE internship
    SET title = 'New Title', t_id = '23451',
        t_name = 'New Tag Name', start_date = 'New Date',
        end_date = 'New Date'
    WHERE ID = '11111';  -- values will be variables


--Insert for new company or tags

--Insert for tag
INSERT INTO tag (ID, name)
    VALUES ('22234', 'New Tag Name');  -- values will be variables


--Insert for company
INSERT INTO company (ID, name)
    VALUES ('33333', 'New Company Name');  -- values will be variables


--Create a DML statement for a View that gathers submission data, i.e. submission, student, company, tags

CREATE view submissions as

    SELECT student.name, company.name, internship.title, internship.t_name
    FROM internship
        JOIN student on internship.s_id = student.id  -- linking internship student ids
        JOIN company on internship.c_id = company.id  -- linking internship company ids
        JOIN tag on internship.t_id = tag.id  -- linking internship tag ids
    ORDER BY student.name;
