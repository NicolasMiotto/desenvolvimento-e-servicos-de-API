use dev_api;

-- drop table `dev_api`.`carros`;

create table `dev_api`.`carros` (
	`oid_carro` BIGINT not null AUTO_INCREMENT,
	`nom_carro` VARCHAR(500) not null ,
	`nom_marca` VARCHAR(500) not null ,
	`num_ano_fabricacao` int not null ,
	`num_ano_modelo` int not null ,
	`nom_cor` int not null ,
	`nom_combustivel` VARCHAR(500) not null ,
	`num_placa` VARCHAR(500) not null ,
	`dat_criacao` DATETIME not null DEFAULT CURRENT_TIMESTAMP,
	`dat_alteracao` DATETIME null,
	primary key (`oid_carro`)
)
-- engine = InnoDB
;