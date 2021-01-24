// --------------------- 
const mongo = require('mongoose')
//-------------------------
const express = require('express')
const deamon = express()
const fetch = require('node-fetch')
const Bluebird = require('bluebird')
fetch.Promise = Bluebird
const admin_db = require('/db/admin/db-admins.json')
const data = new Date(day)
const users = require('/db/users/')
// -------------------
  
mongo.connect('mongodb://localhost/db', { useMongoClient: true })
mongo.Promise = global.Promise

module.exports = mongo

//--------------------


// Admin --------
cobe = admin_db['cobe']
oreo = admin_db['oreo']
days_admin = true
//Common Users --

// --------------

function verify_Day(){}


function verify(key){
    if(key === cobe['key'] || key === oreo['key']){
        return {
            "status":true,
            "days":days_admin,
        }

    }else{
        return {
            "status":false,
            "days":0,
        }
    }
}

// script
deamon.get('/:key', (req, res)=> {
    key = req.params.key
    
    ex = verify(key)

    res.send(ex)

})



deamon.listen(1337, ()=> {
    
})