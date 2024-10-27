---
layout: page
title: common/touch (Indonesia)
description: "Buat berkas-berkas kosong baru dan setel waktu akses dan modifikasi terhadap para berkas."
content_hash: c666f412a8aea11ccb79082afea893c3cffc0ca0
last_modified_at: 2024-10-27
related_topics:
  - title: català version
    url: /ca/common/touch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/touch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/touch.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/touch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/touch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/touch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/touch.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/touch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# touch

Buat berkas-berkas kosong baru dan setel waktu akses dan modifikasi terhadap para berkas.
Informasi lebih lanjut: <https://manned.org/touch>.

- Buat kumpulan berkas baru:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Atur informasi waktu [a]kses atau [m]odifikasi pada kumpulan berkas yang telah tersedia dalam penyimpanan, dan jangan membuat ([c]reate) berkas baru jika tak tersedia dalam penyimpanan:

`touch -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Atur informasi wak[t]u terhadap kumpulan berkas, dan jangan membuat ([c]reate) berkas baru jika tak tersedia dalam penyimpanan:

`touch -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDHHMM.SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Gunakan informasi wak[t]u atas suatu berkas referensi terhadap kumpulan berkas yang diolah, dan jangan membuat ([c]reate) berkas baru jika tak tersedia dalam penyimpanan:

`touch -c -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_referensi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>
