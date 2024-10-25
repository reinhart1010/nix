---
layout: page
title: common/aws (Indonesia)
description: "Alat baris perintah (CLI) resmi untuk Amazon Web Services."
content_hash: d5fc6d39dedde97a58810bf99eab3c2f4f509413
last_modified_at: 2024-10-25
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/aws.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/aws.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws

Alat baris perintah (CLI) resmi untuk Amazon Web Services.
Beberapa subperintah seperti `s3` mempunyai dokumentasi terpisah.
Informasi lebih lanjut: <https://aws.amazon.com/cli>.

- Atur penggunaan AWS Command-line secara umum:

`aws configure wizard`

- Atur penggunaan AWS Command-line menggunakan SSO:

`aws configure sso`

- Dapatkan identitas pemanggil perintah (digunakan untuk menyelesaikan permasalahan yang berkaitan dengan hak akses):

`aws sts get-caller-identity`

- Tampilkan daftar sumber daya AWS dalam suatu wilayah (region) ke dalam format YAML:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- Gunakan fitur auto prompt untuk membantu melakukan suatu perintah:

`aws iam create-user --cli-auto-prompt`

- Jalankan perintah wizard terhadap suatu sumber daya AWS:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_table</span>

- Buat suatu berkas JSON CLI Skeleton (berguna untuk mengatur infrastruktur sebagai perintah kode):

`aws dynamodb update-table --generate-cli-skeleton`

- Tampilkan bantuan terhadap suatu perintah:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` help`
