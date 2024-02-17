import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyB_Spr9VuJEtTCHIfZy4HJm9eoX-cymKYE"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

app = Flask(__name__)

model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    user_message = data['message']

    response = model.generate_content(user_message)
    bot_response = response.text
    formatted_response = format_response(bot_response)

    return jsonify({'content': formatted_response})

def format_response(response_text):
    # Split the response into separate points
    points = response_text.split('*')

    # Create an unordered list from the points
    formatted_response = '<ul>'
    for point in points:
        if point.strip() != '':
            formatted_response += f'<li>{point.strip()}</li>'
    formatted_response += '</ul>'

    return formatted_response

if __name__ == '__main__':
    app.run(debug=True)
