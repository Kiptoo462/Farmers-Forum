import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Victor = User(first_name = "Kiptoo",
                                last_name = "Victor",
                                username = "kiptoo462",
                                password = "Dskl321",
                                email = "kiptoovictor462@gmail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hi, run away now.",
                            user_id = self.user_Victor.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Mark.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Victor, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))