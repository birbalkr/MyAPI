const mongoose = require('mongoose');

// uri=
// 'mongodb+srv://birbalkr1435:Birbal!@#123@myappapi.eqfuppm.mongodb.net/myappapi?retryWrites=true&w=majority&appName=myappapi'

uri = "mongodb+srv://birbalkr1435:AkjV672rvjrL2Omi@myappapi.eqfuppm.mongodb.net/myappapi?retryWrites=true&w=majority&appName=myappapi"



const connectDB=()=>{
    console.log('db');
    return mongoose.connect(uri, {
        useNewUrlParser:true,
        useUnifiedTopology:true,
    })
};

module.exports = connectDB;













