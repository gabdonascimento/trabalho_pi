CREATE TABLE `provas`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(64) NOT NULL,
    `corrida_pontuacao` INT NOT NULL,
    `corrida_posicao` INT NOT NULL,
    `valor` DECIMAL(8, 2) NOT NULL,
    `valor_descricao` VARCHAR(64) NOT NULL,
    `penalidade` DECIMAL(8, 2) NULL,
    `penalty_description` VARCHAR(64) NULL,
    `penalidade_descricao` INT NOT NULL,
    `equipe_id` INT UNSIGNED NOT NULL
);
CREATE TABLE `equipes`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(64) NOT NULL,
    `nota` INT,
    `carro_id` VARCHAR(32) NOT NULL
);
CREATE TABLE `estudantes`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(64) NOT NULL,
    `RA` VARCHAR(10) NOT NULL,
    `equipe_id` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `estudantes` ADD CONSTRAINT `estudantes_equipe_id_foreign` FOREIGN KEY(`equipe_id`) REFERENCES `equipes`(`id`);
ALTER TABLE
    `provas` ADD CONSTRAINT `provas_equipe_id_foreign` FOREIGN KEY(`equipe_id`) REFERENCES `equipes`(`id`);