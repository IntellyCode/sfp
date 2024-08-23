"""
Configuration class that loads and manages program parameters from a config.json file.

This class is initialized at the program's entry point and is responsible for loading
the configuration file and providing methods to access specific configuration settings.

Attributes:
    config (dict): A dictionary containing configuration parameters loaded from config.json.
    cwd (str): The current working directory of the program's parent directory.

Methods:
    get_pdf_path():
        Returns the absolute path to the PDF file specified in the config.json file.
    get_output_path():
        Returns the absolute path to the output file specified in the config.json file.
"""

from json import load
import os
import logging


class Config:
    def __init__(self):
        """
        Initializes the Config class by loading the configuration parameters from config.json
        and setting the current working directory.
        """
        self.logger = logging.getLogger(__name__)
        self.config = load(open('config.json'))
        self.cwd = os.path.dirname(os.getcwd())
        self.logger.info('Config loaded from config.json')

    def get_pdf_path(self):
        """
        Constructs and returns the absolute path to the PDF file as specified in the config.json file.

        Returns:
            str: The absolute path to the PDF file.
        """
        pdf_path = self.config['pdf_path']
        self.logger.info("PDF path set to {}".format(pdf_path))
        return self.cwd + pdf_path

    def get_output_path(self):
        output_path = self.config['output_path']
        self.logger.info("Output path set to {}".format(output_path))
        return self.cwd + output_path
