import logging

class loggen:
    @staticmethod
    def log():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S Xp')

        logs = logging.getLogger()
        logs.setLevel(logging.INFO)
        return logs



