const express = require('express');
const router = express.Router();
const Book = require('../models/book');

// GET all books
router.get('/', async (req, res) => {
  const books = await Book.find();
  res.json(books);
});

// GET book by ID
router.get('/:id', async (req, res) => {
  const book = await Book.findById(req.params.id);
  if (!book) return res.status(404).json({ message: 'Book not found' });
  res.json(book);
});

// POST new book
router.post('/', async (req, res) => {
  const book = new Book(req.body);
  await book.save();
  res.status(201).json(book);
});

// DELETE book
router.delete('/:id', async (req, res) => {
  const book = await Book.findById(req.params.id);
  if (!book) return res.status(404).json({ message: 'Book not found' });
  await book.deleteOne();
  res.json({ message: 'Book deleted' });
});

module.exports = router;