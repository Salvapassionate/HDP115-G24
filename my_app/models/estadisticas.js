'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class empresas extends Model {
    /**
     * Método auxiliar para definir asociaciones.
     * Este método no forma parte del ciclo de vida de Sequelize.
     * El archivo `models/index` llamará a este método automáticamente.
     */
    static associate(models) {
      // Definir asociación aquí.
      
      this.hasOne(models.Ubicacion, {
        onDelete: 'CASCADE',
        hooks: true,
      })
    }
    
  }
  Estadistica.init({
    
    Nombre: DataTypes.STRING,
    Apellido: DataTypes.STRING,
    Edad: DataTypes.STRING,
    Genero: DataTypes.STRING,
    TipoDeDiscapacidad: DataTypes.STRING,
    Sector: DataTypes.STRING,
    RamaDeActividadEconomica: DataTypes.STRING,
    CategoriaOcupacional: DataTypes.STRING,
  }, {
    sequelize,
    modelName: 'Estadistica',
  });
  return Estadistica;
};