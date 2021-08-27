import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Collins = User(first_name = "Kiptoo",
                                last_name = "Victor",
                                username = "Kiptoo462",
                                password = "easy",
                                email = "kiptoovictor462@mail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hallo Welt! Ich bin hier",
                            user_id = self.user_Collins.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Collins.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Victor, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))