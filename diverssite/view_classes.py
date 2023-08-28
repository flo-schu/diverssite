from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView


class LoggedinDetailView(UserPassesTestMixin, DetailView):
    login_url = "/users/login/"

    def test_func(self):
        """
        test function for class UserPassesTestMixin to regulate access to
        article
        """
        user = self.request.user
        object = self.model.objects.get(**self.kwargs)
        if user.is_active:
            return True
        elif object.visibility == "public":
            return True
        else:
            return False
