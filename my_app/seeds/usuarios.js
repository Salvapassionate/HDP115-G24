'use strict'
const { faker } = require('@faker-js/faker')
/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        /**
         * Agregue comandos semilla aquí.                  
         */
        let usuarios = []
        const niveles = ['verde', 'amarilla', 'roja']
        usuarios = [
            ...usuarios,
            {
                id: 1,
                nombre:'admin',
                password: 'admin10*',
                               
            },
        ]

        usuarios = [
            ...usuarios,
            {
                id: 2,
                nombre:'user',
                password: 'user10*',
                               
            },
        ]

        usuarios = [
            ...usuarios,
            {
                id: 3,
                nombre:'pm18106',
                password: 'achievo.djangopm18106',
                               
            },
        ]

        usuarios = [
            ...usuarios,
            {
                id: 4,
                nombre:'pb21015',
                password: 'achievo.djangopm18106',
                               
            },
        ]

        usuarios = [
            ...usuarios,
            {
                id: 5,
                nombre:'rh21014',
                password: 'achievo.djangopm18106',
                               
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