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
  empresas.init({
    nombreE: DataTypes.STRING,
    direcciónE: DataTypes.STRING,
    correoE: DataTypes.STRING,
    teléfonoE: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'empresas',
  });
  return empresas;
};