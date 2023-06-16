# Instance Variable, Static V, Class V
class User:

    user_name = 'Sai Kiran'  # static  / class v
    pass_word = 'Admin'
    def get_user_details(self):
        print(User.user_name, User.pass_word)
    @classmethod
    def get_user_details2(cls):
        print(cls.user_name, cls.pass_word)

u = User()
u.get_user_details()

User.get_user_details2()
