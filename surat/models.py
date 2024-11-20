# surat/models.py
from django.db import models

class Surat(models.Model):
    JENIS_SURAT = [
        ('Masuk', 'Surat Masuk'),
        ('Keluar', 'Surat Keluar'),
    ]

    jenis = models.CharField(max_length=6, choices=JENIS_SURAT)
    nomor_surat = models.CharField(max_length=100, unique=True)
    tanggal_surat = models.DateField()
    pengirim = models.CharField(max_length=100)
    penerima = models.CharField(max_length=100)
    perihal = models.TextField()
    file_surat = models.FileField(upload_to='uploads/surat/')

    def __str__(self):
        return f"{self.jenis}: {self.nomor_surat} - {self.perihal}"
