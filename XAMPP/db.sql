
--
-- Database: `db_connect`
--

CREATE DATABASE IF NOT EXISTS `db_connect` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_connect`;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_contact`
--

DROP TABLE IF EXISTS `tbl_contact`;
CREATE TABLE `tbl_contact` (
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_contact`
--

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_contact`
--
