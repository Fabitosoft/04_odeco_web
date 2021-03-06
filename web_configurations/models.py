from django.db import models
from solo.models import SingletonModel
from tinymce import HTMLField
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import SmartResize, ResizeToFit

from web.utils import get_image_name


class IndexConfiguration(SingletonModel):
    def header_imagen_upload_to(instance, filename):
        new_filename = get_image_name('Header', filename)
        return "web/img/index/%s" % new_filename

    def overlay_publicidad_imagen_upload_to(instance, filename):
        new_filename = get_image_name('Overlay', filename)
        return "web/img/index/%s" % new_filename

    header_titulo = models.CharField(max_length=150, default='Aqui el titulo')
    header_text = models.TextField(max_length=150, default='Aqui la descripción', null=True, blank=True)
    header_text_en = models.TextField(max_length=150, default='Aqui la descripción Ingles', null=True, blank=True)
    header_imagen = ProcessedImageField(
        processors=[SmartResize(width=2560, height=1500, upscale=False)],
        format='JPEG',
        options={'quality': 50},
        upload_to=header_imagen_upload_to,
        verbose_name='Imagen Cabezote (2560 x 1500)',
        null=True,
        blank=True
    )
    header_imagen_normal = ImageSpecField(
        processors=[SmartResize(width=1280, height=750, upscale=False)],
        options={'quality': 50},
        source='header_imagen',
        format='JPEG'
    )
    header_imagen_webp = ImageSpecField(
        processors=[SmartResize(width=1280, height=750, upscale=False)],
        options={'quality': 50},
        source='header_imagen',
        format='WEBP'
    )
    header_imagen_cell = ImageSpecField(
        source='header_imagen',
        processors=[SmartResize(width=412, height=660, upscale=False)],
        format='JPEG'
    )
    header_imagen_cell_webp = ImageSpecField(
        source='header_imagen',
        processors=[SmartResize(width=412, height=660, upscale=False)],
        format='WEBP'
    )
    overlay_publicidad = ProcessedImageField(
        processors=[ResizeToFit(width=1024, height=768, upscale=False)],
        format='JPEG',
        options={'quality': 70},
        upload_to=overlay_publicidad_imagen_upload_to,
        verbose_name='Imagen Overlay Publicidad (1024 x 768)',
        null=True,
        blank=True
    )
    overlay_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return "Index"

    class Meta:
        verbose_name = "Index"


class CasosExitoConfiguration(SingletonModel):
    def header_imagen_upload_to(instance, filename):
        new_filename = get_image_name('Header', filename)
        return "web/img/casexi/%s" % new_filename

    header_text = models.TextField(max_length=150, verbose_name='Titulo', default='Aqui la descripción', null=True,
                                   blank=True)
    header_text_en = models.TextField(max_length=150, verbose_name='Titulo Ingles', null=True, blank=True)
    header_imagen = ProcessedImageField(
        processors=[SmartResize(width=2560, height=1500, upscale=False)],
        format='JPEG',
        options={'quality': 50},
        upload_to=header_imagen_upload_to,
        verbose_name='Imagen Cabezote (2560 x 1500)',
        null=True,
        blank=True
    )
    descripcion = HTMLField('Texto Casos Éxito', default='Descripción casos Éxito', null=True, blank=True)
    descripcion_en = HTMLField('Texto Casos Éxito Ingles', null=True, blank=True)

    def __unicode__(self):
        return "Casos Exito"

    class Meta:
        verbose_name = "Casos Exito"


class GeneralConfiguration(SingletonModel):
    direccion = models.CharField(max_length=200, default='Dirección aquí', verbose_name='Dirección')
    horarios_de_atencion = HTMLField('Horarios de Atención', default='Texto Horarios de Atención aquí')
    horarios_de_atencion_en = HTMLField('Horarios de Atención Ingles', default='Texto Horarios de Atención aquí')
    numeros_contacto = HTMLField('Numeros de Contacto', default='Numeros de contacto', null=True, blank=True)
    correos_contacto = HTMLField('Correos de Contacto', default='Correos de contacto', null=True, blank=True)
    texto_habeas_data = HTMLField('Habeas Data', default='Información Habeas Data', null=True, blank=True)
    texto_habeas_data_en = HTMLField('Habeas Data Ingles', default='Información Habeas Data', null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    whatsaap = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    version_css_cache = models.CharField(max_length=20, default='')

    def __unicode__(self):
        return "General"

    class Meta:
        verbose_name = "General"


class LaEmpresaConfiguration(SingletonModel):
    def imagen_principal_upload_to(instance, filename):
        new_filename = get_image_name('La Empresa Principal', filename)
        return "web/img/empr/%s" % new_filename

    titulo = models.CharField(max_length=150, default='Aqui el titulo')
    texto = HTMLField('Descripcion Empresa', default='Aqui la descripción')
    texto_en = HTMLField('Descripcion Empresa Ingles', default='Aqui la descripción en ingles')
    imagen_principal = ProcessedImageField(
        processors=[SmartResize(width=570, height=362, upscale=False)],
        format='JPEG',
        options={'quality': 70},
        upload_to=imagen_principal_upload_to,
        verbose_name='Imagen Principal (570x362)',
        null=True,
        blank=True
    )
    video = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return "La Empresa"

    class Meta:
        verbose_name = "La Empresa"


class CacheConfiguration(SingletonModel):
    empresa_update = models.DateTimeField(null=True, blank=True)
    soluciones_update = models.DateTimeField(null=True, blank=True)
    clientes_update = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return "Caches Index"

    class Meta:
        verbose_name = "Cache Index"
