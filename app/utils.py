import random

def send_otp(aadhaar_number):
    print(f"Sending OTP to Aadhaar: {aadhaar_number}")
    return str(random.randint(100000, 999999))

def verify_otp(user_input, real_otp):
    return user_input == real_otp
