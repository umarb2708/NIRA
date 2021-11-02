-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 02, 2021 at 12:24 PM
-- Server version: 10.3.31-MariaDB-0+deb10u1
-- PHP Version: 7.3.31-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hira_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `climate_info`
--

CREATE TABLE `climate_info` (
  `id` int(6) NOT NULL,
  `temp` varchar(20) NOT NULL,
  `humidity` varchar(20) NOT NULL,
  `pressure` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `wind` varchar(30) NOT NULL,
  `overall` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `climate_info`
--

INSERT INTO `climate_info` (`id`, `temp`, `humidity`, `pressure`, `place`, `wind`, `overall`) VALUES
(1, '28.9', '81', '1008', 'Thrissur', '2.18', 'Clouds');

-- --------------------------------------------------------

--
-- Table structure for table `commands`
--

CREATE TABLE `commands` (
  `sno` int(6) NOT NULL,
  `main_kw` varchar(50) NOT NULL,
  `action_file` varchar(50) NOT NULL DEFAULT 'action_not_found'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `commands`
--

INSERT INTO `commands` (`sno`, `main_kw`, `action_file`) VALUES
(4, 'turn on', 'automation.turn_on_device'),
(5, 'turn off', 'automation.turn_off_dev'),
(6, 'move forward', 'mov.forward'),
(7, 'training', 'train.train_rex'),
(8, 'wiki', 'wiki.search_in_wiki'),
(9, 'search', 'web.search_from_net');

-- --------------------------------------------------------

--
-- Table structure for table `home_automation`
--

CREATE TABLE `home_automation` (
  `id` int(6) NOT NULL,
  `floor` varchar(30) NOT NULL,
  `plac` varchar(30) NOT NULL,
  `component` varchar(10) NOT NULL DEFAULT 'light',
  `status` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home_automation`
--

INSERT INTO `home_automation` (`id`, `floor`, `plac`, `component`, `status`) VALUES
(4, 'first', 'living', 'Light', '0'),
(5, 'first', 'living', 'Fan', '0'),
(6, 'first', 'living', 'Lamp', '0'),
(7, 'first', 'living', 'All', '0');

-- --------------------------------------------------------

--
-- Table structure for table `raspi_info`
--

CREATE TABLE `raspi_info` (
  `id` int(6) NOT NULL,
  `cpu_load` float DEFAULT 0,
  `tot_ram` varchar(20) DEFAULT '100',
  `used_ram` float DEFAULT NULL,
  `up_time` varchar(50) DEFAULT NULL,
  `tot_mem` varchar(30) DEFAULT '14',
  `used_mem` float DEFAULT NULL,
  `temp` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `raspi_info`
--

INSERT INTO `raspi_info` (`id`, `cpu_load`, `tot_ram`, `used_ram`, `up_time`, `tot_mem`, `used_mem`, `temp`) VALUES
(1, 9.2, '100', 42.7, '2 H, 25 M', '14.0', 4.99, 47.236);

-- --------------------------------------------------------

--
-- Table structure for table `user_log`
--

CREATE TABLE `user_log` (
  `id` int(6) UNSIGNED NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `ip_address` varchar(30) NOT NULL,
  `pid` varchar(20) NOT NULL,
  `log_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
