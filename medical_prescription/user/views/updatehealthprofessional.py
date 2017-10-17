# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from user.models import User
from user.forms import UpdateUserForm
from user.decorators import is_health_professional


class UpdateHealthProfessional(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'edit_health_professional.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(UpdateHealthProfessional, self).dispatch(*args, **kwargs)

    def get_success_url(self, **kwargs):
            return reverse_lazy('edit', kwargs={'pk': self.object.id})
