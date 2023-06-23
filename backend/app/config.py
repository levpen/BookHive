import json

CONFIG_PATH = "./config.json"


class DictObj:
    def __init__(self, in_dict: dict):
        assert isinstance(in_dict, dict)
        for key, val in in_dict.items():
            if isinstance(val, (list, tuple)):
                setattr(
                    self, key, [DictObj(x) if isinstance(x, dict) else x for x in val]
                )
            else:
                setattr(self, key, DictObj(val) if isinstance(val, dict) else val)


class Postgres:
    def __init__(self):
        self.database: str = ""
        self.user: str = ""
        self.password: str = ""
        self.host: str = ""
        self.port: int = 0


class Backend:
    def __init__(self):
        self.port: int = 8080
        self.host: str = "0.0.0.0"
        self.log_level: str = "info"


class Config:
    def __init__(self):
        self.PostgresConfig = Postgres()
        self.BackendConfig = Backend()


def get_config() -> Config:
    config_file = open(CONFIG_PATH, "r")
    config_json: dict = json.loads(config_file.read())

    config: Config = Config()
    postgres = DictObj(config_json.get("postgres"))
    backend = DictObj(config_json.get('backend'))

    # merging
    config.PostgresConfig = postgres
    config.BackendConfig = backend

    return config
