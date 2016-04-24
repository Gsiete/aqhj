-- MySQL dump 10.13  Distrib 5.6.30, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: aqhj
-- ------------------------------------------------------
-- Server version	5.6.30-0ubuntu0.15.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add tournament',1,'add_tournament'),(2,'Can change tournament',1,'change_tournament'),(3,'Can delete tournament',1,'delete_tournament'),(4,'Can add stadium',2,'add_stadium'),(5,'Can change stadium',2,'change_stadium'),(6,'Can delete stadium',2,'delete_stadium'),(7,'Can add team',3,'add_team'),(8,'Can change team',3,'change_team'),(9,'Can delete team',3,'delete_team'),(10,'Can add match',4,'add_match'),(11,'Can change match',4,'change_match'),(12,'Can delete match',4,'delete_match'),(13,'Can add log entry',5,'add_logentry'),(14,'Can change log entry',5,'change_logentry'),(15,'Can delete log entry',5,'delete_logentry'),(16,'Can add permission',6,'add_permission'),(17,'Can change permission',6,'change_permission'),(18,'Can delete permission',6,'delete_permission'),(19,'Can add group',7,'add_group'),(20,'Can change group',7,'change_group'),(21,'Can delete group',7,'delete_group'),(22,'Can add user',8,'add_user'),(23,'Can change user',8,'change_user'),(24,'Can delete user',8,'delete_user'),(25,'Can add content type',9,'add_contenttype'),(26,'Can change content type',9,'change_contenttype'),(27,'Can delete content type',9,'delete_contenttype'),(28,'Can add session',10,'add_session'),(29,'Can change session',10,'change_session'),(30,'Can delete session',10,'delete_session'),(31,'Can add country',11,'add_country'),(32,'Can change country',11,'change_country'),(33,'Can delete country',11,'delete_country'),(34,'Can add region/state',12,'add_region'),(35,'Can change region/state',12,'change_region'),(36,'Can delete region/state',12,'delete_region'),(37,'Can add city',13,'add_city'),(38,'Can change city',13,'change_city'),(39,'Can delete city',13,'delete_city');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$a9yItqung6Hq$m0y06v3cWumITViZa4OqRK2UdMnXeAoM+HxnRZb62OQ=','2016-04-19 20:41:58.573301',1,'admin','','','gpoussif@gmail.com',1,1,'2016-04-03 11:50:26.269303');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities_light_city`
--

DROP TABLE IF EXISTS `cities_light_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities_light_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `alternate_names` longtext,
  `name` varchar(200) NOT NULL,
  `display_name` varchar(200) NOT NULL,
  `search_names` longtext NOT NULL,
  `latitude` decimal(8,5) DEFAULT NULL,
  `longitude` decimal(8,5) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  `population` bigint(20) DEFAULT NULL,
  `feature_code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `geoname_id` (`geoname_id`),
  UNIQUE KEY `cities_light_city_region_id_29b81cd4_uniq` (`region_id`,`name`),
  UNIQUE KEY `cities_light_city_region_id_dc18c213_uniq` (`region_id`,`slug`),
  KEY `cities_light_city_country_id_cf310fd2_fk_cities_light_country_id` (`country_id`),
  KEY `cities_light_city_d7397f31` (`name_ascii`),
  KEY `cities_light_city_2dbcba41` (`slug`),
  KEY `cities_light_city_b068931c` (`name`),
  KEY `cities_light_city_248081ec` (`population`),
  KEY `cities_light_city_3f98884f` (`feature_code`),
  CONSTRAINT `cities_light_city_country_id_cf310fd2_fk_cities_light_country_id` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`),
  CONSTRAINT `cities_light_city_region_id_f7ab977b_fk_cities_light_region_id` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_city`
--

LOCK TABLES `cities_light_city` WRITE;
/*!40000 ALTER TABLE `cities_light_city` DISABLE KEYS */;
/*!40000 ALTER TABLE `cities_light_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities_light_country`
--

DROP TABLE IF EXISTS `cities_light_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities_light_country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `alternate_names` longtext,
  `name` varchar(200) NOT NULL,
  `code2` varchar(2) DEFAULT NULL,
  `code3` varchar(3) DEFAULT NULL,
  `continent` varchar(2) NOT NULL,
  `tld` varchar(5) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `geoname_id` (`geoname_id`),
  UNIQUE KEY `code2` (`code2`),
  UNIQUE KEY `code3` (`code3`),
  KEY `cities_light_country_d7397f31` (`name_ascii`),
  KEY `cities_light_country_2dbcba41` (`slug`),
  KEY `cities_light_country_0e20e84e` (`continent`),
  KEY `cities_light_country_a311df50` (`tld`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_country`
--

LOCK TABLES `cities_light_country` WRITE;
/*!40000 ALTER TABLE `cities_light_country` DISABLE KEYS */;
/*!40000 ALTER TABLE `cities_light_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities_light_region`
--

DROP TABLE IF EXISTS `cities_light_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities_light_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `alternate_names` longtext,
  `name` varchar(200) NOT NULL,
  `display_name` varchar(200) NOT NULL,
  `geoname_code` varchar(50) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cities_light_region_country_id_6e5b3799_uniq` (`country_id`,`name`),
  UNIQUE KEY `cities_light_region_country_id_3dd02103_uniq` (`country_id`,`slug`),
  UNIQUE KEY `geoname_id` (`geoname_id`),
  KEY `cities_light_region_d7397f31` (`name_ascii`),
  KEY `cities_light_region_2dbcba41` (`slug`),
  KEY `cities_light_region_b068931c` (`name`),
  KEY `cities_light_region_eb02a700` (`geoname_code`),
  CONSTRAINT `cities_light_regi_country_id_b2782d49_fk_cities_light_country_id` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_region`
--

LOCK TABLES `cities_light_region` WRITE;
/*!40000 ALTER TABLE `cities_light_region` DISABLE KEYS */;
/*!40000 ALTER TABLE `cities_light_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-04-03 14:26:11.438848','1','Tournament object',1,'Added.',1,1),(2,'2016-04-03 14:30:05.020039','1','MainStadium',1,'Added.',2,1),(3,'2016-04-03 14:37:37.923240','1','Main Team',1,'Added.',3,1),(4,'2016-04-03 14:37:57.020284','2','Stadium 2',1,'Added.',2,1),(5,'2016-04-03 14:38:11.551149','2','Team 2',1,'Added.',3,1),(6,'2016-04-03 14:38:45.101842','3','Stadium 3',1,'Added.',2,1),(7,'2016-04-03 14:38:49.062548','3','Team 3',1,'Added.',3,1),(8,'2016-04-03 14:39:38.782536','1','Match object',1,'Added.',4,1),(9,'2016-04-03 14:40:39.228909','2','Match object',1,'Added.',4,1),(10,'2016-04-03 18:42:17.872788','3','Main Team - Team 3 (2016-04-03 20:42:12+02:00)',1,'Added.',4,1),(11,'2016-04-03 18:44:26.801438','4','Main Team - Main Team (2016-04-24 20:44:22+02:00)',1,'Added.',4,1),(12,'2016-04-04 19:50:06.265726','3','Stadium 3',2,'Changed timezone.',2,1),(13,'2016-04-04 19:54:36.762557','3','Stadium 3',2,'Changed timezone.',2,1),(14,'2016-04-19 21:20:56.415553','1','Main Team - Team 2 (2016-04-27 01:39:29+02:00)',2,'Changed time.',4,1),(15,'2016-04-19 21:21:09.583420','2','Main Team - Team 2 (2016-05-01 16:40:27+02:00)',2,'Changed time.',4,1),(16,'2016-04-19 21:21:21.749325','3','Main Team - Team 3 (2016-05-07 20:42:12+02:00)',2,'Changed time.',4,1),(17,'2016-04-19 21:41:12.930722','1','Main Team - Team 2 (2016-04-20 01:39:29+02:00)',2,'Changed time.',4,1),(18,'2016-04-19 21:46:58.160146','2','Main Team - Team 2 (2016-04-20 23:47:42+02:00)',2,'Changed time.',4,1),(19,'2016-04-19 21:48:18.187839','2','Main Team - Team 2 (2016-04-20 23:49:42+02:00)',2,'Changed time.',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (5,'admin','logentry'),(7,'auth','group'),(6,'auth','permission'),(8,'auth','user'),(13,'cities','city'),(11,'cities','country'),(12,'cities','region'),(9,'contenttypes','contenttype'),(4,'main','match'),(2,'main','stadium'),(3,'main','team'),(1,'main','tournament'),(10,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-04-03 11:26:25.339148'),(2,'auth','0001_initial','2016-04-03 11:26:40.983839'),(3,'admin','0001_initial','2016-04-03 11:26:43.512095'),(4,'admin','0002_logentry_remove_auto_add','2016-04-03 11:26:43.713404'),(5,'contenttypes','0002_remove_content_type_name','2016-04-03 11:26:45.581842'),(6,'auth','0002_alter_permission_name_max_length','2016-04-03 11:26:46.504947'),(7,'auth','0003_alter_user_email_max_length','2016-04-03 11:26:47.597432'),(8,'auth','0004_alter_user_username_opts','2016-04-03 11:26:47.673864'),(9,'auth','0005_alter_user_last_login_null','2016-04-03 11:26:48.440956'),(10,'auth','0006_require_contenttypes_0002','2016-04-03 11:26:48.499025'),(11,'auth','0007_alter_validators_add_error_messages','2016-04-03 11:26:48.569782'),(12,'main','0001_initial','2016-04-03 11:27:00.442038'),(13,'sessions','0001_initial','2016-04-03 11:27:01.254900'),(14,'main','0002_auto_20160403_1435','2016-04-03 14:35:18.844038'),(15,'main','0003_auto_20160404_0053','2016-04-03 22:53:57.206409'),(16,'main','0004_auto_20160404_2211','2016-04-04 20:11:50.419125'),(17,'cities_light','0001_initial','2016-04-22 20:48:01.114604'),(18,'cities_light','0002_city','2016-04-22 20:48:08.668736'),(19,'cities_light','0003_auto_20141120_0342','2016-04-22 20:48:08.799251'),(20,'cities_light','0004_autoslug_update','2016-04-22 20:48:08.986234'),(21,'cities_light','0005_blank_phone','2016-04-22 20:48:09.143397'),(22,'cities_light','0006_compensate_for_0003_bytestring_bug','2016-04-22 20:48:09.187669');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gwum9cym79yx8da7be9g2hqu0ah7h4xw','NWUzYWIzYWIwODQxYzhkZDZjNjZlMGU4MjRlZDY5ZDNjYWFiNzE1ODp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk4Njg1NzY3NzYyNDY1ZjUxZTc5YzlkMjZmNGE5YzViZWQzMTcyNTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-04-17 11:50:54.226615'),('wo2ydeld0lgsca7omt7y65mc44va6yqk','ZDdjYjM4MjlhNjE5YzA0ZGUwNTc5M2I3MjBkMzA3YzRhYmM3NjExNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiI5ODY4NTc2Nzc2MjQ2NWY1MWU3OWM5ZDI2ZjRhOWM1YmVkMzE3MjU0In0=','2016-05-03 20:41:58.695822');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_match`
--

DROP TABLE IF EXISTS `main_match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_match` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime(6) NOT NULL,
  `stadium_id` int(11),
  `team_a_id` int(11) NOT NULL,
  `team_b_id` int(11) NOT NULL,
  `tournament_id` int(11),
  PRIMARY KEY (`id`),
  KEY `main_match_5c1e67db` (`stadium_id`),
  KEY `main_match_d6765f71` (`team_a_id`),
  KEY `main_match_a9875406` (`team_b_id`),
  KEY `main_match_656a3fdb` (`tournament_id`),
  CONSTRAINT `main_match_stadium_id_a5dfb3cb_fk_main_stadium_id` FOREIGN KEY (`stadium_id`) REFERENCES `main_stadium` (`id`),
  CONSTRAINT `main_match_team_a_id_f42468f6_fk_main_team_id` FOREIGN KEY (`team_a_id`) REFERENCES `main_team` (`id`),
  CONSTRAINT `main_match_team_b_id_746457ad_fk_main_team_id` FOREIGN KEY (`team_b_id`) REFERENCES `main_team` (`id`),
  CONSTRAINT `main_match_tournament_id_73ccc317_fk_main_tournament_id` FOREIGN KEY (`tournament_id`) REFERENCES `main_tournament` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_match`
--

LOCK TABLES `main_match` WRITE;
/*!40000 ALTER TABLE `main_match` DISABLE KEYS */;
INSERT INTO `main_match` VALUES (1,'2016-04-19 23:39:29.000000',1,1,2,1),(2,'2016-04-20 21:49:42.000000',2,1,2,1),(3,'2016-05-07 18:42:12.000000',1,1,3,1),(4,'2016-04-24 18:44:22.000000',3,1,1,1);
/*!40000 ALTER TABLE `main_match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_stadium`
--

DROP TABLE IF EXISTS `main_stadium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_stadium` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `timezone` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_stadium`
--

LOCK TABLES `main_stadium` WRITE;
/*!40000 ALTER TABLE `main_stadium` DISABLE KEYS */;
INSERT INTO `main_stadium` VALUES (1,'MainStadium','Europe/Berlin'),(2,'Stadium 2','Europe/Berlin'),(3,'Stadium 3','America/Argentina/Buenos_Aires');
/*!40000 ALTER TABLE `main_stadium` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_team`
--

DROP TABLE IF EXISTS `main_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `is_domain_team` tinyint(1) NOT NULL,
  `stadium_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_team_stadium_id_5fd2f9b8_fk_main_stadium_id` (`stadium_id`),
  KEY `main_team_slug_6003d6f5_uniq` (`slug`),
  CONSTRAINT `main_team_stadium_id_5fd2f9b8_fk_main_stadium_id` FOREIGN KEY (`stadium_id`) REFERENCES `main_stadium` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_team`
--

LOCK TABLES `main_team` WRITE;
/*!40000 ALTER TABLE `main_team` DISABLE KEYS */;
INSERT INTO `main_team` VALUES (1,'Main Team','main-team',1,1),(2,'Team 2','team-2',0,2),(3,'Team 3','team-3',0,3);
/*!40000 ALTER TABLE `main_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_tournament`
--

DROP TABLE IF EXISTS `main_tournament`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_tournament` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_tournament_2dbcba41` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_tournament`
--

LOCK TABLES `main_tournament` WRITE;
/*!40000 ALTER TABLE `main_tournament` DISABLE KEYS */;
INSERT INTO `main_tournament` VALUES (1,'A tournament','2016-04-03 14:26:00.000000','2016-04-03 14:26:04.000000','');
/*!40000 ALTER TABLE `main_tournament` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-22 22:48:37
