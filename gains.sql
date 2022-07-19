CREATE DATABASE  IF NOT EXISTS `gains` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gains`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: gains
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` varchar(45) DEFAULT 'CURRENT_TIMESTAMP()',
  `updated_at` varchar(45) DEFAULT 'CURRENT_TIMESTAMP()',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Trevor','Ryan','2@gmail.com','$2b$12$QBGWgIIxy01jN4OmEP6pkOP/whuor8k3p.c3Enw1Qif2dv0fIt4Cu','CURRENT_TIMESTAMP()','CURRENT_TIMESTAMP()'),(2,'Mike','Ryan','3@gmail.com','$2b$12$6F93w9oKbDvqyZel1Cb8e.teZQPe3qDFUWgqI3HhZQ3gB1J.WS4mK','CURRENT_TIMESTAMP()','CURRENT_TIMESTAMP()'),(3,'Trevor','Ryan','4@gmail.com','$2b$12$AC29Bp9Mf7O2kw.Wpx5TteSpHf5QJe55BaEDRuR4PrMvecEzRK.wW','CURRENT_TIMESTAMP()','CURRENT_TIMESTAMP()');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workouts`
--

DROP TABLE IF EXISTS `workouts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workouts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `compound_lift` varchar(45) DEFAULT NULL,
  `compound_lift2` varchar(45) DEFAULT NULL,
  `compound_lift3` varchar(45) DEFAULT NULL,
  `accessory` varchar(45) DEFAULT NULL,
  `accessory2` varchar(45) DEFAULT NULL,
  `accessory3` varchar(45) DEFAULT NULL,
  `created_at` varchar(45) DEFAULT 'CURRENT_TIMESTAMP()',
  `updated_at` varchar(45) DEFAULT 'CURRENT_TIMESTAMP()',
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_workouts_users_idx` (`user_id`),
  CONSTRAINT `fk_workouts_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workouts`
--

LOCK TABLES `workouts` WRITE;
/*!40000 ALTER TABLE `workouts` DISABLE KEYS */;
INSERT INTO `workouts` VALUES (1,'Upper one','great','Bench','Bench','Bench','curl','curl','curl','CURRENT_TIMESTAMP()','2022-07-13 20:12:22',1),(3,'Lower','Legs and more legs andfggf','Bench','Bench','Bench','curl','Curl','curl','CURRENT_TIMESTAMP()','2022-07-18 18:22:33',2),(5,'Upper','Chest and back cxcc','Bench','Bench','Bench','Curl','Curl','Curl','CURRENT_TIMESTAMP()','2022-07-18 18:22:37',2),(7,'sdfdfds','dsfddf','Bench','Bench','Bench','curl','curl','curl','CURRENT_TIMESTAMP()','CURRENT_TIMESTAMP()',3);
/*!40000 ALTER TABLE `workouts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-18 18:36:38
