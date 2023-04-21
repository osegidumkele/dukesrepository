var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

const axios = require('axios');
// set the view engine to ejs

app.use(bodyParser.urlencoded());

app.set('view engine', 'ejs');


// use res.render to load up an ejs view file

// index page
app.get('/', function(req, res) {

  res.render('pages/index', {
    
  });
});

app.get('/api', function(req, res) {

    //API call
    axios.get('https://jsonplaceholder.typicode.com/users')
    .then((response)=>{
//code to hold the api data and pull 3 random results
        const users = response.data;
        const values = [];
        for (let i = 0; i < 3; i++) {
            const randomIndex = Math.floor(Math.random() * users.length);
            values.push(users[randomIndex]);
        }
        console.log(values);
        res.render('pages/api', { values, tagline:tagline });
    })
    .catch(error => console.error(error));

});



app.listen(8080);
console.log('Server is listening on port 8080');
