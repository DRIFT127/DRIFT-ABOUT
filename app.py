from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Render the main page (templates/index.html)
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def handle_contact():
    # Get form data from the contact section
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Print to console (you can replace with email or database)
    print(f"\n📨 New message from: {name} ({email})")
    print(f"💬 Message: {message}\n")
    
    # Return JSON response for the frontend fetch request
    return jsonify({"status": "success", "message": "Message sent securely!"})

if __name__ == '__main__':
    # For production on Render, use debug=False and let platform set host/port
    # For local testing, you can keep debug=True (but note Termux issues, so use debug=False)
    app.run(debug=False, host='0.0.0.0', port=5000)