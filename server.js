const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

app.use(express.static('public'));

app.get('/api/articles', (req, res) => {
    if (fs.existsSync('articles.json')) {
        const data = fs.readFileSync('articles.json');
        res.json(JSON.parse(data));
    } else {
        res.json([]);
    }
});

app.get('/article/:id', (req, res) => {
    const articles = JSON.parse(fs.readFileSync('articles.json'));
    const article = articles.find(a => a.id === req.params.id);
    res.send(`<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>body{font-family:sans-serif;padding:20px;line-height:1.6;max-width:800px;margin:auto}</style></head><body><a href="/">← Back</a><h1>${article.title}</h1><p>${article.content}</p></body></html>`);
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));