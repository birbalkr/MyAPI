require('dotenv').config();
const connectDB = require('./db/connect');
const Product = require('./models/product');

const productjson=require('./products.json')

const start = async() =>{
    try {
        await connectDB(process.env.MONGODB_URL);
        await Product.create(productjson);
        console.log('add');
    } catch (error) {
        console.log(error);
    }
};


start();
