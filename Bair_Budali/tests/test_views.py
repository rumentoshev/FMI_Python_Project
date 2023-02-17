from django import TestCase, Client
from django.urls import reverse
from core.models import Profile, Post, LikePost, FollowersCount, User
import json

class DeletePostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpass'
        )
        self.post = Post.objects.create(
            title='Test post', content='Test content', author=self.user
        )

    def test_delete_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_post'), {
            'user': self.user.username,
            'post_id': self.post.id,
        })
        self.assertRedirects(response, f'/profile/{self.user.username}/')
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='testuser1', email='testuser1@example.com', password='testpass1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2', email='testuser2@example.com', password='testpass2'
        )
        self.profile1 = Profile.objects.create(
            user=self.user1, bio='Test bio', image='test.jpg'
        )
        self.profile2 = Profile.objects.create(
            user=self.user2, bio='Test bio', image='test.jpg'
        )
        self.post1 = Post.objects.create(
            title='Test post 1', content='Test content', user=self.user1
        )
        self.post2 = Post.objects.create(
            title='Test post 2', content='Test content', user=self.user1
        )
        self.post3 = Post.objects.create(
            title='Test post 3', content='Test content', user=self.user2
        )
        self.followers_count = FollowersCount.objects.create(
            user=self.user1.username, follower=self.user2.username
        )

    def test_profile_authenticated(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('profile', args=[self.user1.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertEqual(response.context['user_object'], self.user1)
        self.assertEqual(response.context['user_profile'], self.profile1)
        self.assertQuerysetEqual(
            response.context['user_posts'], [repr(self.post1), repr(self.post2)], ordered=False
        )
        self.assertEqual(response.context['user_post_lenght'], 2)
        self.assertEqual(response.context['button_text'], 'Последвай')
        self.assertEqual(response.context['user_followers'], 1)
        self.assertEqual(response.context['user_following'], 0)

    def test_profile_unauthenticated(self):
        response = self.client.get(reverse('profile', args=[self.user1.username]))
        self.assertRedirects(
            response, f'/signin/?next={reverse("profile", args=[self.user1.username])}'
        )

    def test_profile_follow_button_text(self):
        self.client.login(username='testuser2', password='testpass2')
        response = self.client.get(reverse('profile', args=[self.user1.username]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['button_text'], 'Отследвай')

    def test_profile_follow_counts(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('profile', args=[self.user1.username]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user_followers'], 1)
        self.assertEqual(response.context['user_following'], 0)

        self.client.login(username='testuser2', password='testpass2')
        response = self.client.get(reverse('profile', args=[self.user2.username]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user_followers'], 0)
        self.assertEqual(response.context['user_following'], 1)