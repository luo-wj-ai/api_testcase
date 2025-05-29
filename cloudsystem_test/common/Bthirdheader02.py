import hmac
import hashlib
import base64
import time
import uuid


def generate_api_auth_data():
    """
    Generate authentication data with HMAC-SHA256 signature.
    Returns four values (client_id, timestamp, request_id, signature), each with "02" appended.
    """
    client_id = '72Y0eyQT4POSWaHDwfeqXoj2osMusXlW'
    client_key = 'ka5fO9bbkayixlIOyxb2s4Nq5xQ1I1r5'

    def generate_hmac_sha256(client_id, client_key, request_id, timestamp):
        message = f"{client_id}:{request_id}:{timestamp}"
        digest = hmac.new(
            client_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).digest()
        return base64.b64encode(digest).decode('utf-8')

    # Generate request ID (UUID without hyphens)
    request_id = str(uuid.uuid4()).replace('-', '')

    # Generate timestamp (milliseconds, current time + 2 minutes)
    timestamp = str(int((time.time() + 120) * 1000))

    # Generate signature
    signature = generate_hmac_sha256(client_id, client_key, request_id, timestamp)

    # Return four values, each with "02" appended
    return (
        str(client_id),
        str(request_id),
        str(timestamp),
        str(signature)
    )


# Example usage
if __name__ == "__main__":
    a, b, c, d = generate_api_auth_data()
    print(f"a (clientId02): {a}")
    print(f"b (timestamp02): {b}")
    print(f"c (requestId02): {c}")
    print(f"d (signature02): {d}")