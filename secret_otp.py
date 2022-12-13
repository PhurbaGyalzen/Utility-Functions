import secrets
# secrets is a default python module introuduced after python version 3.6.
# Note: The python random module is not random if it's seed is found. Use secrets instead for fully random numbers.  


def generate_otp(length: int)-> int:
    """
    Args:
        length (int): Lenght of OTP to be generated

    Returns:
        int: OTP 
    """

    otp_length = 10**length
    
    # Generates a random input-length digit(s) number(s)
    otp = secrets.randbelow(otp_length)

    # Add ending zeros if otp is less than input length
    otp = otp = str(otp).ljust(length, "0")

    return int(otp)
