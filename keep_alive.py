from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Bóng X Bot</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                .container {
                    text-align: center;
                    padding: 40px;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                }
                h1 { margin: 0 0 20px 0; font-size: 3em; }
                p { font-size: 1.2em; opacity: 0.9; }
                .status { 
                    display: inline-block;
                    padding: 10px 20px;
                    background: #4CAF50;
                    border-radius: 25px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🤖 Bóng X Telegram Bot</h1>
                <p>Bot đang chạy và sẵn sàng phục vụ!</p>
                <div class="status">✅ Online 24/7</div>
                <p style="margin-top: 30px; font-size: 0.9em;">
                    Created by Bóng X
                </p>
            </div>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {'status': 'ok', 'bot': 'running'}, 200

def run():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
