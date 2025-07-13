# 📚 Book Recommender Chatbot

![Book Recommender Chatbot](https://img.shields.io/badge/Status-Active-brightgreen)  
A modern, interactive chatbot that recommends books based on genre, author, or mood, built with HTML, JavaScript, and styled with Tailwind CSS, powered by a local JSON API.

## ✨ Features
- **Conversational Interface**: Guides users through selecting recommendation criteria (genre, author, mood) with a smooth chat flow.
- **Dynamic Book Suggestions**: Fetches real-time recommendations from a local API, displaying title, author, and description.
- **Sleek Design**: Responsive UI with Tailwind CSS for a clean, mobile-friendly experience.
- **Robust Error Handling**: Gracefully manages API failures with clear user feedback.
- **Lightweight**: Pure HTML/JavaScript solution, no heavy frameworks required.

## 🛠️ Tech Stack
- **Front-End**: HTML, JavaScript, Tailwind CSS (via CDN)
- **Back-End**: Local JSON API (running at `http://localhost:3000`)
- **API Data**: Based on `books_openapi.json` and `books_sample.json`

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge, etc.)
- A local API server running at `http://localhost:3000` (see [API Setup](#api-setup))
- Optional: A simple HTTP server (e.g., `http-server` via Node.js) for local development

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/book-recommender-chatbot.git
   cd book-recommender-chatbot
   ```

2. **Set Up the Front-End**:
   - Ensure `index.html` (containing the HTML/JavaScript chatbot code) is in the repository root.
   - Verify Tailwind CSS is included via CDN (`https://cdn.tailwindcss.com`).

3. **Run a Local Server** (recommended for development):
   - Install `http-server` (optional):
     ```bash
     npm install -g http-server
     ```
   - Start the server:
     ```bash
     http-server
     ```
   - Open `http://localhost:8080` in your browser.

4. **Alternative**: Directly open `index.html` in a browser (note: API requests may be blocked due to CORS without a server).

### API Setup
- The chatbot expects a JSON API at `http://localhost:3000` with endpoints `/books/genre`, `/books/author`, and `/books/mood`, as defined in `books_openapi.json`.
- The API should return an array of objects with `title`, `author`, and `description` fields, matching the structure in `books_sample.json`.
- Example API response for `http://localhost:3000/books/genre?q=sci-fi`:
  ```json
  [
    {"title": "Dune", "author": "Frank Herbert", "description": "A sci-fi epic..."},
    {"title": "Ender's Game", "author": "Orson Scott Card", "description": "A young prodigy..."}
  ]
  ```
- Ensure the API server is running before launching the chatbot. Contact your backend developer or refer to your API documentation for setup details.

### Usage
1. Open `http://localhost:8080` (or double-click `index.html`).
2. Follow the chatbot prompts to select a recommendation type (genre, author, or mood).
3. Enter a query (e.g., `sci-fi`, `dan brown`, `happy`) in lowercase, matching the keys in `books_sample.json`.
4. View book recommendations displayed with titles, authors, and descriptions.
5. Click "Start Over" to reset the conversation.

## 📸 Screenshots
<img width="1916" height="924" alt="Screenshot 2025-07-14 011126" src="https://github.com/user-attachments/assets/9c3c5a23-111c-4626-94a8-04641c0daebd" />

## 🐛 Troubleshooting
- **API Error**: If you see "Sorry, I couldn't fetch book recommendations," check if the API server is running:
  ```bash
  curl http://localhost:3000/books/genre?q=sci-fi
  ```
  Ensure it returns valid JSON.
- **CORS Issues**: If API requests fail, verify the API server allows CORS for `http://localhost:8080`. Update server configuration if needed.
- **Query Mismatch**: Use lowercase queries (e.g., `sci-fi`, `dan brown`, `happy`) to match `books_sample.json` keys.
- **Blank Page**: Ensure `index.html` includes the correct Tailwind CSS CDN and JavaScript logic. Check browser console for errors (F12 > Console).

## 🤝 Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.
