CREATE TABLE student
	(ID			varchar(5), 
	 name			varchar(20) not null, 
	 
	 PRIMARY KEY (ID, name)
	);

CREATE TABLE company
	(ID			varchar(5), 
	 name			varchar(20) not null, 
	 
	 PRIMARY KEY (ID, name)
	);

CREATE TABLE tag
	(ID			varchar(5), 
	 name			varchar(20) not null, 
	 
	 PRIMARY KEY (ID, name)
	);

CREATE TABLE internship
	(ID			varchar(5), 
	 title			varchar(20) not null, 
	 s_id			varchar(5),
	 t_id			varchar(5),
	 t_name			varchar(20) not null, 
	 start_date		varchar(10),
	 end_date		varchar(10),
	 c_id			varchar(5),


	 PRIMARY KEY (ID, title, s_id),
	 FOREIGN KEY (c_id) REFERENCES company,
	 FOREIGN KEY (s_id) REFERENCES student,
	 FOREIGN KEY (t_id, t_name) REFERENCES tag
	);
