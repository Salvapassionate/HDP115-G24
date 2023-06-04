'use strict'
const { faker } = require('@faker-js/faker')
/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        /**
         * Agregue comandos semilla aquí.                  
         */
        let Estadistica = []
        const niveles = ['verde', 'amarilla', 'roja']
        Estadistica = [
            ...Estadistica,
            {
                id: 1,
                Nombre:'Gabriel',
                Apellido: 'Rodríguez',
                Edad: '20',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Visual',
                Sector: 'Agricultura',
                RamaDeActividadEconomica: 'Información y comunicaciones',
                CategoriaOcupacional: 'Control de calidad',
            },
        ]
        
        Estadistica = [
            ...Estadistica,
            {
                id: 2,
                Nombre:'Sofía',
                Apellido: 'García',
                Edad: '25',
                Genero: 'Femenino',
                TipoDeDiscapacidad: 'Habla y del lenguaje',
                Sector: 'Industria',
                RamaDeActividadEconomica: 'Industria manufacturera',
                CategoriaOcupacional: 'Operadora de máquina',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 3,
                Nombre:'Mateo',
                Apellido: 'Martínez',
                Edad: '18',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'psicosocial',
                Sector: 'Industria',
                RamaDeActividadEconomica: 'Construcción',
                CategoriaOcupacional: 'Ingeniero civil',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 4,
                Nombre:'Valentina',
                Apellido: 'Gonzáles',
                Edad: '23',
                Genero: 'Femenino',
                TipoDeDiscapacidad: 'Física',
                Sector: 'Comercio',
                RamaDeActividadEconomica: 'Enseñanza',
                CategoriaOcupacional: 'Profesora de Economía',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 5,
                Nombre:'Sebastían',
                Apellido: 'Hernández',
                Edad: '30',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Invisible',
                Sector: 'Servicios',
                RamaDeActividadEconomica: 'Información y comunicaciones',
                CategoriaOcupacional: 'Tele-operador',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 6,
                Nombre:'Isabella',
                Apellido: 'Lopéz',
                Edad: '40',
                Genero: 'Femenino',
                TipoDeDiscapacidad: 'Del Desarrollo',
                Sector: 'Comercio',
                RamaDeActividadEconomica: 'Comercio al por mayor y al por menor y reparación de vehículos automotores',
                CategoriaOcupacional: 'Vendedor',
            },
        ]        

        Estadistica = [
            ...Estadistica,
            {
                id: 7,
                Nombre:'Diego',
                Apellido: 'Peréz',
                Edad: '19',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Intelectual',
                Sector: 'Industria',
                RamaDeActividadEconomica: 'Transporte y almacenamiento',
                CategoriaOcupacional: 'Conductor',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 8,
                Nombre:'Camila',
                Apellido: 'Sanchéz',
                Edad: '24',
                Genero: 'Femenino',
                TipoDeDiscapacidad: 'Visual',
                Sector: 'Agricultura',
                RamaDeActividadEconomica: 'Administración pública',
                CategoriaOcupacional: 'Administradora',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 9,
                Nombre:'Alejandro',
                Apellido: 'Ramiréz',
                Edad: '20',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Física',
                Sector: 'Agricultura',
                RamaDeActividadEconomica: 'Alojamiento y servicio de comida',
                CategoriaOcupacional: 'Cocinero',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 10,
                Nombre:'Juan',
                Apellido: 'García',
                Edad: '35',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Psicosocial',
                Sector: 'Industria',
                RamaDeActividadEconomica: 'Construcción',
                CategoriaOcupacional: 'Albañil',
            },
        ]
    
        Estadistica = [
            ...Estadistica,
            {
                id: 11,
                Nombre: 'Carlos',
                Apellido: 'Martinéz',
                Edad: '20',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Visual',
                Sector: 'Comercio',
                RamaDeActividadEconomica: 'Actividades inmobiliarias',
                CategoriaOcupacional: 'Agente inmobiliario',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 12,
                Nombre:'Andrés Lopéz',
                Apellido: 'Lopéz',
                Edad: '29',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Física',
                Sector: 'Agricultura',
                RamaDeActividadEconomica: 'Servicios administrativos y apoyo',
                CategoriaOcupacional: 'Asistente',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 13,
                Nombre:'Gabriel',
                Apellido: 'Ortega',
                Edad: '24',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Intelectual',
                Sector: 'Agricultura',
                RamaDeActividadEconomica: 'Otras actividades de servicio',
                CategoriaOcupacional: 'Agricultor',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 14,
                Nombre:'David',
                Apellido: 'Ríos',
                Edad: '23',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Visual',
                Sector: 'Industria',
                RamaDeActividadEconomica: 'Atención a la salud humana',
                CategoriaOcupacional: 'Ayudante de enfermería',
            },
        ]

        Estadistica = [
            ...Estadistica,
            {
                id: 15,
                Nombre:'Francisco',
                Apellido: 'Torres',
                Edad: '24',
                Genero: 'Masculino',
                TipoDeDiscapacidad: 'Intelectual',
                Sector: 'Industria',
                RamaDeActividadEconomica: 'Industria manufacturera',
                CategoriaOcupacional: 'Operador de montaje',
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