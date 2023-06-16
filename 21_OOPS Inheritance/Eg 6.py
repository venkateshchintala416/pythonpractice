# Instance V
class User:

    def get_user_details(self, user_name, user_password):

        self.uname = user_name      # instance v
        self.upass = user_password

    def display(self):
        print(self.uname, self.upass)

u = User()
u.get_user_details('sai kiran', 'admin')
u.display()
