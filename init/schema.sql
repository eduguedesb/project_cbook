CREATE TABLE `tb_dados` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefone` varchar(18) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `descricao` longtext NOT NULL,
  `categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `tb_categorias` (
  `id_categoria` int(11) NOT NULL,
  `nome_categoria` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
