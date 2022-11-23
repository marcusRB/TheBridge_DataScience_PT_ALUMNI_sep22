-- Creamos el SCHEMA erp
CREATE SCHEMA IF NOT EXISTS erp;

-- Creamos la tabla erp.tb_company

DROP TABLE erp.tb_company;
CREATE TABLE IF NOT EXISTS erp.tb_company (
	co_code char(3) NOT NULL
	,co_name varchar(50) NOT NULL
	,co_address varchar(50) NOT NULL
	,co_city varchar(50) NOT NULL
	,co_country varchar(30) NOT NULL DEFAULT 'España'
	,last_updated_by varchar(20) NOT NULL DEFAULT 'System'
	,last_update_date date NOT NULL
	,CONSTRAINT pk_company PRIMARY KEY (co_code)
);


DROP TABLE erp.tb_customer;
CREATE TABLE IF NOT EXISTS erp.tb_customer (
	cust_no char(5) NOT NULL
	,cust_name varchar(50) NOT NULL
	,cust_cif varchar(15) NOT NULL
	,last_updated_by varchar(20) NOT NULL DEFAULT 'System'
	,last_update_date date NOT NULL
	,CONSTRAINT pk_customer PRIMARY KEY (cust_no)
);

DROP TABLE erp.tb_site;
CREATE TABLE IF NOT EXISTS erp.tb_site (
	cust_no char(5) NOT NULL
	,site_id int4 NOT NULL
	,site_code char(5) NOT NULL
	,site_name varchar(50) NOT NULL
	,site_address varchar(150) NOT NULL
	,site_city varchar(50) NOT NULL
	,site_country varchar(30) NOT NULL DEFAULT 'España'
	,site_phone numeric NULL
	,co_code char(3) NOT NULL
	,last_updated_by varchar(20) NOT NULL DEFAULT 'System'
	,last_update_date date NOT NULL
	,CONSTRAINT pk_site PRIMARY KEY (site_id)
	,CONSTRAINT fk_site_company FOREIGN KEY (co_code) REFERENCES erp.tb_company (co_code)
	,CONSTRAINT fk_site_customer FOREIGN KEY (cust_no) REFERENCES erp.tb_customer (cust_no)
);




