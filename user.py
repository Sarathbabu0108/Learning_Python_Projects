class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.current_job_title}.You can contact them at {self.email} ")


app_user_one = User("sarathbabu@gmail.com", "sarath babu", "pwd", "devops engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Devops trainer")
app_user_one.get_user_info()

app_user_two = User("sreeju.gmail.com", "sreeju", "pwd", "devops engineer")
app_user_two.get_user_info()
