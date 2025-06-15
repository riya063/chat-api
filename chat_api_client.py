import requests

# 🛑 Replace these with your actual API endpoints from CloudFormation output
GET_MESSAGES_URL = "https://ck3lb9wzu1.execute-api.ap-south-1.amazonaws.com/Prod/messages"
SEND_MESSAGE_URL = "https://ck3lb9wzu1.execute-api.ap-south-1.amazonaws.com/Prod/messages"

# ✅ Function to send a new message
def send_message(chat_id, message):
    payload = {
        "chatId": chat_id,
        "message": message
    }
    response = requests.post(POST_MESSAGE_URL, json=payload)
    if response.status_code == 200:
        print("✅ Message sent successfully.")
    else:
        print(f"❌ Failed to send message: {response.status_code}")
        print(response.text)

# ✅ Function to get all messages
def get_messages():
    response = requests.get(GET_MESSAGES_URL)
    if response.status_code == 200:
        messages = response.json()
        print("📨 All Messages:")
        for msg in messages:
            print(msg)
    else:
        print(f"❌ Failed to retrieve messages: {response.status_code}")
        print(response.text)

# ✅ Run the script
if __name__ == "__main__":
    print("📤 Sending message...")
    send_message("chat123", "Hello from Riya’s Python client!")

    print("\n📥 Fetching messages...")
    get_messages()
