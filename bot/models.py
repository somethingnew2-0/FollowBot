from django.db import models

# Create your models here.
class Keywords(models.Model):

    user = models.OneToOneField(get_user_model(), unique=True,
        related_name='profile')

    # Extra attributes ...

    def __unicode__(self):
        return "{0}'s profile".format(self.user)