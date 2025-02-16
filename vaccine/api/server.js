const express = require('express')
const mysql = require('mysql')
const bodyParser = require('body-parser')

const app = express();
const PORT = process.env.PORT || 3000;
// Middleware
app.use(bodyParser.json());
// MySQL Connection
// const db = mysql.createConnection({
//   host: 'localhost',
//   user: 'your_username',
//   password: 'your_password',
//   database: 'your_database_name'
// });
// Connect to MySQL
// db.connect((err) => {
//   if (err) {
//     console.error('Error connecting to MySQL: ' + err.stack);
//     return;
//   }
//   console.log('Connected to MySQL as ID ' + db.threadId);
// });
// // Routes
// app.get('/api/users', (req, res) => {
//   db.query('SELECT * FROM users', (err, results) => {
//     if (err) {
//       console.error('Error executing query: ' + err.stack);
//       res.status(500).send('Error fetching users');
//       return;
//     }
//     res.json(results);
//   });
// });
app.get('/', (req, res) => {
  res.json({
    message: 'Hello World'
  })
})
// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});