import logging
import os
from datetime import datetime
def create_log():
  """
  Creates a log file with the current date and time as its name in the "logs" folder.
  If the "logs" folder does not exist, it will be created.
  The location of the log file will be determined by the current working directory.
  The format of the log file will include the date and time, line number, name, log level, and message.
  The log level will be set to INFO.

  """
  log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
  logs_path = os.path.join(os.getcwd(),"logs",log_file)
  os.makedirs(logs_path,exist_ok=True)
  log_file_path = os.path.join(logs_path,log_file)
  logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
  )

#if __name__=="__main__":
    #create_log()
    #logging.info('Logging has started...')
