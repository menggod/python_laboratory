def validate_pin(pin):
    if len(pin) > 4:
        return False
    else:
        for x in pin:
            if str(x).isnumeric():
                return True
            else:
                return False


print(validate_pin("-1.74"))
