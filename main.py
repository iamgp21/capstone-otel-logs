import logging 
from glob_logging import CustomLogFW


global_logger = CustomLogFW(service_name="main", instance_id="1")
handler = global_logger.setup_logging()
logging.getLogger().addHandler(handler)

if __name__ == "__main__":
    logging.error("This is a error message from main")
