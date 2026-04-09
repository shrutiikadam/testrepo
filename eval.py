class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.history = []

    def is_adult(self) -> bool:
        return self.age >= 18

    def add_activity(self, activity: str):
        self.history.append(activity)
        self._log_activity(activity)

    def _log_activity(self, activity: str):
        print(f"{self.name} did {activity}")
        self._update_stats(activity)

    def _update_stats(self, activity: str):
        if self.is_adult():
            self._adult_stats(activity)
        else:
            self._minor_stats(activity)

    def _adult_stats(self, activity: str):
        print("Adult activity:", activity)

    def _minor_stats(self, activity: str):
        print("Minor activity:", activity)


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)
        self._validate_user(user)

    def _validate_user(self, user: User):
        if not user.name:
            raise ValueError("Invalid user")
        self._process_user(user)

    def _process_user(self, user: User):
        if user.is_adult():
            self._handle_adult(user)
        else:
            self._handle_minor(user)

    def _handle_adult(self, user: User):
        user.add_activity("driving")

    def _handle_minor(self, user: User):
        user.add_activity("school")


def process_users(users):
    manager = UserManager()
    for user in users:
        manager.add_user(user)


def create_users():
    u1 = User("Alice", 25)
    u2 = User("Bob", 15)
    return [u1, u2]


def main():
    users = create_users()
    process_users(users)


if __name__ == "__main__":
    main()
