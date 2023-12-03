const express = require('express');
const path = require('path');
const axios = require('axios'); // Used for making HTTP requests to the Flask API

// Initialize Express app
const app = express();

// Set the view engine to EJS
app.set('view engine', 'ejs');

// Set the directory for EJS templates
app.set('views', path.join(__dirname, 'views'));

// Serve static files from the 'static' directory (if you have one)
app.use(express.static(path.join(__dirname, 'static')));

// Body parser middleware to parse request bodies
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Routes
app.get('/', (req, res) => {
    res.render('pages/index');
});

// Route for handling login form submission
app.post('/login', async (req, res) => {
    try {
        const response = await axios.post('http://localhost:5000/api/login', req.body);
        res.redirect('/');
    } catch (error) {
        const message = error.response && error.response.data ? error.response.data.message : 'Login failed. Please try again.';
        res.render('pages/error', { message });
    }
});

// Route: List Floors
app.get('/floors', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/api/floor');
        res.render('pages/floors', { floors: response.data });
    } catch (error) {
        const message = error.response && error.response.data ? error.response.data.message : 'Error fetching floors';
        res.render('pages/error', { message });
    }
});

// Route: List Rooms
app.get('/rooms', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/api/room');
        res.render('pages/rooms', { rooms: response.data });
    } catch (error) {
        const message = error.response && error.response.data ? error.response.data.message : 'Error fetching rooms';
        res.render('pages/error', { message });
    }
});

// Route: List Residents
app.get('/residents', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/api/resident');
        res.render('pages/residents', { residents: response.data });
    } catch (error) {
        const message = error.response && error.response.data ? error.response.data.message : 'Error fetching residents';
        res.render('pages/error', { message });
    }
});

// Set the port for the server to listen on
const PORT = process.env.PORT || 5000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Error stack:', err.stack);
    const message = err.response && err.response.data ? err.response.data.message : 'Something broke!';
    res.status(500).render('pages/error', { message });
});