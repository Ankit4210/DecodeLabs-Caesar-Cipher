import hashlib


def create_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def check_password(password, saved):

    return create_password(password)==saved
