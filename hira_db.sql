-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 06, 2021 at 09:27 AM
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
-- Table structure for table `commands_executed`
--

CREATE TABLE `commands_executed` (
  `id` int(11) NOT NULL,
  `command` varchar(30) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(4, 'first', 'living', 'Light', '1'),
(5, 'first', 'living', 'Fan', '0'),
(6, 'first', 'living', 'Lamp', '0'),
(7, 'first', 'living', 'All', '0');

-- --------------------------------------------------------

--
-- Table structure for table `raspi_info`
--

CREATE TABLE `raspi_info` (
  `id` int(6) NOT NULL,
  `temp` float NOT NULL DEFAULT 0,
  `cpu_load` float NOT NULL DEFAULT 0,
  `used_ram` float NOT NULL DEFAULT 0,
  `used_mem` float NOT NULL DEFAULT 0,
  `up_time` varchar(30) NOT NULL DEFAULT '0 m'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `raspi_info`
--

INSERT INTO `raspi_info` (`id`, `temp`, `cpu_load`, `used_ram`, `used_mem`, `up_time`) VALUES
(1, 46.2, 2.5, 36.8, 28.8, '7 m');

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

--
-- Dumping data for table `user_log`
--

INSERT INTO `user_log` (`id`, `user_name`, `ip_address`, `pid`, `log_time`) VALUES
(1, 'pi', '', '22733', '2021-11-03 09:42:05'),
(2, 'pi', '', '24074', '2021-11-03 09:45:13'),
(3, 'pi', '', '25345', '2021-11-03 09:47:39'),
(4, 'pi', '', '26071', '2021-11-03 09:48:27'),
(5, 'pi', '', '26985', '2021-11-03 09:50:18'),
(6, 'pi', '', '28701', '2021-11-03 09:54:04'),
(7, 'pi', '', '32136', '2021-11-03 10:02:04'),
(8, 'pi', '', '2748', '2021-11-03 10:08:43'),
(9, 'pi', '', '3339', '2021-11-03 10:09:38'),
(10, 'pi', '', '5387', '2021-11-03 10:14:03'),
(11, 'pi', '', '6234', '2021-11-03 10:15:41');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `commands_executed`
--
ALTER TABLE `commands_executed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `raspi_info`
--
ALTER TABLE `raspi_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_log`
--
ALTER TABLE `user_log`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `commands_executed`
--
ALTER TABLE `commands_executed`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `user_log`
--
ALTER TABLE `user_log`
  MODIFY `id` int(6) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;