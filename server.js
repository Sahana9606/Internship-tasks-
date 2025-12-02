const express = require('express');
const mongoose = require('mongoose');
const booksRouter = require('./routes/book');

const app = express();
app.use(express.json());

mongoose.connect('mongodb://127.0.0.1:27017/library', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

app.use('/books', booksRouter);

const port = 3000;
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});