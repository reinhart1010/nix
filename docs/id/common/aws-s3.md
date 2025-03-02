---
layout: page
title: common/aws-s3 (Indonesia)
description: "Alat baris perintah (CLI) untuk AWS S3 - jasa penyimpanan berkas bagi layanan web."
content_hash: 55db28f4489ecb042b306a870b8478417c343604
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/aws-s3.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-s3.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-s3.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws-s3.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-s3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-s3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws s3

Alat baris perintah (CLI) untuk AWS S3 - jasa penyimpanan berkas bagi layanan web.
Beberapa subperintah seperti `cp` mempunyai dokumentasi terpisah.
Informasi lebih lanjut: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Tampilkan daftar seluruh berkas dalam suatu bucket:

`aws s3 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_bucket</span>

- Lakukan sinkronisasi isi berkas dan direktori dari sumber penyimpanan lokal menuju suatu bucket:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_bucket</span>

- Lakukan sinkronisasi isi berkas dan direktori dari suatu bucket menuju sumber penyimpanan lokal:

`aws s3 sync s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_bucket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tujuan</span>

- Lakukan sinkronisasi dengan pengecualian:

`aws s3 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>`/*`

- Hapus suatu berkas dari suatu bucket:

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Hanya tampilkan daftar berkas yang dirubah tanpa melakukan perubahan tersebut (mode dry-run):

`aws s3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` --dryrun`
