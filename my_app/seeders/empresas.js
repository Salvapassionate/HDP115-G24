'use strict'
const { faker } = require('@faker-js/faker')
/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        /**
         * Agregue comandos semilla aquí.                  
         */
        let empresas = []
        const niveles = ['verde', 'amarilla', 'roja']
        empresas = [
            ...empresas,
            {
                id: 1,
                nombreE:'Siman Metrocentro',
                direcciónE: '7ma, 39 Avenida Norte Los Sisimiles and, Avenida Los Andes',
                correoE: 'contacto@siman.com',
                teléfonno: '2298-3777',                
            },
        ]
        
        empresas = [
            ...empresas,
            {
                id: 2,
                nombreE:'Súper Selectos Centro Comercial San Luis',
                direcciónE: 'Calle San Antonio Abad y Avenida Izalco',
                correoE: 'servicioalcliente@superselectos.com.sv',
                teléfonno: '2235-2423 / 2226-3579 / 2225-9265',                
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 3,
                nombreE:'Diparvel Escalón',
                direcciónE: 'Final 79 Av. Sur y principio de la 75 Av. Sur, Col. (2 cuadras antes del redondel de las fuentes Beethoven)',
                correoE: 'csd.escalon@diparvel.com.sv',
                teléfonno: '2263-0055 / 2263-4712',                
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 4,
                nombreE:'Texaco La 25',
                direcciónE: 'Sobre el boulevard tutunichapa y 25 Av. Norte',
                correoE: 'esacsc@chevron.com',
                teléfonno: '2526-7700',                
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 5,
                nombreE:'Siman Galerías',
                direcciónE: 'Paseo General Escalón #3700 Col. Escalón',
                correoE: 'contacto@siman.com',
                teléfonno: '2298-3777',                
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 6,
                nombreE:'Súper Selectos Aguilares',
                direcciónE: 'Avenida Central Norte y Final 2a Calle Oriente, Aguilares',
                correoE: 'servicioalcliente@superselectos.com.sv',
                teléfonno: '2321-4841 / 2321-5140',                
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 7,
                nombreE:'Diparvel Pedregal',
                direcciónE: 'Col. Jardines de la Hacienda, calle El Pedregal Pol. A-1 #13',
                correoE: 'csd.pedregal@diparvel.com.sv',
                teléfonno: '2520-4528',                
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 8,
                nombreE:'Texaco Centroamerica',
                direcciónE: '25 Av. Norte y Calle Gabriela Mistral',
                correoE: 'esacsc@chevron.com',
                teléfonno: '2244-5540',                
            },
        ]

        empresas = [
            ...empresas,
            {
                id: 9,
                nombreE:'Siman La Gran Vía',
                direcciónE: 'C. Panamericana Calle Chiltiupan, Centro Comercial La Gran Vía Local #1',
                correoE: 'contacto@siman.com',
                teléfonno: '2243-3000',                
            },
        ]

        empresas = [
            ...empresas,
            {
                id: 10,
                nombreE:'Super Selectos Ahuachapán',
                direcciónE: 'Carretera a Ahuachapan, desvío a Sonsonate',
                correoE: 'servicioalcliente@superselectos.com.sv',
                teléfonno: '2413-1804 / 2413-1806 / 2443-1866',
            },
        ]

        empresas = [
            ...empresas,
            {
                id: 11,
                nombreE:'Diparvel Venezuela',
                direcciónE: 'Boulevard Venezuela y calle Amberes Nº 10-A Col. Roma',
                correoE: 'csd.venezuela@diparvel.com.sv',
                teléfonno: '2520-4537 / 2520-4538',
            },
        ]
    
        empresas = [
            ...empresas,
            {
                id: 12,
                nombreE:'Texaco Santa Elena',
                direcciónE: 'Avenida Bella Vista y Calzada El Almendro, Polígono L, Bosques de Santa Elena 2',
                correoE: 'esacsc@chevron.com',
                teléfonno: '2244-5540',
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 13,
                nombreE:'Siman Plaza Mundo',
                direcciónE: 'Kilómetro 4 1/2 Boulevard Nacional del Ejercito Calle Monte Carmelo Centro Comercial Plaza Mundo-Expansión',
                correoE: 'contacto@siman.com',
                teléfonno: '2298-3777',
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 14,
                nombreE:'Super Selectos Apopa Pericentro',
                direcciónE: 'Km. 12 Carretera Troncal del Norte',
                correoE: 'servicioalcliente@superselectos.com.sv',
                teléfonno: '2216-0517 / 2216-5086 / 2216-5182',
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 15,
                nombreE:'Diparvel 27 Av. Sur',
                direcciónE: '12 Calle Poniente y 27 Avenida Sur.',
                correoE: 'csd.27avenida@diparvel.com.sv',
                teléfonno: '2520-4500 / 2520-4511 / 2520-4512',
            },
        ]

        empresas = [
            ...empresas,
            {
                id: 16,
                nombreE:'Texaco Caribe',
                direcciónE: 'Paseo General Escalón y Av.Manuel Enrique Araujo, frente a Salvador Del Mundo',
                correoE: 'esacsc@chevron.com',
                teléfonno: '2223-0653',
            },
        ]

        empresas = [
            ...empresas,
            {
                id: 17,
                nombreE:'Siman Santa Ana',
                direcciónE: 'Avenida Independencia Sur Centro comercial Metrocentro Local #101',
                correoE: 'contacto@siman.com',
                teléfonno: '2298-3777',
            },
        ]

        empresas = [
            ...empresas,
            {
                id: 18,
                nombreE:'Super Selectos Apopa Periplaza',
                direcciónE: 'Carretera Troncal del Norte Km. 12, Peri Plaza Apopa',
                correoE: 'servicioalcliente@superselectos.com.sv',
                teléfonno: '2214-9115',
            },
        ]
   
        empresas = [
            ...empresas,
            {
                id: 19,
                nombreE:'Diparvel 29 Calle Poniente',
                direcciónE: 'Entre 29 Calle Poniente y Avenida España',
                correoE: 'csd.29calle@diparvel.com.sv',
                teléfonno: '2226-1744 / 2225-0148',
            },
        ]
        empresas = [
            ...empresas,
            {
                id: 20,
                nombreE:'Texaco Quezaltepeque',
                direcciónE: 'Urb. Del Huerto Lote 12, Block F Quezaltepeque',
                correoE: 'esacsc@chevron.com',
                teléfonno: '2244-5540',
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