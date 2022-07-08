import mysql.connector as sq

mydb=sq.connect(host="localhost",user="User",passwd="password",buffered=True)

mycursor=mydb.cursor()

mycursor.execute('CREATE SCHEMA nj_state_teachers_salaries_cls')

SQLCMD = 'CREATE TABLE nj_state_teachers_salaries_cls.nj_state_teachers_salaries(last_name varchar(50),\
first_name varchar(50),county varchar(50),district varchar(200),school varchar(200),primary_job varchar(200),\
fte FLOAT,salary INT,certificate varchar(50),subcategory varchar(50),teaching_route varchar(30),\
highly_qualified varchar(150),experience_district INT,experience_nj INT,experience_total INT)'
    
mycursor.execute(SQLCMD)

SQLCMD="""LOAD DATA INFILE '/autograder/nj_teachers_salaries_cls.csv'\
INTO TABLE nj_state_teachers_salaries_cls.nj_state_teachers_salaries FIELDS TERMINATED BY',' \
OPTIONALLY ENCLOSED BY '"'\
LINES TERMINATED BY '\\n' IGNORE 1 ROWS """

mycursor.execute(SQLCMD)

mydb.commit()


