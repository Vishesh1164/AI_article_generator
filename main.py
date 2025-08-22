from flask import Flask ,render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv('GEMINI_API_KEY') )

prompt_template = PromptTemplate(
    input_variables=["prompt"],
    template='''Write a well-researched, engaging, and easy-to-read article on the topic: "{prompt}".  

Guidelines:
- Start with an attention-grabbing introduction.  
- Explain the topic clearly with proper structure (use headings and subheadings where needed).  
- Add real-world examples, use cases, or analogies for better understanding.  
- Keep the tone informative yet conversational (not robotic).  
- Conclude with key takeaways or a summary.  
- Optimize readability (short paragraphs, bullet points where useful).  
- Length: around 800–1000 words.  

'''
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["GET","POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    # Call your AI model or processing function here
    formatted_prompt = prompt_template.format(prompt=prompt)
    result = llm.invoke(formatted_prompt)
    return jsonify({"result": result.content})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT automatically
    app.run(host="0.0.0.0", port=port, debug=False)

