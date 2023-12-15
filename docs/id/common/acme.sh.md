---
layout: page
title: common/acme.sh (Indonesia)
description: "Sebuah shell script yang mengimplementasikan ACME client protocol (pembuat sertifikat HTTPS), alternatif dari `certbot`."
content_hash: ee540054e3d945d5e4d847a1a462fce902a5764f
last_modified_at: 2023-12-15
related_topics:
  - title: বাংলা version
    url: /bn/common/acme.sh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/acme.sh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acme.sh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/acme.sh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/acme.sh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># acme.sh

Sebuah shell script yang mengimplementasikan ACME client protocol (pembuat sertifikat HTTPS), alternatif dari `certbot`.
Lihat juga: `acme.sh dns`.
Informasi lebih lanjut: <https://github.com/acmesh-official/acme.sh>.

- Terbitkan sertifikat baru dan pasang pada webroot secara langsung:

`acme.sh --issue --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --webroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/menuju/webroot</span>

- Terbitkan sertifikat untuk domain majemuk, menggunakan mode verifikasi mandiri (standalone) pada port 80:

`acme.sh --issue --standalone --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- Terbitkan sertifikat menggunakan mode verifikasi mandiri berbasis TLS pada port 443:

`acme.sh --issue --alpn --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Terbitkan sertifikat dengan konfigurasi server Nginx untuk memasangnya:

`acme.sh --issue --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Terbitkan sertifikat dengan konfigurasi server Apache untuk memasangnya:

`acme.sh --issue --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Terbitkan sertifikat wildcard (\*) menggunakan verifikasi DNS via API (daftar jenis `api_dns` yang didukung tersedia dalam <https://github.com/acmesh-official/acme.sh/wiki/How-to-use-lexicon-DNS-API>):

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_dns</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- Pasang sertifikat ke dalam direktori tertentu (dapat berguna untuk proses pemutakhiran otomatis):

`acme.sh --install-cert -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/menuju/example.com.key</span>` --fullchain-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/menuju/example.com.cer</span>` --reloadcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"systemctl force-reload nginx"</span>
