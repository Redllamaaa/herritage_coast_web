from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to="staff_photos/", blank=True, null=True)
    show_on_homepage = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} – {self.title}"
