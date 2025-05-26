import hashlib
import random
import time

# 生成雪花算法唯一ID
def generate_snowflake_id():
    timestamp = int(time.time() * 1000)  # 当前时间戳，精确到毫秒
    random_num = random.randint(0, 999)  # 随机数
    return str(timestamp) + str(random_num)


app_key = "gitsqTTQ3pnEvFyC"
app_id = "Q0NylSZ7hj"

timestamp = int(time.time() * 1000)
request_id = generate_snowflake_id()
sign_str = app_key + app_id + request_id + str(timestamp) + app_key
signature = hashlib.md5(sign_str.encode()).hexdigest()

# print("x-request-id:", request_id)
# print("x-timestamp:", timestamp)
# print("x-signature:", signature)

