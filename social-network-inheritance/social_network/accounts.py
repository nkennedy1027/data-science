
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def __str__(self):
        return f'[<User: "{self.first_name} {self.last_name}">]'

    def add_post(self, post):
        self.posts.append(post)
        self.posts.sort(key=lambda post: post.timestamp)
        

    def get_timeline(self):
        tl = []
        for user in self.following:
            for post in user.posts:
                tl.append(post)
        return tl

    def follow(self, other):
        self.following.append(other)
