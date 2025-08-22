# LangChain Article Generator

A Flask web application that uses Google Gemini AI (via LangChain) to generate well-researched, engaging articles on any topic.  
Includes a Tailwind CSS-powered frontend for a modern UI.

---

## Features

- **AI Article Generation:** Uses Gemini 2.5 Flash model for high-quality content.
- **Customizable Prompt:** Generates articles with structure, examples, and conversational tone.
- **Responsive UI:** Styled with Tailwind CSS.
- **Environment Variables:** Secure API key management via `.env`.

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/langchain.git
cd langchain
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
npm install
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4. Build Tailwind CSS

```sh
npm run tw
```

This will watch and build your CSS from `static/src/source.css` to `static/css/output.css`.

### 5. Run the Flask app

```sh
python main.py
```

---

## Usage

- Open [http://localhost:5000](http://localhost:5000) in your browser.
- Enter a topic and click "Generate" to receive a full-length article.

---

## Project Structure

```
langchain/
│
├── main.py                  # Flask backend
├── package.json             # npm scripts & dependencies
├── .env                     # API keys (not tracked by git)
├── templates/
│   └── index.html           # Frontend HTML
├── static/
│   ├── src/source.css       # Tailwind CSS source
│   └── css/output.css       # Compiled CSS
└── .gitignore
```

---

## Customization

- **Prompt Template:** Edit `main.py` to change article style or requirements.
- **Styling:** Modify `static/src/source.css` and rebuild with `npm run tw`.

---

## Troubleshooting

- **npm errors:**  
  If you see `could not determine executable to run`, try:
  - `npm install`
  - `npm cache clean --force`
  - Delete `node_modules` and `package-lock.json`, then reinstall.

- **API errors:**  
  Ensure your `.env` file contains a valid `GEMINI_API_KEY`.

---

## License

ISC

---

## Author

Vishesh Srivastava
