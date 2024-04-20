import logging
import os
from datetime import datetime

LOG_FILENAME = datetime.now().strftime('%m_%d_%Y_%H_%M_S') + ".log"
log_directory = os.path.join(os.getcwd(), "logs")
os.makedirs(log_directory, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_directory, LOG_FILENAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started.")
