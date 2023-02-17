from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import index, settings, upload, follow, search, delete_post, profile, like_post, like_post_prof, signin, signup, logout



class TestUrls(SimpleTestCase):
    
    def test_index_is_resolves(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEqual(resolve(url).func,index)

    def test_settings_is_resolves(self):
        url = reverse('settings')
        print(resolve(url))
        self.assertEqual(resolve(url).func,settings)
    
    def test_upload_is_resolves(self):
        url = reverse('upload')
        print(resolve(url))
        self.assertEqual(resolve(url).func,upload)

    def test_follow_is_resolves(self):
        url = reverse('follow')
        print(resolve(url))
        self.assertEqual(resolve(url).func,follow)

    def test_search_is_resolves(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEqual(resolve(url).func,search)
    
    def test_delete_post_is_resolves(self):
        url = reverse('delete_post')
        print(resolve(url))
        self.assertEqual(resolve(url).func,delete_post)

    def test_profile_is_resolves(self):
        url = reverse('profile',args=['some-str'])
        print(resolve(url))
        self.assertEqual(resolve(url).func,profile)

    def test_signup_is_resolves(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEqual(resolve(url).func,signup)

    def test_signin_is_resolves(self):
        url = reverse('signin')
        print(resolve(url))
        self.assertEqual(resolve(url).func,signin)

    def test_logout_is_resolves(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEqual(resolve(url).func,logout)

    def test_like_post_is_resolves(self):
        url = reverse('like-post')
        print(resolve(url))
        self.assertEqual(resolve(url).func,like_post)

    def test_like_post_prof_is_resolves(self):
        url = reverse('like-post-prof')
        print(resolve(url))
        self.assertEqual(resolve(url).func,like_post_prof)