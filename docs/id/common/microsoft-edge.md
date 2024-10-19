---
layout: page
title: common/microsoft-edge (Indonesia)
description: "Aplikasi peramban web (web browser) dari Microsoft yang dibangun berdasarkan peramban Chromium yang dikembangkan oleh Google."
content_hash: af64500efec6a99dde1369e367fbd64b7ae7c293
last_modified_at: 2024-10-19
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/microsoft-edge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># microsoft-edge

Aplikasi peramban web (web browser) dari Microsoft yang dibangun berdasarkan peramban Chromium yang dikembangkan oleh Google.
Perintah ini tersedia sebagai `msedge` dalam perangkat Windows.
Catatan: Anda mungkin dapat menggunakan argumen perintah `chromium` lainnya untuk dapat mengatur jalannya Microsoft Edge.
Informasi lebih lanjut: <https://microsoft.com/edge>.

- Buka suatu URL atau berkas:

`microsoft-edge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|jalan/menuju/berkas.html</span>

- Buka dalam mode peramban privat (InPrivate):

`microsoft-edge --inprivate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dalam jendela aplikasi baru:

`microsoft-edge --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dalam mode aplikasi web (tanpa bilah toolbar, URL bar, tombol navigasi, dsb.):

`microsoft-edge --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Hubungkan peramban dengan suatu peladen proksi:

`microsoft-edge --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dengan direktori profil pengguna tertentu:

`microsoft-edge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Buka dengan menonaktifkan validasi CORS (berguna untuk menguji akses suatu API):

`microsoft-edge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>` --disable-web-security`

- Selalu buka jendela alat DevTools (pembantu pengembang web) setiap kali membuka tab baru:

`microsoft-edge --auto-open-devtools-for-tabs`
