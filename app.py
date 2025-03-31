from flask import Flask, request

app = Flask(__name__)

# Your verify token (must match the token you use in Meta Webhook setup)
VERIFY_TOKEN = 'myverifytoken123'

@app.route('/', methods=['GET'])
def index():
    return 'Webhook server is running!', 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verification handshake with Meta
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            print('WEBHOOK VERIFIED')
            return challenge, 200
        else:
            print('VERIFICATION FAILED')
            return 'Verification token mismatch', 403

    elif request.method == 'POST':
        # Webhook data received from WhatsApp
        data = request.get_json()
        print("WEBHOOK DATA RECEIVED:")
        print(data)
        return 'EVENT_RECEIVED', 200

    else:
        return 'Method not allowed', 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
