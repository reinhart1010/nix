---
layout: page
title: common/chromium (Indonesia)
description: "Aplikasi peramban web (web browser) bersumber terbuka yang terutama dikembangkan dan dikelola oleh Google."
content_hash: 0944bf368dce71ed02ce0b66cb4e2969191a22f6
last_modified_at: 2024-10-19
related_topics:
  - title: Deutsch version
    url: /de/common/chromium.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chromium.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chromium.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chromium.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chromium.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chromium.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chromium.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chromium.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chromium

Aplikasi peramban web (web browser) bersumber terbuka yang terutama dikembangkan dan dikelola oleh Google.
Catatan: Anda mungkin perlu menggantikan perintah `chromium` dengan peramban tujuan Anda, seperti `brave`, `google-chrome`, `opera`, atau `vivaldi`.
Informasi lebih lanjut: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Buka suatu URL atau berkas:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|jalan/menuju/berkas.html</span>

- Buka dalam mode peramban privat (incognito):

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dalam jendela aplikasi baru:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dalam mode aplikasi web (tanpa bilah toolbar, URL bar, tombol navigasi, dsb.):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Hubungkan peramban dengan suatu peladen proksi:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dengan direktori profil pengguna tertentu:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Buka dengan menonaktifkan validasi CORS (berguna untuk menguji akses suatu API):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>` --disable-web-security`

- Selalu buka jendela alat DevTools (pembantu pengembang web) setiap kali membuka tab baru:

`chromium --auto-open-devtools-for-tabs`
