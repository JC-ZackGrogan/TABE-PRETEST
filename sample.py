from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# OpenAI client setup
client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1/",
    api_key=""
)

def generate_problem(topic, section):
    """Use OpenAI API to generate a structured problem and solution."""
    messages = [
        {
            "role": "user",
            "content": f"Create a {section} problem and solution for the topic: {topic}. Provide a structured JSON response with keys 'problem' and 'answer'."
        }
    ]
    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        messages=messages,
        max_tokens=2000
    )
    structured_output = completion.choices[0].message["content"]
    return structured_output

@app.route('/')
def home():
    return "<h1>Welcome to the Math and Reading Test API</h1>"

@app.route('/test/math', methods=['GET'])
def math_test():
    topics = [
        "Dividing Fractions", "Equilateral Triangle", "Real Numbers", "Order of Operations",
        "Corresponding Angles", "Adding Decimals", "Exponent Powers", "Basics of Factors",
        "Obtuse triangle", "Irrational Numbers", "Area Calculations", "The Quadratic Formula",
        "Percentages", "Slope Formula", "Ratios", "General Polynomial", "Perimeter Calculations",
        "Intercept", "Multiplying Fractions", "Complex Numbers", "Measurement"
    ]
    problems = []
    for topic in topics:
        structured_response = generate_problem(topic, "math")
        problems.append({"topic": topic, "data": structured_response})
    return jsonify(problems)

@app.route('/test/reading', methods=['GET'])
def reading_test():
    topics = [
        "Commas", "Appositive", "Semicolon", "Sentence Fragment", "Dashes", "Conjunctive Adverbs",
        "Quotation Marks", "Independent Clause", "Adjective Phrases", "Equal Comparisons",
        "Conjunctions", "Noun phrases", "Parts of Speech", "Pronoun", "Linking verbs", "Intransitive verbs",
        "Auxiliary verbs", "Capitalization Rules", "Parallelism", "Negation", "Word Usage", "Vocabulary"
    ]
    problems = []
    for topic in topics:
        structured_response = generate_problem(topic, "reading")
        problems.append({"topic": topic, "data": structured_response})
    return jsonify(problems)

if __name__ == '__main__':
    app.run(debug=True)
