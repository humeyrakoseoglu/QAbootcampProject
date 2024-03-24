import pymysql

from utils.settings import SettingKeys, Settings


def connect():
    """
    Veritabanına bağlantı oluşturur.
    """
    return pymysql.connect(host=SettingKeys.DB_HOST,
                           user=SettingKeys.DB_USER,
                           password=SettingKeys.DB_PASSWORD,
                           database=SettingKeys.DB_DATABASE)


class Database:
    def __init__(self):
        """
        Veritabanı bağlantısı için ayarları yükler.
        """
        self.settings = Settings()


class DatabaseController:
    def __init__(self):
        """
        Veritabanı denetleyicisi için bir veritabanı örneği oluşturur.
        """
        Database.__init__(self)

    @staticmethod
    def insert_data(case_name, case_path, case_status, duration, stack_trace):
        """
        Veritabanına yeni bir test raporu ekler.

        :param case_name: Testin adı
        :param case_path: Testin yolu
        :param case_status: Testin durumu
        :param duration: Testin süresi
        :param stack_trace: Testin hata izi (varsa)
        """
        db = connect()
        cursor = db.cursor()
        query = "INSERT INTO bootcampfinalprojectdb.case_reports (case_name, case_path, case_status, duration, stack_trace) VALUES (%s, %s, %s, %s, %s)"
        values = (case_name, case_path, case_status, duration, stack_trace)
        cursor.execute(query, values)
        db.commit()
        db.close()
