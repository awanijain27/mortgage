CREATE DATABASE  IF NOT EXISTS `loan_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `loan_management`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: loan_management
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `all_records`
--

DROP TABLE IF EXISTS `all_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `all_records` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `Amount` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father_name` varchar(30) NOT NULL,
  `Location` varchar(30) NOT NULL,
  `Date` date NOT NULL,
  `Type` varchar(10) NOT NULL,
  `Weight` float(8,3) DEFAULT NULL,
  `Deposit` int DEFAULT NULL,
  `Deposit_date` date DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `all_records`
--

LOCK TABLES `all_records` WRITE;
/*!40000 ALTER TABLE `all_records` DISABLE KEYS */;
INSERT INTO `all_records` VALUES (103,50000,'awani ','shailesh jain','Khalwa','2023-07-08','N',400.000,NULL,NULL),(104,4000,'Sabulal','Vishram','Sawlikheda','2023-07-08','N',410.000,NULL,NULL),(105,5500,'Jitendra','Jain','Khalwa','2023-07-08','N',200.000,NULL,NULL),(106,4520,'akshat','jain','Khalwa','2023-07-07','N',210.000,500,'2023-07-08');
/*!40000 ALTER TABLE `all_records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `removed_records`
--

DROP TABLE IF EXISTS `removed_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `removed_records` (
  `User_id` int NOT NULL,
  `Amount` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father_name` varchar(30) NOT NULL,
  `Location` varchar(30) NOT NULL,
  `Date` date NOT NULL,
  `Removed_date` date DEFAULT (curdate()),
  `Type` varchar(10) NOT NULL,
  `Weight` float(8,3) DEFAULT NULL,
  `Interest` int DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `removed_records`
--

LOCK TABLES `removed_records` WRITE;
/*!40000 ALTER TABLE `removed_records` DISABLE KEYS */;
INSERT INTO `removed_records` VALUES (101,40000,'akshat','Shailesh','Khalwa','2023-01-21','2023-07-08','N',510.000,6628),(102,3000,'Sabulal','Vishram','Sawlikheda','2023-07-08','2023-07-08','N',225.000,520);
/*!40000 ALTER TABLE `removed_records` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-09  0:27:00
