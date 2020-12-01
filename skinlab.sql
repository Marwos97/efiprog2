-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: skinlab
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `addskin`
--

DROP TABLE IF EXISTS `addskin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addskin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `float` decimal(10,2) NOT NULL,
  `stock` int DEFAULT NULL,
  `brand_id` int NOT NULL,
  `category_id` int NOT NULL,
  `image` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brand_id` (`brand_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `addskin_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`),
  CONSTRAINT `addskin_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addskin`
--

LOCK TABLES `addskin` WRITE;
/*!40000 ALTER TABLE `addskin` DISABLE KEYS */;
INSERT INTO `addskin` VALUES (16,'AK47-FRACTURE',2000.00,0.60,2,9,5,'eb8fcec8a08e37e4c21b.jpg'),(17,'AK47-REDLINE',900.00,0.10,1,10,5,'fdf1c87ba4af61f01eab.jpg'),(18,'AWP-ASIMOV',8000.00,0.07,6,7,6,'0a14e2d6c856e465f9a5.jpg'),(19,'AWP-REDLINE',3500.00,0.80,2,10,6,'e359b3660f041716af9a.jpeg'),(20,'DK-FRACTURE',1000.00,0.67,3,9,14,'4db9a4178848d3901061.jpg'),(21,'DK-ASIMOV',15000.00,0.02,10,7,14,'3384e512ee244f408c21.jpg'),(22,'GLOCK-NEONOIR',600.00,0.40,5,8,13,'ed185833e6f03000115b.jpeg'),(23,'M4-FRACTURE',4000.00,0.60,2,9,9,'cccae72af54663a3dbd0.jpg'),(24,'M4A4-NEO NOIR',5500.00,0.40,6,8,12,'7762d64aacad9cfda1f2.jpeg'),(26,'MAC10-FRACTURE',1500.00,0.20,2,9,10,'9b1d43fe157449767014.jpg'),(27,'P90-ASIMOV',3000.00,0.07,5,7,11,'a6aeaa49f9857adc23a8.jpg'),(30,'M4-NEO NOIR',7000.00,0.07,3,8,9,'e6a8fd007486bb16ee24.jpg');
/*!40000 ALTER TABLE `addskin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (7,'ASIMOV'),(9,'FRACTURE 2'),(8,'NEO-NOIR'),(10,'RED-LINE');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (5,'AK-47'),(6,'AWP'),(14,'DK'),(13,'GLOCK'),(9,'M4'),(12,'M4A4'),(10,'MAC10'),(8,'P250'),(11,'P90'),(7,'USP');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Joe Vidal','joevidal5','joe.vidal.bmx@hotmail.com','$2b$12$rVD./Yji1uZ6hMMytVBIC.heqPuQIEUrqAwczQrXDHqMbibb9vTkO'),(2,'joel','Sh4rk3n','joe.vidal.bmx@gmail.com','$2b$12$6Kw/L2hcZ0K59Z/.Izz8z.15W80Lnz0kfu6MS2CJJD2gKwPNLxWgm'),(4,'admin1','admin1','admin@admin.com','$2b$12$f.9zeQ9k1fHrq4DtwEvLIus8H0.fZfSGW5j6gND/el4URaLV/bEbO'),(6,'admin4','admin4','admin4@admin.com','$2b$12$CoSHCLH/vgoXmWq1C74unOuO.MMPPg/ovtg435gCOogOPg7LI2.e2');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-24 21:23:40
