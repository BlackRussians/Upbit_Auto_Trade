import configparser


class EasyConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def read(self, key_list, secret_key_list, watch_list, watch_coin_list):
        self.config.read("./config.ini", encoding='utf-8')
        count_API = [section for section in self.config.sections() if "API" in section]
        count_watch_coin = [section for section in self.config.sections() if "WATCH_COIN" in section]

        for i in range(len(count_API)):
            key_list.addItem(self.config[count_API[i]]["name"])
            secret_key_list.append(
                {"name": self.config[count_API[i]][self.config.options(count_API[i])[0]],
                 "API_KEY": self.config[count_API[i]][self.config.options(count_API[i])[1]],
                 "SECRET_KEY": self.config[count_API[i]][self.config.options(count_API[i])[2]]}
            )

        for i in range(len(count_watch_coin)):
            watch_list.addItem(f"코인{i + 1}")
            watch_coin_list.append(
                {"coin": self.config.options(count_watch_coin[i])[0],
                 "watch_price": float(self.config[count_watch_coin[i]][self.config.options(count_watch_coin[i])[0]])})

    def write(self):
        with open("../src/config.ini", "w", encoding='utf-8') as configFile:
            self.config.write(configFile)

    def reset(self):
        self.config = configparser.ConfigParser()
