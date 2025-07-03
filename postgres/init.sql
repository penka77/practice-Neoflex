-- Создание роли student
CREATE ROLE student WITH LOGIN PASSWORD 'student_pass' NOSUPERUSER NOINHERIT NOCREATEDB NOCREATEROLE;

-- Отзыв прав на БД postgres
REVOKE CONNECT ON DATABASE postgres FROM PUBLIC;
REVOKE ALL ON DATABASE postgres FROM PUBLIC;

-- Создание БД metrics и отзыв прав
CREATE DATABASE metrics WITH OWNER = postgres_user;
REVOKE ALL ON DATABASE metrics FROM PUBLIC;
--GRANT CONNECT ON DATABASE metrics TO postgres_user;

-- Создание БД retail и отзыв прав
CREATE DATABASE retail WITH OWNER = postgres_user;
REVOKE ALL ON DATABASE retail FROM PUBLIC;
--GRANT CONNECT ON DATABASE retail TO postgres_user;

--Переход в БД metrics
\c metrics;

--Создание схемы metrics в БД metrics
CREATE SCHEMA metrics;

-- Все CREATE TABLE для БД metrics
CREATE TABLE metrics.market_prices (
 name_market varchar NOT NULL,
 position_name varchar NOT NULL,
 barcode varchar NOT NULL,
 type_product varchar NOT NULL,
 type_budget varchar NOT NULL,
 price float4 NOT NULL
);

CREATE TABLE metrics.preferences (
 id varchar NOT NULL,
 city varchar NOT NULL,
 supermarket float4 NOT NULL,
 build_market float4 NOT NULL,
 cafe float4 NOT NULL,
 zoo_market float4 NOT NULL,
 pharmacy float4 NOT NULL,
 other_market float4 NOT NULL,
 CONSTRAINT preferences_pk PRIMARY KEY (id)
);

CREATE TABLE metrics.supermarket (
 id varchar NOT NULL,
 budget float4 NOT NULL,
 middle float4 NOT NULL,
 premium float4 NOT NULL,
 CONSTRAINT supermarket_pk PRIMARY KEY (id)
);

CREATE TABLE metrics.build_market (
 id varchar NOT NULL,
 budget float4 NOT NULL,
 middle float4 NOT NULL,
 premium float4 NOT NULL,
 CONSTRAINT build_market_pk PRIMARY KEY (id)
);

CREATE TABLE metrics.cafe (
 id varchar NOT NULL,
 budget float4 NOT NULL,
 middle float4 NOT NULL,
 premium float4 NOT NULL,
 CONSTRAINT cafe_pk PRIMARY KEY (id)
);

CREATE TABLE metrics.zoo_market (
 id varchar NOT NULL,
 budget float4 NOT NULL,
 middle float4 NOT NULL,
 premium float4 NOT NULL,
 CONSTRAINT zoo_market_pk PRIMARY KEY (id)
);

CREATE TABLE metrics.pharmacy (
 id varchar NOT NULL,
 budget float4 NOT NULL,
 middle float4 NOT NULL,
 premium float4 NOT NULL,
 CONSTRAINT pharmacy_pk PRIMARY KEY (id)
);

CREATE TABLE metrics.other_market (
 id varchar NOT NULL,
 budget float4 NOT NULL,
 middle float4 NOT NULL,
 premium float4 NOT NULL,
 CONSTRAINT other_market_pk PRIMARY KEY (id)
);


CREATE TABLE metrics.terminals (
 id varchar NOT NULL,
 market varchar NOT NULL,
 bank varchar not NULL,
 imei varchar not NULL,
 os varchar not NULL
);

--Переходим в БД retail
\c retail;

--Создание схемы data в БД reatil
CREATE SCHEMA data;

-- Все CREATE TABLE для БД retail
CREATE TABLE data.cards (
 "number" varchar NOT NULL,
 "owner" varchar NOT NULL,
 bank varchar NOT NULL,
 payment_system varchar NOT NULL,
 CONSTRAINT cards_pk PRIMARY KEY (number)
);

CREATE TABLE data.banks (
 id varchar not null,
 name varchar NOT NULL,
 abbreviation varchar NOT NULL,
 inn varchar NOT NULL,
 ogrn varchar NOT null,
 bik varchar NOT null,
 phone varchar NOT null,
 date_open date NOT NULL,
 head_office varchar NOT null,
 CONSTRAINT banks_pk PRIMARY KEY (id)
);

CREATE TABLE data.peoples (
 id varchar NOT NULL,
 gender varchar NOT NULL,
 birthday date NOT NULL,
 CONSTRAINT peoples_pk PRIMARY KEY (id)
);

CREATE TABLE data.organizations (
 id varchar NOT NULL,
 address varchar NOT NULL,
 name_market varchar NULL,
 type_budget varchar NULL,
 mcc int2 NOT NULL,
 date_open date NOT NULL,
 date_close date NULL,
 CONSTRAINT organizations_pk PRIMARY KEY (id)
);

CREATE TABLE data.mcc (
 mcc int2 NOT NULL,
 type_organization varchar NOT NULL
);



-- GRANT для роли student на БД retail
GRANT CONNECT ON DATABASE retail TO student;
GRANT USAGE ON SCHEMA data TO student;
GRANT SELECT ON ALL TABLES IN SCHEMA data TO student;

