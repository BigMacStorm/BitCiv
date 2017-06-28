# will handle the configuration data

import ConfigParser
import io


class ConfigMgr:

    def __init__(self, engine):
        self.engine = engine
        print("running config manager")
        print("loading configuration data")


        with open("config.ini") as file:
            config_file = file.read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(config_file))
