import logging
import time as t

class L_Template():

    def __init__(self, namefile, time_in_namefile, name_logger):
        self.logger = logging.getLogger(name_logger)
        self.logger.setLevel(logging.DEBUG)
        logging.StreamHandler().setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.StreamHandler().setFormatter(self.formatter)
        self.logger.addHandler(logging.StreamHandler())
        if (time_in_namefile):
            logging.basicConfig(filename = namefile + ' ' + t.strftime("%Y%m%d-%H%M%S") + '.log', 
                                encoding='utf-8', 
                                level=logging.DEBUG
                                )
        else:
            logging.basicConfig(filename = namefile + '.log', 
                                encoding='utf-8', 
                                level=logging.DEBUG)