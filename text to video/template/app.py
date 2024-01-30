from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_otp', methods=['POST'])
def generate_otp():
    # Generate a random 6-digit OTP
    import random
    otp = random.randint(100000, 999999)
    return jsonify({'otp': otp})

@app.route('/validate_login', methods=['POST'])
def validate_login():
    entered_otp = request.form.get('otp')
    
    # Simplified login validation logic, replace with your actual logic
    if entered_otp:
        # Redirect to front.html on successful login
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid OTP. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True)
