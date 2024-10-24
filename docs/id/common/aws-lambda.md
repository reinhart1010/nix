---
layout: page
title: common/aws-lambda (Indonesia)
description: "Gunakan AWS Lambda, suatu layanan komputasi untuk menjalankan kode perintah tanpa membuat atau mengatur infrastruktur peladen."
content_hash: 123b8342201aa62192bd9509599fb4e5a092bed7
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/common/aws-lambda.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-lambda.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-lambda.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-lambda.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-lambda.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws lambda

Gunakan AWS Lambda, suatu layanan komputasi untuk menjalankan kode perintah tanpa membuat atau mengatur infrastruktur peladen.
Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Jalankan suatu function:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/respons.json</span>

- Jalankan suatu function dengan payload masukan (input) dalam format JSON:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` --payload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/respons.json</span>

- Tampilkan daftar function yang tersedia:

`aws lambda list-functions`

- Tampilkan informasi konfigurasi mengenai suatu function:

`aws lambda get-function-configuration --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>

- Tampilkan daftar alias yang didaftarkan terhadap suatu function:

`aws lambda list-aliases --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>

- Tampilkan informasi konfigurasi konkurensi yang dicadangkan (reserved concurrency) terhadap suatu function:

`aws lambda get-function-concurrency --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>

- Tampilkan daftar layanan AWS yang berhak memanggil suatu function:

`aws lambda get-policy --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>
