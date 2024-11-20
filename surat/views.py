# surat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Surat
from .forms import SuratForm
import os
from django.conf import settings

def list_surat(request):
    surat = Surat.objects.all()
    return render(request, 'surat/list_surat.html', {'surat': surat})

def add_surat(request):
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_surat')
        else:
            print(form.errors)
    else:
        form = SuratForm()
    return render(request, 'surat/add_surat.html', {'form': form})

def edit_surat(request, surat_id):
    surat = get_object_or_404(Surat, id=surat_id)
    old_file = surat.file_surat.path if surat.file_surat else None  # Simpan path file lama
    
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES, instance=surat)
        if form.is_valid():
            # Cek apakah ada file baru yang diunggah
            if 'file_surat' in request.FILES:
                # Hapus file lama jika ada
                if old_file and os.path.exists(old_file):
                    os.remove(old_file)
            form.save()  # Simpan surat beserta file baru
            return redirect('list_surat')  # Kembali ke daftar surat setelah edit
    else:
        form = SuratForm(instance=surat)
    
    return render(request, 'surat/edit_surat.html', {'form': form, 'surat': surat})

def delete_surat(request, surat_id):
    surat = get_object_or_404(Surat, id=surat_id)
    surat.file_surat.delete()
    surat.delete()
    return redirect('list_surat')

def preview_file(request, surat_id):
    # Dapatkan surat berdasarkan ID
    surat = get_object_or_404(Surat, id=surat_id)
    # Kirim data surat ke template
    return render(request, 'surat/preview_file.html', {'surat': surat})
