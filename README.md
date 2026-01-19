# Bóng X Telegram Bot

Bot Telegram AI được tạo bởi Bóng X với nhiều profile tính cách khác nhau.

## Tính năng

- 🤖 Chat AI với Cerebras Cloud SDK
- 👥 Nhiều profile tính cách (Default, Duy, Tiểu Vy)
- 🔐 Quyền admin cho một số lệnh
- 📝 Lưu lịch sử chat
- 🌐 Web server để deploy trên Render 24/7

## Lệnh Bot

### Lệnh Cơ Bản
- `/start` - Khởi động bot
- `/help` - Xem danh sách lệnh
- `/ping` - Kiểm tra trạng thái hệ thống

### Lệnh AI Chatbot
- `/chat <tin nhắn>` - Chat với AI
- `/profiles` - Xem danh sách profile AI
- `/profile <tên>` - Đổi profile AI (chỉ admin)

### Lệnh Admin (ID: 7509896689)
- `/profile` - Đổi profile AI
- `/cleanup` - Dọn dẹp tin nhắn

## Cài đặt Local

1. Clone repository:
```bash
git clone https://github.com/doanhvipqq/aiiibongxx.git
cd aiiibongxx
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Tạo file `.env`:
```env
TELEGRAM_TOKEN=your_telegram_bot_token
CER_API_KEY=your_cerebras_api_key
```

4. Tạo file `api_keys.json`:
```json
{
  "cerebras_api_keys": ["your_api_key_here"]
}
```

5. Chạy bot:
```bash
python main.py
```

## Deploy trên Render

### Bước 1: Tạo Web Service
1. Đăng nhập vào [Render](https://render.com)
2. Nhấn "New +" → "Web Service"
3. Connect repository: `https://github.com/doanhvipqq/aiiibongxx.git`

### Bước 2: Cấu hình
Render sẽ tự động phát hiện `render.yaml`. Bạn chỉ cần thêm Environment Variables:

**Environment Variables:**
- `TELEGRAM_TOKEN` = Token bot Telegram của bạn
- `CER_API_KEY` = API key Cerebras của bạn

### Bước 3: Deploy
Nhấn "Create Web Service" và đợi Render deploy!

Bot sẽ chạy 24/7 với web server tại `https://your-app.onrender.com`

## Cấu trúc Project

```
bot_tele/
├── main.py              # Entry point
├── keep_alive.py        # Flask web server
├── requirements.txt     # Python dependencies
├── render.yaml          # Render config
├── .env                 # Environment variables (local)
├── api_keys.json        # API keys (local)
├── handlers/
│   ├── chatbot.py      # AI chatbot handler
│   └── general.py      # General commands
├── utils/
│   ├── logger.py       # Logging utility
│   └── storage.py      # Data storage
└── data/
    ├── profiles/       # AI personality profiles
    ├── logs.json       # Chat logs
    └── viettat.json    # Vietnamese abbreviations
```

## Tác giả

**Bóng X**
- GitHub: [@doanhvipqq](https://github.com/doanhvipqq)
- Repository: [aiiibongxx](https://github.com/doanhvipqq/aiiibongxx)

## License

MIT License - Tự do sử dụng và chỉnh sửa
