---
layout: page
title: freebsd/base64 (Indonesia)
description: "Lakukan pengodean dan pendekodean terhadap suatu berkas atau `stdin` dari/menuju format Base64, menuju `stdout` atau berkas lainnya."
content_hash: 77d163d3b9005a4b4c99c169f2e643168525f2bb
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/freebsd/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

Lakukan pengodean dan pendekodean terhadap suatu berkas atau `stdin` dari/menuju format Base64, menuju `stdout` atau berkas lainnya.
Informasi lebih lanjut: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Kodekan isi suatu berkas menuju format Base64, dan keluarkan hasil menuju `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Kodekan isi suatu berkas menuju format Base64, dan keluarkan hasil menuju suatu berkas luaran/output:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_output</span>

- Bungkus luaran Base64 dalam panjang karakter yang tetap (nilai `0` akan menonaktifkan pembungkusan):

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--break</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|76|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Dekodekan kode Base64 yang tersimpan dalam suatu berkas, dan keluarkan hasil menuju `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Kodekan isi dari `stdin` menuju `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` | base64`

- Dekodekan kode Base64 yang berasal dari `stdin` menuju `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` | base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>
