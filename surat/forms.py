# surat/forms.py
from django import forms
from .models import Surat

class SuratForm(forms.ModelForm):
    class Meta:
        model = Surat
        fields = ['jenis', 'nomor_surat', 'tanggal_surat', 'pengirim', 'penerima', 'perihal', 'file_surat']
