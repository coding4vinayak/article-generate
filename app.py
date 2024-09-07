from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Initialize the language model pipeline
model_name = "gpt-3"  # Replace with 'LLaMA' or other model names if needed
generator = pipeline("text-generation", model=model_name)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        if keyword:
            # Generate article topics
            prompt = f"Generate article topics based on the keyword: {keyword}"
            results = generator(prompt, max_length=50, num_return_sequences=5)
            topics = [result['generated_text'] for result in results]
            return render_template("index.html", topics=topics, keyword=keyword)
    return render_template("index.html", topics=None)

if __name__ == "__main__":
    app.run(debug=True)
