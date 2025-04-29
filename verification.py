def generate_otp():
    return "123456"
def captcha_question():
    return 2+3
def verify_captcha(ans):
    return ans==captcha_question()
def verify_email(user_otp):
    return user_otp==generate_otp()
def verify_sms(user_otp):
    return user_otp==generate_otp()
def account_creation(email,password,captcha_ans,email_otp,sms_otp):
    if not email or not password:
        return "email or password missing"
    if not verify_captcha(captcha_ans):
        return "captcha not correct"
    if not verify_email(email_otp):
        return "email otp not correct"
    if not verify_sms(sms_otp):
        return "sms otp not correct"
    return "Account created"
