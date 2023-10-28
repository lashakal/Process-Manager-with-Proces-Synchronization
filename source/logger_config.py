import logging

# Create a logger
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("log_file.log", mode="w")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)