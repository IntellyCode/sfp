from config import Config
from reader import Reader
from writer import Writer
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger(__name__)
    config = Config()

    reader = Reader(config.get_pdf_path())
    writer = Writer(config.get_output_path())

    for data in reader.loop():
        writer.write(data)
