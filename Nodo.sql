-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 30-11-2024 a las 07:59:49
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grafos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Nodo`
--

CREATE TABLE `Nodo` (
  `id_nodo` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Nodo`
--

INSERT INTO `Nodo` (`id_nodo`, `nombre`) VALUES
(0, 'Manizales'),
(1, 'Pereira'),
(2, 'Armenia'),
(3, 'Chinchina'),
(4, 'Villamaria'),
(5, 'Palestina'),
(6, 'Neira'),
(7, 'La Virginia'),
(8, 'Dosquebradas'),
(9, 'Santa Rosa de Cabal'),
(10, 'Cartago'),
(11, 'Calarca'),
(12, 'Ciscasia'),
(13, 'La Tebaida'),
(14, 'Montenegro');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Nodo`
--
ALTER TABLE `Nodo`
  ADD PRIMARY KEY (`id_nodo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
