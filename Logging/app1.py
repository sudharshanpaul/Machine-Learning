import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler() # Method which is responsible for putting all logs inside the particular file
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a}-{b} = {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug("Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(10,15)
subtract(15,10)
multiply(10,7)
divide(10,0)