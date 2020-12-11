import os
from tsquery.cli import cli
if os.getenv('TSQUERY_DEBUG'):
    import logging
    from tsquery import logger
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
cli()
