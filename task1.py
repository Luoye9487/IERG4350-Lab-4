import re

def check_name(name):
    # TODO: implement this function
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF"  
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF"  
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    
    if emoji_pattern.search(name):
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
