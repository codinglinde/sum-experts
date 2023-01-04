CREATE DATABASE software_project_practice1;
USE software_project_practice1;
-- Create customer table
CREATE TABLE customer
  (
     customer_id   INTEGER PRIMARY KEY auto_increment,
     f_name        VARCHAR(55) NOT NULL,
     l_name        VARCHAR(55) NOT NULL,
     address       VARCHAR(100) NOT NULL,
     email_address VARCHAR(55) NOT NULL,
     phone_num     BIGINT NOT NULL
  );
-- Create services table
CREATE TABLE services
  (
     services_id INTEGER PRIMARY KEY auto_increment,
     service     VARCHAR(100) NOT NULL
  );
-- Create advisor table
CREATE TABLE advisor
  (
     advisor_id    INTEGER PRIMARY KEY auto_increment,
     f_name        VARCHAR(55) NOT NULL,
     l_name        VARCHAR(55) NOT NULL,
     specialism    VARCHAR(55) NOT NULL,
     email_address VARCHAR(55) NOT NULL,
     phone_num     VARCHAR(55) NOT NULL,
     services_id   INT,
     FOREIGN KEY (services_id) REFERENCES services(services_id)
  );

-- Create products table
CREATE TABLE product
  (
     product_id   INTEGER PRIMARY KEY auto_increment,
     product_name VARCHAR(55) NOT NULL,
     services_id  INT,
     FOREIGN KEY (services_id) REFERENCES services(services_id)
  );
-- Populate data into customer
INSERT INTO customer
            (f_name,
             l_name,
             address,
             email_address,
             phone_num)
VALUES      ('Isaac',
             'Talbot',
             '32 Nenthead Road, Littleton, BS18 2LY',
             'talbot.i@bungar.biz',
             07878273722),
            ('Finlay',
             'Arnold',
             '55 Temple Way, WITHAM ON THE HILL, PE10 6PS',
             'arnold4878@bauros.biz',
             07829896659),
            ('Alfie',
             'Lucas',
             '14 Ponteland Rd, HOUNSLOW WEST, TW3 8HA',
             'alfie1744@infotech44.tech',
             07750072584);

-- Populate data into advisor
INSERT INTO advisor
            (f_name,
             l_name,
             specialism,
             email_address,
             phone_num)
VALUES      ('Phoebe',
             'Casey',
             'Mortgage',
             'Phoebe_Casey7816@bungar.biz',
             '01232 223278 (01)'),
            ('Julius',
             'Ebden',
             'Investments',
             'Julius_Ebden4878@bauros.biz',
             '01232 223278 (02)'),
            ('Jack',
             'Curtis',
             'FinancialPlanner',
             'Jack_Curtis1744@infotech44.tech',
             '01232 223278 (03)'),
            ('Kurt',
             'Knott',
             'Mortgage',
             'Kurt_Knott3351@bulaffy.com',
             '01232 223278 (04)'),
            ('Erick',
             'Ross',
             'Investments',
             'Erick_Ross6986@tonsy.org',
             '01232 223278 (05)' );

-- Populate data into services
INSERT INTO services
            (service)
VALUES      ('Mortgage'),
            ('Mortgage'),
            ('Investment (Savings)'),
            ('Investment (Stocks & Bonds)'),
            ('Financial Planning (Plan)');
-- Populate data into products
INSERT INTO product
            (product_name)
VALUES      ('Financial Planner'),
            ('Mortgage Planner'),
            ('Investment Savings Road Map'),
            ('Investment Stocks & Bonds Planner'),
            ('Mortgage Rates Service');

CREATE TABLE `bookings` (
  `advisor` varchar(45) DEFAULT NULL,
  `09-10` int(11) DEFAULT NULL,
  `09-10-booking-id` varchar(20) DEFAULT NULL,
  `10-11` int(11) DEFAULT NULL,
  `10-11-booking-id` varchar(20) DEFAULT NULL,
  `11-12` int(11) DEFAULT NULL,
  `11-12-booking-id` varchar(20) DEFAULT NULL,
  `12-13` int(11) DEFAULT NULL,
  `12-13-booking-id` varchar(20) DEFAULT NULL,
  `13-14` int(11) DEFAULT NULL,
  `13-14-booking-id` varchar(20) DEFAULT NULL,
  `14-15` int(11) DEFAULT NULL,
  `14-15-booking-id` varchar(20) DEFAULT NULL,
  `15-16` int(11) DEFAULT NULL,
  `15-16-booking-id` varchar(20) DEFAULT NULL,
  `16-17` int(11) DEFAULT NULL,
  `16-17-booking-id` varchar(20) DEFAULT NULL,
  `bookingDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `filldates`(dateStart DATE, dateEnd DATE, advisor VARCHAR(20))
BEGIN
  WHILE dateStart <= dateEnd DO
    INSERT INTO bookings (advisor, bookingDate) VALUES (advisor, dateStart);
    SET dateStart = date_add(dateStart, INTERVAL 1 DAY);
  END WHILE;
END$$
DELIMITER ;


call filldates('20221101', '20221130', 'Phoebe');
call filldates('20221101', '20221130', 'Julius');
call filldates('20221101', '20221130', 'Jack');
call filldates('20221101', '20221130', 'Kurt');
call filldates('20221101', '20221130', 'Erick');

