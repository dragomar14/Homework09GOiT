from format_phone_number import *


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (phone.strip().removeprefix("+").replace("(", "")
                 .replace(")", "").replace("-", "").replace(" ", ""))
    new_phone = [str(int(i)) for i in new_phone]
    new_phone = "".join(new_phone)
    return new_phone