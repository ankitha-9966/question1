from verification import account_creation
def test_case():
    assert account_creation("Ankitha9@gmail.com","Anki1234",5,"123456","123456")=="Account created"
    assert account_creation("","Anki1234",5,"123456","123456")=="email or password missing"
    assert account_creation("Ankitha9@gmail.com","Anki1234",3,"123456","123456")=="captcha not correct"
    assert account_creation("Ankitha9@gmail.com","Anki1234",5,"12345","123456")=="email otp not correct"
    assert account_creation("Ankitha9@gmail.com","Anki1234",5,"123456","1234567")=="sms otp not correct"
    print("All tests passed")
if __name__ == "__main__":
        test_case()
    

