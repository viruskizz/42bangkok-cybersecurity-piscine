const express = require("express");
const path = require("path");
const app = express();

// Set EJS as the view engine
app.set("view engine", "ejs");

// Set the views directory
app.set("views", path.join(__dirname, "views"));
app.use('/public', express.static('public'))

app.get("/", function(req, res) {
    user = {
        firstName: 'Araiva',
        lastName: 'Viruskizz'
    }
    res.render('pages/index', {
        user,
        title: 'Homepage'
    });
});

app.listen(3000, function(){
    console.log('Listening on port 3000');
});