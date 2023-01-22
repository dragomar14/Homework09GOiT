def format_phone_number(func):

    def true_cover(num):
        new_num = func(num)
        if len(new_num) == 12:
            return f"+{new_num}"
        else:
            return f"+38{new_num}"

    return true_cover