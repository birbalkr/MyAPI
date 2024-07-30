const mongoose = require('mongoose');


const productSchema = mongoose.Schema({
    name:{
        type:String,
        required:true,
    },
    price:{
        type:Number,
        required:[true, 'price must be provided'],
    }, 
    featured:{
        type:Boolean,
        default:true,
    }
})



module.exports = mongoose.model('Product', productSchema);

