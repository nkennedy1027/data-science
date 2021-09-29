from datetime import datetime

# Please remove the comments and
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)


class Post(object):
    post_id = 0
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None
        self.id = Post.post_id
        Post.post_id += 1

    def set_user(self, user):
        self.user = user

    def __getitem__(self, item):
        return self[item]


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        Post.__init__(self, text, timestamp)

    def __str__(self):
        return (
            f'{f"@{self.user.first_name} {self.user.last_name}: " if self.user != None else ""}"{self.text}"\n'
            f'\t{self.timestamp.strftime("%A, %b %d, %Y")}'
        )
    
    def __repr__(self):
        return f'<TextPost: Post {self.id}>'


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        Post.__init__(self, text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return (
            f'{f"@{self.user.first_name} {self.user.last_name}: " if self.user != None else ""}"{self.text}"\n'
            f'\t{self.image_url}\n'
            f'\t{self.timestamp.strftime("%A, %b %d, %Y")}'
        )

    def __repr__(self):
        return f'<PicturePost: Post {self.id}>'


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        Post.__init__(self, text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return (
            f'{f"@{self.user.first_name} Checked In: " if self.user != None else ""}"{self.text}"\n'
            f'\t{self.latitude}, {self.longitude}\n'
            f'\t{self.timestamp.strftime("%A, %b %d, %Y")}'
        )
    def __repr__(self):
        return f'<CheckInPost: Post {self.id}>'

