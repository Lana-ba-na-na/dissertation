-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1
-- Время создания: Июн 17 2020 г., 15:38
-- Версия сервера: 5.5.25
-- Версия PHP: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `standard`
--

-- --------------------------------------------------------

--
-- Структура таблицы `activityps_activityvac`
--

CREATE TABLE IF NOT EXISTS `activityps_activityvac` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `standard_activity` varchar(200) NOT NULL,
  `id_prof_activityvac` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- Дамп данных таблицы `activityps_activityvac`
--

INSERT INTO `activityps_activityvac` (`id`, `standard_activity`, `id_prof_activityvac`) VALUES
(1, 'Разработка программного обеспечения', 2),
(2, 'Разработка программного обеспечения', 3),
(3, 'Разработка программного обеспечения', 4),
(4, 'Разработка программного обеспечения', 6),
(5, 'Разработка программного обеспечения', 7),
(6, 'Проектирование, разработка и интеграция информационных ресурсов в локальной сети и информационно-телекоммуникационной сети «Интернет»', 1),
(7, 'Проектирование, разработка и интеграция информационных ресурсов в локальной сети и информационно-телекоммуникационной сети «Интернет»', 6),
(8, 'Проектирование, разработка и интеграция информационных ресурсов в локальной сети и информационно-телекоммуникационной сети «Интернет»', 7),
(9, 'Создание системного программного обеспечения', 5),
(10, 'Создание системного программного обеспечения', 6),
(11, 'Создание системного программного обеспечения', 8);

-- --------------------------------------------------------

--
-- Структура таблицы `activity_language`
--

CREATE TABLE IF NOT EXISTS `activity_language` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_activity` int(10) DEFAULT NULL,
  `id_language` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `education`
--

CREATE TABLE IF NOT EXISTS `education` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

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
-- Структура таблицы `professional_activity`
--

CREATE TABLE IF NOT EXISTS `professional_activity` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- Дамп данных таблицы `professional_activity`
--

INSERT INTO `professional_activity` (`id`, `name`, `url`) VALUES
(1, 'Разработка веб приложений', 'https://scand.com/ru/services/web-application-development/'),
(2, 'Разработка мобильных приложений', 'https://scand.com/ru/services/mobile-app-development/'),
(3, 'Разработка Desktop приложений', 'https://scand.com/ru/services/desktop-custom-software-development/'),
(4, 'Разработка игр', NULL),
(5, 'Разработка системного программного обеспечения', NULL),
(6, 'Система управления базами данных', 'https://ru.wikipedia.org/wiki/Шаблон:СУБД'),
(7, 'Системы управления версиями', 'https://ru.wikipedia.org/wiki/Шаблон:Системы_управления_версиями'),
(8, 'Операционные системы', 'https://ru.wikipedia.org/wiki/Шаблон:Операционные_системы');

-- --------------------------------------------------------

--
-- Структура таблицы `prof_area`
--

CREATE TABLE IF NOT EXISTS `prof_area` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) DEFAULT NULL,
  `url` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=35 ;

--
-- Дамп данных таблицы `prof_area`
--

INSERT INTO `prof_area` (`id`, `name`, `url`) VALUES
(1, 'Образование', '/profstandarty/01-obrazovanie.html'),
(2, 'Здравоохранение', '/profstandarty/02-zdravookhranenie.html'),
(3, 'Социальное обслуживание', '/profstandarty/03-sotcialnoe-obsluzhivanie.html'),
(4, 'Культура, искусство', '/profstandarty/04-kultura-iskusstvo.html'),
(5, 'Физическая культура и спорт', '/profstandarty/05-fizicheskaia-kultura-i-sport.html'),
(6, 'Связь, информационные и коммуникационные технологии', '/profstandarty/06-sviaz-informatcionnye-i-kommunikatcionnye-tekhnologii.html'),
(7, 'Административно-управленческая и офисная деятельность', '/profstandarty/07-administrativno-upravlencheskaia-i-ofisnaia-deiatelnost.html'),
(8, 'Финансы и экономика', '/profstandarty/08-finansy-i-ekonomika.html'),
(9, 'Юриспруденция', '/profstandarty/09-iurisprudentciia.html'),
(10, 'Архитектура, проектирование, геодезия, топография и дизайн', '/profstandarty/10-arhitektura-proektirovanie-geodeziia-topografiia-i-dizain.html'),
(11, 'Средства массовой информации, издательство и полиграфия', '/profstandarty/11-sredstva-massovoi-informatcii-izdatelstvo-i-poligrafiia.html'),
(12, 'Обеспечение безопасности', '/profstandarty/12-obespechenie-bezopasnosti.html'),
(13, 'Сельское хозяйство', '/profstandarty/13-selskoe-hoziaistvo.html'),
(14, 'Лесное хозяйство, охота', '/profstandarty/14-lesnoe-hoziaistvo-ohota.html'),
(15, 'Рыбоводство и рыболовство', '/profstandarty/15-rybovodstvo-i-rybolovstvo.html'),
(16, 'Строительство и жилищно-коммунальное хозяйство', '/profstandarty/16-stroitelstvo-i-zhilishchno-kommunalnoe-hoziaistvo.html'),
(17, 'Транспорт', '/profstandarty/17-transport.html'),
(18, 'Добыча, переработка угля, руд и других полезных ископаемых', '/profstandarty/18-dobycha-pererabotka-uglia-rud-i-drugikh-poleznykh-iskopaemykh.html'),
(19, 'Добыча, переработка, транспортировка нефти и газа', '/profstandarty/19-dobycha-pererabotka-transportirovka-nefti-i-gaza.html'),
(20, 'Электроэнергетика', '/profstandarty/20-elektroenergetika.html'),
(21, 'Легкая и текстильная промышленность', '/profstandarty/21-legkaia-i-tekstilnaia-promyshlennost.html'),
(22, 'Пищевая промышленность, включая производство напитков и табака', '/profstandarty/22-pishchevaia-promyshlennost-vcliuchaia-proizvodstvo-napitkov-i-tabaka.html'),
(23, 'Деревообрабатывающая и целлюлозно-бумажная промышленность, мебельное производство', '/profstandarty/23-derevoobrabatyvaiushchaia-i-tcelliulozno-bumazhnaia-promyshlennost-mebelnoe-proizvodstvo.html'),
(24, 'Атомная промышленность', '/profstandarty/24-atomnaia-promyshlennost.html'),
(25, 'Ракетно-космическая промышленность', '/profstandarty/25-raketno-kosmicheskaia-promyshlennost.html'),
(26, 'Химическое, химико-технологическое производство', '/profstandarty/26-himicheskoe-himiko-tekhnologicheskoe-proizvodstvo.html'),
(27, 'Металлургическое производство', '/profstandarty/27-metallurgicheskoe-proizvodstvo.html'),
(28, 'Производство машин и оборудования', '/profstandarty/28-proizvodstvo-mashin-i-oborudovaniia.html'),
(29, 'Производство электрооборудования, электронного и оптического оборудования', '/profstandarty/29-proizvodstvo-elektrooborudovaniia-elektronnogo-i-opticheskogo-oborudovaniia.html'),
(30, 'Судостроение', '/profstandarty/30-sudostroenie.html'),
(31, 'Автомобилестроение', '/profstandarty/31-avtomobilestroenie.html'),
(32, 'Авиастроение', '/profstandarty/32-aviastroenie.html'),
(33, 'Сервис, оказание услуг населению (торговля, техническое обслуживание, ремонт, предоставление персональных услуг, услуги гостеприимства, общественное питание и пр.)', '/profstandarty/33-servis-okazanie-uslug-naseleniiu.html'),
(34, 'Сквозные виды профессиональной деятельности в промышленности', '/profstandarty/40-skvoznye-vidy-professionalnoi-deiatelnosti-v-promyshlennosti.html');

-- --------------------------------------------------------

--
-- Структура таблицы `prof_standard`
--

CREATE TABLE IF NOT EXISTS `prof_standard` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `activity` varchar(300) DEFAULT NULL,
  `id_prof_area` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Список профессиональных стандартов' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `programming_languages`
--

CREATE TABLE IF NOT EXISTS `programming_languages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Языки программирования' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `skills_activity`
--

CREATE TABLE IF NOT EXISTS `skills_activity` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_activity` int(10) DEFAULT NULL,
  `id_skills` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `skills_vacancy`
--

CREATE TABLE IF NOT EXISTS `skills_vacancy` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `quantity` int(10) DEFAULT NULL,
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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
