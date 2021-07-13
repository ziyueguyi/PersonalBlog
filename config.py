import os

File_path = os.getcwd()
m_info = {
    "user": "root",
    "password": "hzfdcj",
    "host": "localhost",
    "port": "3306",
    "database": "PersonalBlog",
    'charset': 'utf8mb4',
}


SDU = """mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}""".format(**m_info)
if __name__ == '__main__':
    print(SDU)
