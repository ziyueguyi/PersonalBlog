import os

File_path = os.getcwd()
m_info = {
    "user": "root",
    "password": ".ai94264744946",
    "host": "localhost",
    "port": "3306",
    "database": "PersonalBlog"}
SDU = "mysql://" + m_info["user"] + ":" + m_info["password"] + "@" + \
      m_info["host"] + ":" + m_info["port"] + "/" + m_info["database"]
