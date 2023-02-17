from django.test import TestCase
from core.models import Profile, Post, LikePost, FollowersCount, User
import datetime


class TestProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create("rumen","rumen1234","rumen@test.com")
        self.profile1 = Profile.objects.create(
             user = self.user,
             id_user = 10,
             bio = "bio1234",
             profileimg = '10-Blank-Profile-Picture-with-Hat.png',
             location = "София"  
        )

    def test_profile_str(self):
        self.assertEqual(str(self.profile), self.user.username)

    def test_profile_user(self):
        self.assertEqual(self.profile.user, self.user)

    def test_profile_id_user(self):
        self.assertEqual(self.profile.id_user, 123)

    def test_profile_bio(self):
        self.assertEqual(self.profile.bio, 'This is a test bio')

    def test_profile_location(self):
        self.assertEqual(self.profile.location, 'Test Location')

    def test_profile_profileimg(self):
        self.assertEqual(self.profile.profileimg.name, '10-Blank-Profile-Picture-with-Hat.png')

    def test_profile_str(self):
        self.assertEqual(self.user.username, "rumen")

class TestPost(TestCase):
    
    def setUp(self):
        self.post = Post.objects.create(
            id = 'e9aef3cd-3808-40cd-9132-3b5fa7e39cbe',
            user = 'ceco',
            image = '10-Blank-Profile-Picture-with-Hat.png',
            caption = 'caption test',
            created_at = datetime(2020, 1, 31, 13, 14, 31),
            no_of_likes = 10
        )

    def test_post_id(self):
        self.assertEqual(str(self.post.id), 'e9aef3cd-3808-40cd-9132-3b5fa7e39cbe')

    def test_post_user(self):
        self.assertEqual(self.post.user, 'ceco')

    def test_post_image(self):
        self.assertEqual(self.post.image, '10-Blank-Profile-Picture-with-Hat.png')

    def test_post_caption(self):
        self.assertEqual(self.post.caption, 'caption test')

    def test_post_created_at_data(self):
        self.assertEqual(self.post.created_at_data, datetime(2020, 1, 31, 13, 14, 31))

    def test_post_no_of_likes(self):
        self.assertEqual(self.post.no_of_likes, 10)

    def test_post_str(self):
        self.assertEqual(self.user, "ceco")
    
class TestLikePost(TestCase):

    def setUp(self):
        self.like_post = LikePost.objects.create(
            post_id = 'e9aef3cd-3808-40cd-9132-3b5fa7e39cbe',
            username = 'ceco'
        )

    def test_like_post_post_id(self):
        self.assertEqual(str(self.like_post.post_id), 'e9aef3cd-3808-40cd-9132-3b5fa7e39cbe')

    def test_post_like_post_username(self):
        self.assertEqual(self.like_post.username, 'ceco')

    def test_like_post_str(self):
        self.assertEqual(self.like_post.username, "ceco")

class TestFollowersCount(TestCase):

    def setUp(self):
        self.follower_count = FollowersCount.objects.create(
            follower = 'ruemn',
            user = 'ceco'
        )

    def test_follower_count_followe(self):
        self.assertEqual(self.follower_count.follower, 'e9aef3cd-3808-40cd-9132-3b5fa7e39cbe')

    def test_follower_count_user(self):
        self.assertEqual(self.follower_count.user, 'ceco')

    def test_follower_count_str(self):
        self.assertEqual(self.follower_count.user, "ceco")
