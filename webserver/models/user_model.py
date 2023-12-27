import bcrypt
from webserver.database.database import get_user_by_id, get_user_by_username


# User model
class User:
    def __init__(self, username, password, email, first_name, last_name, address, dob, session_token):
        if self.check_username_taken(username):
            print("Should be raising error")
            raise ValueError(f"The username '{username}' is already taken")

        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.dob = dob
        self.session_token = session_token

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    @classmethod
    def get_user(cls, user_id):
        # Fetch user data from the database
        user_data = get_user_by_id(user_id)
        if user_data:
            return cls(user_data['username'], user_data['password'], user_data['email'], user_data['first_name'],
                       user_data['last_name'], user_data['address'], user_data['dob'], user_data['session_token'])

    @classmethod
    def check_username_taken(cls, username):
        # Check if the username is taken
        user_data = get_user_by_username(username)
        return user_data is not None

    def to_json(self, include_password=False):
        return {
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'dob': self.dob,
            'password': self.password if include_password else None,
            'session_token': self.session_token
        }
