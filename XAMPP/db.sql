
--
-- Database: `db_connect`
--
-- Creates a database if not already created 
CREATE DATABASE IF NOT EXISTS `db_connect` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_connect`;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_contact`
--
--creates the tables 
DROP TABLE IF EXISTS `tbl_contact`;
CREATE TABLE `tbl_contact` (
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

