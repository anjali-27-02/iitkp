
const express = require('express');
const fs = require('fs');

const app = express();

// Define a route to upload images
app.post('/upload', (req, res) => {
  // Get the list of images
  const images = req.body.images;

  // Save the images to the `/static/images` folder
  for (const image of images) {
    fs.writeFileSync(__dirname + '/static/images/' + image, '');
  }

  // Respond with success
  res.json({
    success: true
  });
});

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000!');
});