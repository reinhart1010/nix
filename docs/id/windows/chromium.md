---
layout: page
title: windows/chromium (Indonesia)
description: "Aplikasi peramban web (web browser) bersumber terbuka yang terutama dikembangkan dan dikelola oleh Google."
content_hash: 5d76c085700194f0b76a0898673a8244f1562c46
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/chromium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chromium

Aplikasi peramban web (web browser) bersumber terbuka yang terutama dikembangkan dan dikelola oleh Google.
Catatan: Anda mungkin perlu menggantikan perintah `chromium` dengan peramban tujuan Anda, seperti `brave`, `google-chrome`. `microsoft-edge`/`msedge`, `opera`, atau `vivaldi`.
Informasi lebih lanjut: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Buka suatu URL atau berkas:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|jalan/menuju/berkas.html</span>

- Buka dalam mode peramban privat (incognito) (gunakan `--inprivate` untuk Microsoft Edge):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chromium --incognito|msedge --inprivate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

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
