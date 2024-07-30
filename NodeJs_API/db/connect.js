const mongoose = require('mongoose');

// uri=
// 'mongodb+srv://birbalkr1435:Birbal!@#123@myappapi.eqfuppm.mongodb.net/myappapi?retryWrites=true&w=majority&appName=myappapi'



const connectDB=(uri)=>{
    console.log('db');
    return mongoose.connect(uri, {
        useNewUrlParser:true,
        useUnifiedTopology:true,
    });
};

module.exports = connectDB;













