const express = require('express');
const app = express();
var cors = require('cors');

app.use(express.json())
app.get('/alumnos', (req, res) =>{
    console.log(req.query);
    res.send('Hello World, appget');
});

app.get('/docentes/:control', (req, res) =>{
    console.log(req.params);
    res.send('Hello World');
});

app.post('/directivos', (req, res) =>{
    console.log(req.params);
    res.send('Hello World');
});

app.listen(3001, () => {
    console.log('WE ON PORT 3000 SUCKAAAAAAAAAAAAA');
});