-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1
-- Время создания: Июн 17 2020 г., 17:06
-- Версия сервера: 5.5.25
-- Версия PHP: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `professional_standard`
--

-- --------------------------------------------------------

--
-- Структура таблицы `education`
--

CREATE TABLE IF NOT EXISTS `education` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='Требования к образованию к трудовым функциям' AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `education`
--

INSERT INTO `education` (`id`, `name`) VALUES
(1, 'бакалавриат'),
(2, 'магистратура');

-- --------------------------------------------------------

--
-- Структура таблицы `education_requirement`
--

CREATE TABLE IF NOT EXISTS `education_requirement` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `id_function` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Требования к образованию к трудовым функциям' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `experience`
--

CREATE TABLE IF NOT EXISTS `experience` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `id_function` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Требования к опыту работы' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `fses`
--

CREATE TABLE IF NOT EXISTS `fses` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_direction` int(10) DEFAULT NULL,
  `id_education` int(10) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='Федеральные государственные образовательные стандарты высшего образования' AUTO_INCREMENT=5 ;

--
-- Дамп данных таблицы `fses`
--

INSERT INTO `fses` (`id`, `id_direction`, `id_education`, `url`) VALUES
(1, 1, 1, 'https://classinform.ru/fgos/09.03.01-informatika-i-vychislitelnaia-tekhnika.html'),
(2, 1, 2, 'https://classinform.ru/fgos/09.04.01-informatika-i-vychislitelnaia-tekhnika.html'),
(3, 2, 1, 'https://classinform.ru/fgos/09.03.04-programmnaia-inzheneriia.html'),
(4, 2, 2, 'https://classinform.ru/fgos/09.04.04-programmnaia-inzheneriia.html');

-- --------------------------------------------------------

--
-- Структура таблицы `labor_action`
--

CREATE TABLE IF NOT EXISTS `labor_action` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'идентификатор',
  `name` varchar(300) DEFAULT NULL COMMENT 'наименование трудовых действий',
  `id_subfunctions` int(10) DEFAULT NULL COMMENT 'идентификатор трудовой подфункии',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `labor_function`
--

CREATE TABLE IF NOT EXISTS `labor_function` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `id_prof_standard` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Обобщенные трудовые функции' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `necessary_knowledge`
--

CREATE TABLE IF NOT EXISTS `necessary_knowledge` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `id_subfunctions` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Необходимые знания' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `necessary_skills`
--

CREATE TABLE IF NOT EXISTS `necessary_skills` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `id_subfunctions` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Необходимые умения' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `prof_standard`
--

CREATE TABLE IF NOT EXISTS `prof_standard` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `activity` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Список профессиональных стандартов' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `standard_direction`
--

CREATE TABLE IF NOT EXISTS `standard_direction` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_fses` int(10) DEFAULT NULL,
  `standard` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `subfunctions`
--

CREATE TABLE IF NOT EXISTS `subfunctions` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `id_function` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Трудовые подфункции' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `training_direction`
--

CREATE TABLE IF NOT EXISTS `training_direction` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `training_direction`
--

INSERT INTO `training_direction` (`id`, `name`) VALUES
(1, 'Информатика и вычислительная техника'),
(2, 'Программная инженерия');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
