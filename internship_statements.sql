SELECT *
    FROM student
    WHERE id = '11111'; -- variable

SELECT *
    FROM internship
    WHERE s_id = '11111'; -- variable

SELECT name
    FROM companies;

SELECT *
    FROM tags;

INSERT INTO internship (ID, title, s_id, t_id, t_name, start_date, end_date, c_id)
    VALUES (54321, 'Title', '11111', '22222', 'TagName', 'YYYY-MM-DD', 'YYYY-MM-DD', '33333');

UPDATE internship
    SET title = 'New Title', t_id = '23451',
        t_name = 'New Tag Name', start_date = 'New Date',
        end_date = 'New Date'
    WHERE ID = '11111';

INSERT INTO tag (ID, name)
    VALUES ('22234', 'New Tag Name');


INSERT INTO company (ID, name)
    VALUES ('33333', 'New Company Name');

CREATE view submissions as

    SELECT student.name, company.name, internship.title, internship.t_name
    FROM internship
        JOIN student on internship.s_id = student.id
        JOIN company on internship.c_id = company.id
        JOIN tag on internship.t_id = tag.id
    ORDER BY student.name;
