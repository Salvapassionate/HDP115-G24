const sequelize = new Sequelize('edandb', 'root', '', {
    host: 'localhost',
    dialect: 'mysql',
    
    })
    
    // Apetura de servidor.
    
    app.listen(app.get('port'), () => {
    console.log(`servidor: http:/llocalhost:$i app.getº 'port')}`)
    
    })
    
    // Creacion de _es para login.
    
    // Habilitar uso de rutas.
    
    app.use('/', require('./routes/user.route'))
    
    app.use('/', require('./routes/home.route'))
    
    app.use( '/' , require( ' ./routeslalerta. route'))
    
    app.use('/', require(' ./routes/login.route'))
    
    app.use('/', require('./routes/inst.route'))