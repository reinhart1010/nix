---
layout: page
title: osx/osascript (Indonesia)
description: "Jalankan AppleScript atau JavaScript for Automation (JXA) dari command-line."
content_hash: dac0802a3ba080dc9d6f864014fbdf3074df407e
related_topics:
  - title: English version
    url: /en/osx/osascript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/osascript.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># osascript

Jalankan AppleScript atau JavaScript for Automation (JXA) dari command-line.
Informasi lebih lanjut: <https://ss64.com/osx/osascript.html>.

- Menjalankan sebuah perintah AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Halo dunia'</span>`"`

- Menjalankan beberapa perintah AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Halo'</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'dunia'</span>`"`

- Mengeksekusi perintah dari file AppleScript yang telah terkompilasi (`*.scpt`), terbundel (`*.scptd`), atau secara plaintext (`*.applescript`):

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/apple.scpt</span>

- Mendapatkan ID pengenal (bundle identifier) dari sebuah aplikasi (dapat digunakan untuk perintah `open -b`):

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Aplikasi</span>`"'`

- Menjalankan sebuah perintah JavaScript:

`osascript -l JavaScript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log('Halo dunia');</span>`"`

- Mengeksekusi perintah dari file JavaScript:

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/javascript.js</span>
