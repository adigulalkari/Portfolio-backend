from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use your SMTP server (example for Gmail)
app.config['MAIL_PORT'] = 587  # TLS port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password or app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'  # Default sender address

mail = Mail(app)

@app.route('/api/send-email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()  # Get the form data in JSON format
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({'success': False, 'message': 'Missing fields'}), 400

        # Create the email message
        msg = Message(
            subject=f"New message from {name}",
            recipients=["recipient-email@example.com"],  # Replace with the recipient's email
            body=f"You have received a new message from {name} ({email}):\n\n{message}",
        )

        # Send the email
        mail.send(msg)
        
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200

    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': 'Failed to send email'}), 500


if __name__ == '__main__':
    app.run(debug=True)
