-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 03, 2021 at 12:29 PM
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
  `id` int(1) NOT NULL,
  `command` text NOT NULL,
  `priority` varchar(4) NOT NULL DEFAULT 'low',
  `frm` varchar(30) NOT NULL DEFAULT 'node-red',
  `exec` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `commands`
--

INSERT INTO `commands` (`id`, `command`, `priority`, `frm`, `exec`) VALUES
(79, 'hira turn on the light', 'med', 'hira', 1);

-- --------------------------------------------------------

--
-- Table structure for table `commands_executed`
--

CREATE TABLE `commands_executed` (
  `id` int(11) NOT NULL,
  `command` varchar(30) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `commands_executed`
--

INSERT INTO `commands_executed` (`id`, `command`, `status`) VALUES
(130, 'initialisation', '1'),
(131, 'turn on the light', '1');

-- --------------------------------------------------------

--
-- Table structure for table `command_centre`
--

CREATE TABLE `command_centre` (
  `sno` int(6) NOT NULL,
  `main_kw` varchar(50) NOT NULL,
  `action_file` varchar(50) NOT NULL DEFAULT 'action_not_found',
  `keywords` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `command_centre`
--

INSERT INTO `command_centre` (`sno`, `main_kw`, `action_file`, `keywords`) VALUES
(4, 'turn on', 'aut.turn_on_device', ''),
(5, 'turn off', 'aut.turn_off_device', ''),
(6, 'move forward', 'mov.forward', ''),
(7, 'training', 'train.train_rex', ''),
(8, 'wiki', 'wiki.search_in_wiki', ''),
(9, 'search', 'web.search_from_net', ''),
(10, 'open youtube', 'yt.open_youtube', ''),
(11, 'close youtube', 'yt.close_youtube', ''),
(12, 'change colour', 'aut.change_colour', 'change,red,blue,green'),
(13, 'email', 'mail.send_email', 'send,to,mail,'),
(14, 'play', 'mdc.play_pause', ''),
(15, 'pause', 'mdc.play_pause', ''),
(16, 'play next', 'mdc.next', ''),
(17, 'paly previous', 'mdc.previous', ''),
(18, 'stop media', 'mdc.stop', ''),
(19, 'weather today', 'wth.weather_info', '');

-- --------------------------------------------------------

--
-- Table structure for table `configuration`
--

CREATE TABLE `configuration` (
  `id` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  `test_en` int(11) NOT NULL DEFAULT 0,
  `input_mode` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` text NOT NULL,
  `Address` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone`, `email`, `Address`) VALUES
(1, 'umar', '7034221248', 'umarthottathil1996@gmail.com', 'Thottathil, Maleshamangalam, Thrissur'),
(2, 'sumayya', '9074345928', 'sumayyasamad64@gmail.com', 'manaladi');

-- --------------------------------------------------------

--
-- Table structure for table `hira_info`
--

CREATE TABLE `hira_info` (
  `id` int(11) NOT NULL,
  `pid` varchar(30) NOT NULL DEFAULT '0',
  `tty` varchar(30) NOT NULL DEFAULT '0',
  `status` int(1) NOT NULL DEFAULT 0,
  `init` int(1) NOT NULL DEFAULT 0,
  `adb` int(11) NOT NULL DEFAULT 0,
  `sleep` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hira_info`
--

INSERT INTO `hira_info` (`id`, `pid`, `tty`, `status`, `init`, `adb`, `sleep`) VALUES
(1, '0', 'pts/0', 0, 0, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `home_automation`
--

CREATE TABLE `home_automation` (
  `id` int(6) NOT NULL,
  `room_id` int(5) NOT NULL,
  `floor` varchar(30) NOT NULL,
  `plac` varchar(30) NOT NULL,
  `component` varchar(10) NOT NULL DEFAULT 'light',
  `status` tinyint(1) NOT NULL,
  `param` int(2) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home_automation`
--

INSERT INTO `home_automation` (`id`, `room_id`, `floor`, `plac`, `component`, `status`, `param`) VALUES
(4, 0, 'first', 'living', 'Light', 1, 0),
(5, 0, 'first', 'living', 'Fan', 0, 0),
(6, 0, 'first', 'living', 'Lamp', 0, 1),
(7, 0, 'first', 'living', 'All', 1, 1);

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
  `up_time` varchar(30) NOT NULL DEFAULT '0 m',
  `connection` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `raspi_info`
--

INSERT INTO `raspi_info` (`id`, `temp`, `cpu_load`, `used_ram`, `used_mem`, `up_time`, `connection`) VALUES
(1, 47.2, 5.8, 42.7, 30.2, '9 m', 1);

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
(11, 'pi', '', '6234', '2021-11-03 10:15:41'),
(12, 'pi', '', '15476', '2021-11-06 09:50:44'),
(13, 'pi', '', '16380', '2021-11-06 09:52:17'),
(14, 'pi', '', '6212', '2021-11-11 06:23:02'),
(15, 'pi', '', '3378', '2021-11-12 15:45:43'),
(16, 'pi', '', '27180', '2021-11-15 14:47:44'),
(17, 'pi', '', '7827', '2021-11-15 15:06:22'),
(18, 'pi', '', '11960', '2021-11-16 17:03:20'),
(19, 'pi', '', '13380', '2021-11-16 17:05:28'),
(20, 'pi', '', '30826', '2021-11-16 18:31:05'),
(21, 'pi', '', '4196', '2021-11-17 16:18:01'),
(22, 'pi', '', '21626', '2021-11-17 16:47:07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `commands`
--
ALTER TABLE `commands`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `commands_executed`
--
ALTER TABLE `commands_executed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `command_centre`
--
ALTER TABLE `command_centre`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `configuration`
--
ALTER TABLE `configuration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `hira_info`
--
ALTER TABLE `hira_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_automation`
--
ALTER TABLE `home_automation`
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
-- AUTO_INCREMENT for table `commands`
--
ALTER TABLE `commands`
  MODIFY `id` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;
--
-- AUTO_INCREMENT for table `commands_executed`
--
ALTER TABLE `commands_executed`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=132;
--
-- AUTO_INCREMENT for table `command_centre`
--
ALTER TABLE `command_centre`
  MODIFY `sno` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `configuration`
--
ALTER TABLE `configuration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `hira_info`
--
ALTER TABLE `hira_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `user_log`
--
ALTER TABLE `user_log`
  MODIFY `id` int(6) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
