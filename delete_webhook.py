import telebot
import requests
import time

# توکن ربات را اینجا وارد کنید
BOT_TOKEN = "8610416077:AAGJbj8xXvBCkIZNH_iBEn1mbZJyovh4474"

def delete_webhook():
    # روش اول: استفاده از متد remove_webhook
    try:
        bot = telebot.TeleBot(BOT_TOKEN)
        bot.remove_webhook()
        print("Webhook deleted successfully (Method 1)")
    except Exception as e:
        print(f"Error deleting webhook with method 1: {e}")
        
        # روش دوم: استفاده مستقیم از API تلگرام
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
            response = requests.get(url)
            if response.status_code == 200 and response.json().get('ok'):
                print("Webhook deleted successfully (Method 2)")
            else:
                print(f"Error deleting webhook with method 2: {response.text}")
        except Exception as e:
            print(f"Error deleting webhook with method 2: {e}")

if __name__ == "__main__":
    delete_webhook()
    print("Please wait a few seconds...")
    time.sleep(3)  # اندکی صبر برای اطمینان از اعمال تغییرات
    print("You can now run the bot with polling method.") 