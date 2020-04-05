from django.contrib.auth.hashers import make_password, check_password
import os ,django

class Student():
    s_name=""
    _s_password=""

    @property
    def s_password(self):
        print("获取")

        return self._s_password

    @s_password.setter
    def s_password(self,password):
        print("设置")
        #密码加密
        self._s_password=make_password(password)

    # def __init__(self,s_name,s_password):
    #     pass

    def verify_password(self,password):
        return  check_password(password,self._s_password)

if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoDay8.settings")  # project_name 项目名称
    django.setup()
    s=Student()
    s.s_name="Rock"
    s.s_password="1234"
    # print(s.s_name)
    print(s.verify_password("1234"))
    print(s.s_password)
