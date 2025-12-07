class User:
    def __init__(self, username: str):
        self.username = username
        self.friends = []

    def add_friend(self, friend: str):
        if friend not in self.friends:
            self.friends.append(friend)
            return F"{friend} qoshildi"
        else:
            return False
        
    def remove_friend(self, friend: str):
        if friend in self.friends:
            self.friends.remove(friend)
            return True
        else:
            return False
        
    def list_friends(self):
        return self.friends
    
    def is_friend(self, friend: str):
        if friend in self.friends:
            return True
        else:
            return False
        
    def mutual_friends(self, other_user: 'User'):
        return list(set(self.friends).intersection(set(other_user.friends)))



user1 = User("Ali")
user2 = User("Vali")

print(user1.add_friend("Sami"))    # True
print(user1.add_friend("Vali"))    # True
print(user1.add_friend("Sami"))    # False (allaqachon mavjud)

print(user2.add_friend("Ali"))     # True
print(user2.add_friend("Sami"))    # True

print(user1.list_friends())   # ['Sami', 'Vali']
print(user2.list_friends())    # ['Ali', 'Sami']

print(user1.is_friend("Vali"))     # True
print(user1.is_friend("Botir"))    # False

print(user1.mutual_friends(user2)) # ['Sami']

print(user1.remove_friend("Vali")) # True
print(user1.remove_friend("Botir"))# False
print(user1.list_friends())        # ['Sami']