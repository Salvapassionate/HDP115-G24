'use strict'
const { faker } = require('@faker-js/faker')
/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        /**
         * Agregue comandos semilla aquí.                  
         */
        let my_app_usuarios = []
        const niveles = ['verde', 'amarilla', 'roja']
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id:1, 
                nombreUb:'Simana Metrocentro ', 
                departamento:'San Salvador', 
                municipio: 'San Salvador',
                coordenadaX: 'San Salvador', 
                coodenadaY: '13.705334',
                
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 2,
                nombreUb: 'Súper Selectos Centro Comercial San Luis',
                departamento: 'San Salvador',
                municipio: 'San Salvador',
                coodenadaX: 13.716191,
                coodenadaX: 13.716191,
                coodenadaY: -89.212591
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 3,
                nombreUb: 'Diparvel Escalón',
                departamento: 'San Salvador',
                municipio: 'San Salvador',
                coodenadaY: 13.699858,
                coodenadaX: -89.233339
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 4,
                nombreUb: 'Texaco La 25',
                municipio: 'San Salvador',
                departamento: 'San Salvador',
                coodenadaY: 13.703994,
                coodenadaX: -89.204689
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 5,
                nombreUb: 'Siman Galerías',
                municipio: 'San Salvador',
                coordenadaX: 'San Salvador',
                coodenadaY: 13.701678,
                coodenadaZ: -89.230029
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 6,
                nombreUb: 'Súper Selectos Aguilares',
                municipio: 'San Salvador',
                coordenadaX: 'Aguilares',
                coodenadaY: 13.960177,
                coodenadaZ: -89.183403
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 7,
                nombreUb: 'Diparvel Pedregal',
                municipio: 'La Libertad',
                coordenadaX: 'Ciudad Delgado',
                coodenadaY: 13.678266,
                coodenadaZ: -89.256385
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 8,
                nombreUb: 'Texaco Centroamerica',
                municipio: 'San Salvador',
                coordenadaX: 'Cuscatlan',
                coodenadaY: 13.707750,
                coodenadaZ: -89.204821
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 9,
                nombreUb: 'Siman La Gran Vía',
                municipio: 'San Salvador',
                coordenadaX: 'La Gran Vía',
                coodenadaY: 13.677944,
                coodenadaZ: -89.252997
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 10,
                nombreUb: 'Super Selectos Ahuachapán',
                municipio: 'Ahuchapan',
                coordenadaX: 'Sonsonate',
                coodenadaY: 13.924510,
                coodenadaZ: -89.843417
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 11,
                nombreUb: 'Diparvel Venezuela',
                municipio: 'San Salvador',
                coordenadaX: 'San Salvador',
                coodenadaY: 13.699836,
                coodenadaZ: -89.233324
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 12,
                nombreUb: 'Texaco Santa Elena',
                municipio: 'La Libertad',
                coordenadaX: 'Cuscatlan',
                coodenadaY: 13.665812,
                coodenadaZ: -89.264347
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 13,
                nombreUb: 'Siman Plaza Mundo',
                municipio: 'San Salvador',
                coordenadaX: 'Soyapango',
                coodenadaY: 13.698900,
                coodenadaZ: -89.152328
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 14,
                nombreUb: 'Super Selectos Apopa Pericentro',
                municipio: 'San Salvador',
                coordenadaX: 'Apopa',
                coodenadaY: 13.794251,
                coodenadaZ: -89.177950
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 15,
                nombreUb: 'Divarpel 27 avenida sur',
                municipio: 'San Salvador',
                coordenadaX: 'San Salvador',
                coodenadaY: 13.694566,
                coodenadaZ: -89.205438
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 16,
                nombreUb: 'Texaco Caribe',
                municipio: 'San Salvador',
                coordenadaX: 'San Salvador',
                coodenadaY: 13.700741,
                coodenadaZ: -89.225104
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 17,
                nombreUb: 'Siman Santa Ana',
                municipio: 'Santa Ana',
                coordenadaX: 'Santa Ana',
                coodenadaY: 13.976942,
                coodenadaZ: -89.561220
            },
        ]
        my_app_usuarios = [
            ...my_app_usuarios,
            {
                id: 18,
                nombreUb: 'Super Selectos Apopa Periplaza',
                municipio: 'San Salvador',
                coordenadaX: 'Apopa',
                coodenadaY: 13.791434,
                coodenadaZ: -89.174108
            },
        ]

        await queryInterface.bulkInsert('Alerta', alerta, {})
        
    },
    async down(queryInterface, Sequelize) {
        /**
         * Agregue comandos para revertir la semilla aquí.
         *
         * Ejemplo:
         * await queryInterface.bulkDelete('People', null, {});
         */
    },
}
