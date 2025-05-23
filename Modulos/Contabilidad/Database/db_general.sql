-- MySQL Script generated by MySQL Workbench
-- Sat Apr 19 09:32:16 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Proveedor` (
  `idProveedor` INT NOT NULL AUTO_INCREMENT,
  `nombre_proveedor` VARCHAR(100) NOT NULL,
  `contacto` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(20) NOT NULL,
  `correo electronico` VARCHAR(100) NOT NULL,
  `direccion` TEXT NOT NULL,
  PRIMARY KEY (`idProveedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Compras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Compras` (
  `idCompras` INT NOT NULL AUTO_INCREMENT,
  `idProveedor` INT NOT NULL,
  `fecha_compra` DATE NOT NULL,
  `total` DECIMAL(15,2) NOT NULL,
  `estado_compra` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCompras`),
  INDEX `idProveedor_idx` (`idProveedor` ASC) VISIBLE,
  CONSTRAINT `idProveedor`
    FOREIGN KEY (`idProveedor`)
    REFERENCES `mydb`.`Proveedor` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cuentas_por_pagar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cuentas_por_pagar` (
  `idCuentas_por_pagar` INT NOT NULL,
  `idProveedor` INT NOT NULL,
  `fecha_factura` DATE NOT NULL,
  `monto_total` DECIMAL(15,2) NOT NULL,
  `fecha_vencimiento` DATE NOT NULL,
  `estado_pago` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCuentas_por_pagar`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CuentasPorPagar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CuentasPorPagar` (
  `idCuentasPorPagar` INT NOT NULL,
  `idProveedor` INT NOT NULL,
  `fecha_factura` DATE NOT NULL,
  `monto_total` DECIMAL(15,2) NOT NULL,
  `fecha_vencimiento` DATE NOT NULL,
  `estado_pago` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCuentasPorPagar`),
  INDEX `idProveedor_idx` (`idProveedor` ASC) VISIBLE,
  CONSTRAINT `idProveedor`
    FOREIGN KEY (`idProveedor`)
    REFERENCES `mydb`.`Proveedor` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cliente` (
  `idCliente` INT NOT NULL,
  `nombre_cliente` VARCHAR(40) NOT NULL,
  `apellido_cliente` VARCHAR(40) NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(20) NULL,
  `direccion` TEXT NOT NULL,
  `Tipo_cliente` VARCHAR(45) NOT NULL,
  `fecha_registro` DATE NOT NULL,
  `estado_cliente` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CuentasPorCobrar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CuentasPorCobrar` (
  `idCuentasPorCobrar` INT NOT NULL,
  `idCliente` INT NOT NULL,
  `fecha_factura` DATE NOT NULL,
  `monto_total` DECIMAL(15,2) NOT NULL,
  `fecha_vencimiento` DATE NOT NULL,
  `estado_cobro` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCuentasPorCobrar`),
  INDEX `idCliente_idx` (`idCliente` ASC) VISIBLE,
  CONSTRAINT `idCliente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `mydb`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`LibroMayor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`LibroMayor` (
  `idAsiento` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `Descripcion` VARCHAR(300) NOT NULL,
  `cuenta_debito` VARCHAR(100) NOT NULL,
  `cuenta_credito` VARCHAR(100) NOT NULL,
  `monto` DECIMAL(15,2) NOT NULL,
  `referencia_transaccion` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idAsiento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ActivosFijos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ActivosFijos` (
  `idActivosFijos` INT NOT NULL,
  `nombre_activo` VARCHAR(100) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `fecha_adquisicion` DATE NOT NULL,
  `valor_compra` DECIMAL(15,2) NOT NULL,
  `valor_residual` DECIMAL(15,2) NOT NULL,
  `vida_util-years` INT NULL,
  `metodo_depreciacion` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idActivosFijos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`GestionImpuestos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`GestionImpuestos` (
  `idImpuesto` INT NOT NULL AUTO_INCREMENT,
  `tipo_impuesto` VARCHAR(100) NOT NULL,
  `tasa` DECIMAL(5,2) NULL,
  `fecha_aplicacion` DATE NOT NULL,
  PRIMARY KEY (`idImpuesto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SeguimientoGanancias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SeguimientoGanancias` (
  `idGanancias` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `ingresos` DECIMAL(15,2) NOT NULL,
  `costos` DECIMAL(15,2) NOT NULL,
  `ganancias` DECIMAL(15,2) NULL,
  PRIMARY KEY (`idGanancias`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`InformeFinanciero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`InformeFinanciero` (
  `idInformeFinanciero` INT NOT NULL,
  `nombre_reporte` VARCHAR(100) NOT NULL,
  `periodo_inicio` DATE NOT NULL,
  `periodo fin` DATE NOT NULL,
  `tipo_reporte` VARCHAR(65) NOT NULL,
  `fecha_generacion` DATE NOT NULL,
  PRIMARY KEY (`idInformeFinanciero`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`GestionRiesgos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`GestionRiesgos` (
  `idGestionRiesgos` INT NOT NULL,
  `tipo_riesgo` VARCHAR(100) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `nivel_riesgo` VARCHAR(45) NOT NULL,
  `fecha_identificacion` DATE NOT NULL,
  `estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idGestionRiesgos`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
