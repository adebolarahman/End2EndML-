import sys
from src.logger import logging
import logging
def error_report_retails(err: str,err_detail:sys) -> str:
    """
    function that takes in two parameters, err and err_detail, which are of type string and sys respectively. 
    The function returns a string value. The function extracts the filename and line number from the sys module
    and formats the error message to include this information along with the error message provided as the err parameter. 

    """
    _,_,exc_tb=err_detail.exc_info()

    filename=exc_tb.tb_frame.f_code.co_filename
    err_msg="This error occured in the python file:  [{0}] on line number [{1}] with error message  [{2}]".format(
    filename,exc_tb.tb_lineno,str(err))
    return err_msg
class CustomException(Exception):
    
    """
    The "CustomException" class is a custom exception that inherits from the general "Exception" class. 
    It has two parameters: "err_msg" and "err_detail", with the latter being a system-related detail.
    The constructor method "__init__" initializes the exception by calling the parent class and passing
    the "err_msg" parameter. It also assigns the value of the "error_report_retails" function to the "error_message" 
    attribute, passing in the "err_msg" and "err_detail" parameters. The "__str__" method returns the value of the
    "error_message" attribute when the exception is raised. 
    
    """
    def __init__(self,err_msg,err_detail:sys):
        super().__init__(err_msg)
        self.error_message=error_report_retails(err_msg,err_detail=err_detail)
    
    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info('Undefined Error!')
        raise CustomException(e, sys)
