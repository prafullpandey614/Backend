import regex as re


from django.core.exceptions import ValidationError
def validate_email_mobile(data):
    if not re.match(r"^\S+@\S+\.\S+$",data) and not re.match(r"^[6-9][0-9]{9}$",data):
        raise ValidationError("Invalid email/mobile number")
    if len(data) > 255:
        raise ValidationError("Invalid email/mobile number")
    return data