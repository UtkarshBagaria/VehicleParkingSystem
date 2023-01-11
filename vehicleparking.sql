-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 16, 2020 at 08:00 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inet_vehicleparking`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_booking`
--
create database 477_vehicle_parking;

use 477_vehicle_parking;

CREATE TABLE `tbl_booking` (
  `booking_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `slot_id` int(11) NOT NULL,
  `booking_status` int(1) NOT NULL,
  `user_id` int(11) NOT NULL
);

LOAD DATA INFILE 'D:/Sem-5/LAB/DBMS/Project/booking_val.csv'
INTO TABLE tbl_booking 
COLUMNS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
ESCAPED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;
-- --------------------------------------------------------

--
-- Table structure for table `tbl_parking_slot`
--

CREATE TABLE `tbl_parking_slot` (
  `parking_slot_id` int(11) NOT NULL,
  `parking_slot_number` int(4) NOT NULL,
  `parking_slot_status` int(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ;

INSERT INTO `tbl_parking_slot` (`parking_slot_id`, `parking_slot_number`, `parking_slot_status`, `user_id`) VALUES
(20, 14, 1, 69892),
(21, 16, 0, NULL),
(22, 17, 1, 63902),
(23, 21, 1, 69322),
(24, 25, 1, NULL);
-- --------------------------------------------------------

--
-- Table structure for table `tbl_payment`
--

CREATE TABLE `tbl_payment` (
  `payment_id` int(11) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `paid_by` varchar(30) NOT NULL,
  `amount` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ;

INSERT INTO `tbl_payment` (`payment_id`, `booking_id`, `paid_by`,`amount`, `user_id`) VALUES
(97291, 999, 'Aron',10, 69892),
(80311, 998, 'John',30, 63902),
(19201, 997, 'Snow',50, 69322);
-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `user_id` int(11) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `status` int(1) NOT NULL
) ;

INSERT INTO `tbl_user` (`user_id`, `fullname`, `contact`, `status`) VALUES
(69892, 'Aron Bond', '1234567890', 1),
(63902, 'John M', '0987654321', 1),
(69322, 'Snow B', '1111199999', 1);
-- --------------------------------------------------------

--
-- Table structure for table `tbl_vehicle`
--

CREATE TABLE `tbl_vehicle` (
  `vehicle_id` int(11) NOT NULL,
  `vehicle_category_id` int(11) NOT NULL,
  `vehicle_plate_number` varchar(15) NOT NULL,
  `vehicle_owner_id` int(11) NOT NULL
) ;

INSERT INTO `tbl_vehicle` (`vehicle_id`, `vehicle_category_id`, `vehicle_plate_number`, `vehicle_owner_id`) VALUES
(2524, 2, 'KA1234', 1000),
(2382, 4, 'WB5678', 1001),
(2392, 5, 'MA1920', 1002);
-- --------------------------------------------------------

--
-- Table structure for table `tbl_vehicle_category`
--

CREATE TABLE `tbl_vehicle_category` (
  `vehicle_category_id` int(11) NOT NULL,
  `vehicle_category_name` varchar(30) NOT NULL,
  `user_id` int(11) NOT NULL
) ;

INSERT INTO `tbl_vehicle_category` (`vehicle_category_id`, `vehicle_category_name`, `user_id`) VALUES
(2, 'Bike', 69892),
(4, 'Car', 63902),
(5, 'Bus', 69322);
-- --------------------------------------------------------

--
-- Table structure for table `tbl_vehicle_owner`
--

CREATE TABLE `tbl_vehicle_owner` (
  `vehicle_owner_id` int(11) NOT NULL,
  `vehicle_owner_name` varchar(30) NOT NULL,
  `vehicle_owner_contact` varchar(15) NOT NULL,
  `user_id` int(11) NOT NULL
) ;

INSERT INTO `tbl_vehicle_owner` (`vehicle_owner_id`, `vehicle_owner_name`, `vehicle_owner_contact`, `user_id`) VALUES
(1000, 'Aron Bond', '1234567890', 69892),
(1001, 'John M', '0987654321', 63902),
(1002, 'Snow B', '1111199999', 69322);
--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_booking`
--
ALTER TABLE `tbl_booking`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `vehicle_id` (`vehicle_id`),
  ADD KEY `slot_id` (`slot_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tbl_parking_slot`
--
ALTER TABLE `tbl_parking_slot`
  ADD PRIMARY KEY (`parking_slot_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tbl_payment`
--
ALTER TABLE `tbl_payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `booking_id` (`booking_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`user_id`);


--
-- Indexes for table `tbl_vehicle`
--
ALTER TABLE `tbl_vehicle`
  ADD PRIMARY KEY (`vehicle_id`),
  ADD KEY `vehicle_owner_id` (`vehicle_owner_id`),
  ADD KEY `vehicle_category_id` (`vehicle_category_id`);

--
-- Indexes for table `tbl_vehicle_category`
--
ALTER TABLE `tbl_vehicle_category`
  ADD PRIMARY KEY (`vehicle_category_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tbl_vehicle_owner`
--
ALTER TABLE `tbl_vehicle_owner`
  ADD PRIMARY KEY (`vehicle_owner_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_booking`
--
ALTER TABLE `tbl_booking`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_parking_slot`
--
ALTER TABLE `tbl_parking_slot`
  MODIFY `parking_slot_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_payment`
--
ALTER TABLE `tbl_payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_vehicle`
--
ALTER TABLE `tbl_vehicle`
  MODIFY `vehicle_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_vehicle_category`
--
ALTER TABLE `tbl_vehicle_category`
  MODIFY `vehicle_category_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_vehicle_owner`
--
ALTER TABLE `tbl_vehicle_owner`
  MODIFY `vehicle_owner_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_booking`
--
ALTER TABLE `tbl_booking`
  ADD CONSTRAINT `tbl_booking_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_booking_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `tbl_vehicle_owner` (`vehicle_owner_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_booking_ibfk_3` FOREIGN KEY (`vehicle_id`) REFERENCES `tbl_vehicle` (`vehicle_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_booking_ibfk_4` FOREIGN KEY (`slot_id`) REFERENCES `tbl_parking_slot` (`parking_slot_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_parking_slot`
--
ALTER TABLE `tbl_parking_slot`
  ADD CONSTRAINT `tbl_parking_slot_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_payment`
--
ALTER TABLE `tbl_payment`
  ADD CONSTRAINT `tbl_payment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_payment_ibfk_2` FOREIGN KEY (`booking_id`) REFERENCES `tbl_booking` (`booking_id`) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- Constraints for table `tbl_vehicle`
--
ALTER TABLE `tbl_vehicle`
  ADD CONSTRAINT `tbl_vehicle_ibfk_1` FOREIGN KEY (`vehicle_category_id`) REFERENCES `tbl_vehicle_category` (`vehicle_category_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_vehicle_ibfk_2` FOREIGN KEY (`vehicle_owner_id`) REFERENCES `tbl_vehicle_owner` (`vehicle_owner_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_vehicle_category`
--
ALTER TABLE `tbl_vehicle_category`
  ADD CONSTRAINT `tbl_vehicle_category_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_vehicle_owner`
--
ALTER TABLE `tbl_vehicle_owner`
  ADD CONSTRAINT `tbl_vehicle_owner_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

UPDATE tbl_parking_slot
SET 
    parking_slot_status = 0 
WHERE
    parking_slot_status = 1;

UPDATE tbl_booking
SET 
    booking_status = 0 
WHERE
    booking_status = 1;

-- Join queries
-- 1)get all the booking details with payment details
SELECT * FROM tbl_booking join tbl_payment on tbl_booking.user_id=tbl_payment.user_id;
-- 2)get each booking with all the vehicle owner details
SELECT * FROM tbl_booking right outer join tbl_vehicle_owner on tbl_booking.user_id=tbl_vehicle_owner.user_id;
-- 3)get all the booking details with each user
SELECT * FROM tbl_booking left outer join tbl_user on tbl_booking.user_id=tbl_user.user_id;
-- 4)get all the vehicle details with vehicle owner details and category details
SELECT * FROM tbl_vehicle join tbl_vehicle_owner on tbl_vehicle.vehicle_owner_id=tbl_vehicle_owner.vehicle_owner_id join tbl_vehicle_category on tbl_vehicle.vehicle_category_id=tbl_vehicle_category.vehicle_category_id;

-- Aggregate functions
-- 1)Get the total number of bookings
SELECT COUNT(*) FROM tbl_booking;
-- 2)get the total amount paid
SELECT SUM(amount) FROM tbl_payment
-- 3)get the min max avg payments
SELECT max(amount) as Max_Cost,min(amount) as Min_Cost FROM tbl_payment;
-- 4)get the total number of 2 wheelers
SELECT COUNT(*) FROM tbl_vehicle where vehicle_category_id=2;

-- Set Operations
--1)Find the users with active booking and an active slot
SELECT U.user_id,U.fullname
FROM tbl_user as U, tbl_booking as B
WHERE U.user_id=B.user_id and B.booking_status=1
UNION 
SELECT P.parking_slot_id,P.parking_slot_number
FROM tbl_user as U1, tbl_parking_slot as P
WHERE U1.user_id=P.user_id and P.parking_slot_status=1;

--2)Get the details about vehicle vehicle owner when vehicle is 2 wheeler
SELECT V.vehicle_id,V.vehicle_plate_number
FROM tbl_vehicle as V, tbl_vehicle_owner as VO
WHERE V.vehicle_owner_id=VO.vehicle_owner_id 
UNION 
SELECT V1.vehicle_id,V1.vehicle_plate_number
FROM tbl_vehicle as V1, tbl_vehicle_category as VCO
WHERE V1.vehicle_category_id=VCO.vehicle_category_id and VCO.vehicle_category_id=2;
-- 3)Get the details about vehicle vehicle owner when vehicle is 4 wheeler
SELECT V.vehicle_id,V.vehicle_plate_number
FROM tbl_vehicle as V, tbl_vehicle_owner as VO
WHERE V.vehicle_owner_id=VO.vehicle_owner_id
UNION
SELECT V1.vehicle_id,V1.vehicle_plate_number
FROM tbl_vehicle as V1, tbl_vehicle_category as VCO
WHERE V1.vehicle_category_id=VCO.vehicle_category_id and VCO.vehicle_category_id=4;
--4)Find the users with inactive booking or inactive slot
SELECT U.user_id,U.fullname
FROM tbl_user as U, tbl_booking as B
WHERE U.user_id=B.user_id and B.booking_status=1 and
EXISTS(
SELECT U1.user_id,U1.fullname
FROM tbl_user as U1, tbl_parking_slot as P
WHERE U1.user_id=P.user_id and P.parking_slot_status=0
);
-- Functions
DELIMITER $$
CREATE FUNCTION active_booking(booking_status int(1))
RETURNS varchar(150)
DETERMINISTIC
BEGIN
DECLARE value varchar(150);
IF ((booking_status) = 1) then
SET value = "You have an active booking";
ELSE
SET value = "Your booking has either expired or you have no booking";
END IF;
RETURN value;
END $$
DELIMITER;

WITH dat as 
(SELECT user_id, booking_status FROM tbl_booking) 
SELECT user_id, booking_status, active_booking(booking_status) as stat FROM dat;

-- PROCEDURE --
DELIMITER $$
CREATE PROCEDURE empty_slot(
IN id int,IN st int, OUT msg varchar(50))
BEGIN
DECLARE `parking_slot_status` int;
UPDATE tbl_parking_slot
SET `parking_slot_status` = st
WHERE parking_slot_id= id;
SET msg='slot updated';
END;$$
DELIMITER ;

CALL empty_slot(24,0,@msg);
SELECT @msg;
SELECT * FROM tbl_parking_slot;

-- TRIGGER --
CREATE TABLE `DEL_parking_slot` (
  `booking_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `slot_id` int(11) NOT NULL,
  `booking_status` int(1) NOT NULL,
  `user_id` int(11)
) ; 

DELIMITER $$
CREATE TRIGGER booking_stat BEFORE DELETE ON tbl_parking_slot
FOR EACH ROW
BEGIN
INSERT INTO DEL_parking_slot SELECT * FROM tbl_booking where slot_id = old.parking_slot_id;
END;$$
DELIMITER ;

SET FOREIGN_KEY_CHECKS=0;
DELETE FROM tbl_parking_slot WHERE parking_slot_id=22; 
SELECT * FROM DEL_parking_slot
;

INSERT INTO `tbl_parking_slot` (`parking_slot_id`, `parking_slot_number`, `parking_slot_status`, `user_id`) VALUES
(22, 17, 1, 63902);

-- CURSOR --
DELIMITER $$
CREATE PROCEDURE total_empty(IN emp int, OUT count int)
BEGIN
DECLARE done INT DEFAULT FALSE;
DECLARE cur1 CURSOR FOR SELECT count(*) FROM tbl_parking_slot where parking_slot_status=emp;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
OPEN cur1;
read_loop: LOOP
FETCH cur1 INTO count;
IF done THEN
LEAVE read_loop;
END IF;
END LOOP;
CLOSE cur1;
END $$
DELIMITER ;

CALL total_empty(0,@A);
SELECT @A;