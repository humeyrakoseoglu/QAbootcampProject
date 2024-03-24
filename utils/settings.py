class SettingKeys:
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "root"
    DB_DATABASE = "bootcampFinalProjectDB"
    DB_PORT = 3306


class Settings:
    def __init__(self):
        self.DB_HOST = SettingKeys.DB_HOST
        self.DB_USER = SettingKeys.DB_USER
        self.DB_PASSWORD = SettingKeys.DB_PASSWORD
        self.DB_DATABASE = SettingKeys.DB_DATABASE
