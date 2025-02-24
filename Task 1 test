def check_name(name):
    # TODO: implement this function
    if u"\u2b55" in name:
        return False
    elif name[0] == " " or name[-1] == " ":
        return False
    else:
        return True
            
def check_name_len(name):
    # TODO: implement this function
    if len(name) < 21:
        return True
    return False

def check_sid_len(name):
    # TODO: implement this function
    new_name = str(name)
    if len(new_name) != 10:
        return False
    elif " " in new_name:
        return False
    elif new_name[0:4] != "1155":
        return False
    return True
