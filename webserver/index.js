var config = require('./config');
var bodyParser = require('body-parser')
var express = require('express');
var morgan = require('morgan');
var cors = require('cors');

var app = express();


//Enabling CORS
app.use(cors());

//Log Enabled
app.use(morgan('dev'));

//Use body parser so we can grab information from POST requests
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

app.use('/api', require('./routes/sentimentRouter')(express));

app.listen(config.PORT, function() {
    console.log('Server Running');
})
