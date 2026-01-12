import sys
import os

def get_custom_error(error, error_details: sys):
    _, _, tb = error_details.exc_info()

    # Go to the deepest traceback
    while tb.tb_next:
        tb = tb.tb_next

    file_name = os.path.basename(tb.tb_frame.f_code.co_filename)
    line_no = tb.tb_lineno

    error_msg = f"File: {file_name} | Line: {line_no} | Error: {str(error)}"

    return error_msg


class CustomError(Exception):
    def __init__(self, error, error_details: sys):
        self.error_message = get_custom_error(error, error_details)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

