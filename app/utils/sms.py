import os
import random

from dotenv import load_dotenv
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

load_dotenv()

SMS_API_KEY = os.getenv("SMS_API_KEY")
SMS_API_SECRET = os.getenv("SMS_API_SECRET")
SENDER_NUMBER = os.getenv("SENDER_NUMBER")

def generate_verification_code(length=6):
    return "".join(random.choices("0123456789", k=length))

def send_sms(to: str, from_: str, text: str):
    params = {
        "type": "sms",
        "to": to,
        "from": from_,
        "text": text,
    }
    cool = Message(SMS_API_KEY, SMS_API_SECRET)
    try:
        response = cool.send(params)
        if response["success_count"] <= 0:
            raise CoolsmsException(f"Failed to send SMS: {response['error_list']}")
    except CoolsmsException as e:
        raise e
