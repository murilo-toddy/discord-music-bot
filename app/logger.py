import logging


logging.basicConfig(
        level=logging.INFO, 
        datefmt="%d-%m-%y %H:%M:%S",
        format="""
            \n[%(levelname)s] %(module)s at %(lineno)s\n[%(asctime)s] %(message)s
        """,
)

logger = logging.getLogger()

