from django.db import models


class Category(models.Model):
    title = models.CharField('Kategori Adı', max_length=100)
   # desc = models.CharField('Kategori Açıklaması', max_length=250)
    created_at = models.DateTimeField("Oluşturma Tarihi", null=False, blank=True, auto_now=True)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return str(self.title)


class Survey(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField('Araştırma Adı', max_length=100)
    created_at = models.DateTimeField('Oluşturulma Tarihi', null=True, blank=True, auto_now=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', null=True, blank=True, auto_now_add=True)
    active = models.BooleanField('Aktif mi?', null=False, blank=False, default=False)

    class Meta:
        verbose_name = 'Araştırma'
        verbose_name_plural = 'Araştırmalar'

    def __str__(self):
        return str(self.name)



