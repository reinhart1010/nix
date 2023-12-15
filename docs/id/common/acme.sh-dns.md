---
layout: page
title: common/acme.sh-dns (Indonesia)
description: "Gunakan verifikasi DNS-01 untuk menerbitkan sertifikat HTTPS."
content_hash: 87bbe2757a2dcc667a79d0da8c198842ee70b5b7
last_modified_at: 2023-12-15
related_topics:
  - title: বাংলা version
    url: /bn/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh-dns.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/acme.sh-dns.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># acme.sh --dns

Gunakan verifikasi DNS-01 untuk menerbitkan sertifikat HTTPS.
Informasi lebih lanjut: <https://github.com/acmesh-official/acme.sh/wiki>.

- Terbitkan sertifikat menggunakan metode verifikasi DNS via API (daftar jenis `api_dns` yang didukung tersedia dalam <https://github.com/acmesh-official/acme.sh/wiki/How-to-use-lexicon-DNS-API>):

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_dns</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Terbitkan sertifikat wildcard (ditandai dengan tanda bintang) menggunakan verifikasi DNS via API:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_dns</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- Terbitkan sertifikat menggunakan verifikasi DNS alias:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_dns</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --challenge-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias-untuk-verifikasi-example.com</span>

- Terbitkan sertifikat dengan masa tunggu pemutakhiran DNS yang ditentukan (dalam detik), sehingga `acme.sh` tidak melakukan proses validasi DNS otomatis melalui server DNS Cloudflare/Google:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_dns</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --dnssleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- Terbitkan sertifikat menggunakan verifikasi DNS manual:

`acme.sh --issue --dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --yes-I-know-dns-manual-mode-enough-go-ahead-please`
