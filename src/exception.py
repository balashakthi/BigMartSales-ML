import sys
import logging

logging.basicConfig(level=logging.INFO)  # Configure logging

def error_message_detail(error, error_detail):
    exc_type, exc_value, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script: [{file_name}], Line [{exc_tb.tb_lineno}], Message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message

