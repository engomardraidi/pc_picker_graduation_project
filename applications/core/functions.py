from .constants import Constants

def get_detail_response(message):
    return {Constants.DETAIL_KEY: message}