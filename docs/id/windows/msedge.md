---
layout: page
title: windows/msedge (Indonesia)
description: "Aplikasi peramban web (web browser) dari Microsoft yang dibangun berdasarkan peramban Chromium yang dikembangkan oleh Google."
content_hash: f55b57d1aa453fda5380bb195042e4a741ffa9ed
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/msedge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msedge

Aplikasi peramban web (web browser) dari Microsoft yang dibangun berdasarkan peramban Chromium yang dikembangkan oleh Google.
Perintah ini tersedia sebagai `microsoft-edge` dalam perangkat selain Windows.
Catatan: Anda mungkin dapat menggunakan argumen perintah `chromium` lainnya untuk dapat mengatur jalannya Microsoft Edge.
Informasi lebih lanjut: <https://microsoft.com/edge>.

- Buka suatu URL atau berkas:

`msedge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|jalan/menuju/berkas.html</span>

- Buka dalam mode peramban privat (InPrivate):

`msedge --inprivate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dalam jendela aplikasi baru:

`msedge --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dalam mode aplikasi web (tanpa bilah toolbar, URL bar, tombol navigasi, dsb.):

`msedge --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Hubungkan peramban dengan suatu peladen proksi:

`msedge --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Buka dengan direktori profil pengguna tertentu:

`msedge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Buka dengan menonaktifkan validasi CORS (berguna untuk menguji akses suatu API):

`msedge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>` --disable-web-security`

- Selalu buka jendela alat DevTools (pembantu pengembang web) setiap kali membuka tab baru:

`msedge --auto-open-devtools-for-tabs`
