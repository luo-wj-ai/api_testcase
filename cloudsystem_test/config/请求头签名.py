import hmac
import hashlib
import base64
import time

'''订购请求头获取签名信息'''
def generate_hmac_sha256(app_id, app_key, timestamp):
    message = f"{app_id}:{timestamp}"
    key_bytes = app_key.encode('utf-8')
    message_bytes = message.encode('utf-8')

    sha256_hmac = hmac.new(key_bytes,message_bytes, hashlib.sha256)
    signature_bytes = sha256_hmac.digest()

    return base64.b64encode(signature_bytes).decode('utf-8')

app_id = "fF3iE0cA2cA5kC1cB3pB2bE2gL1cA1sd"
app_key = "hC0fT4qD0lB2aU2vD0bB0hD1aD2eC5df"
timestamp = str(int(time.time()))
signature = generate_hmac_sha256(app_id, app_key, timestamp)
# print("app_id:",app_id)
# print("timestamp:", timestamp)
# print("Signature:", "third_sys "+signature)
