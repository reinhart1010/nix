---
layout: page
title: common/rsync (Indonesia)
description: "Transfer file ke atau dari sebuah _remote host_ (bukan di antara 2 _remote host_)."
content_hash: 4221f83f47dc52a17be9b018c59cebe65506a92a
last_modified_at: 2023-08-07
related_topics:
  - title: English version
    url: /en/common/rsync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rsync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rsync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rsync.html
    icon: bi bi-globe
---
# rsync

Transfer file ke atau dari sebuah _remote host_ (bukan di antara 2 _remote host_).
Bisa transfer satuan file, maupun beberapa file yang sesuai dengan pola tertentu.
Informasi lebih lanjut: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfer file dari lokal ke _remote host_:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/file_lokal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_directory</span>

- Transfer file dari _remote host_ ke lokal:

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/direktori_lokal</span>

- Transfer file dalam mode [a]rsip (untuk menyimpan atribut-atribut) dan terkompres (_[z]ipped_) secara _[v]erbose_ dan progresnya dapat dibaca orang (_[h]uman-readable [P]rogress_):

`rsync -azvhP `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/file_lokal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_directory</span>

- Transfer direktori dan semua isiny dari remote ke lokal:

`rsync -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/direktori_lokal</span>

- Transfer isi direktori (namun bukan direktori itu sendiri) dari remote ke lokal:

`rsync -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_directory</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/direktori_lokal</span>

- Transfer direktori secara [r]ecursif, dalam [a]rsip (untuk menyimpan atribut-atribut), menyelesaikan _soft[l]inks_ yang terkandung di sana, dan mengabaikan file-file yang sudah ditransfer kecuali jika file itu lebih baru (_[u]nless newer_):

`rsync -rauL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/direktori_lokal</span>

- Transfer file melalui SSH dan hapus file-file lokal yang tidak ada di _remote host_:

`rsync -e ssh --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/file_lokal</span>

- Transfer file melalui SSH dengan menggunakan port yang yang berbeda dari bawaan dan tampilkan progres global:

`rsync -e 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/remote_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi/ke/file_lokal</span>
