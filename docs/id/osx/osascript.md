---
layout: page
title: osx/osascript (Indonesia)
description: "Jalankan AppleScript atau JavaScript for Automation (JXA) dari command-line."
content_hash: 29390f48a48fc0a9fe1fdcac1642e71473c48847
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/osx/osascript.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/osascript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/osascript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# osascript

Jalankan AppleScript atau JavaScript for Automation (JXA) dari command-line.
Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/osascript.1.html>.

- Jalankan sebuah perintah AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Halo dunia'</span>`"`

- Jalankan beberapa perintah AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Halo'</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'dunia'</span>`"`

- Mengeksekusi perintah dari file AppleScript yang telah terkompilasi (`*.scpt`), terbundel (`*.scptd`), atau secara plaintext (`*.applescript`):

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/apple.scpt</span>

- Mendapatkan ID pengenal (bundle identifier) dari sebuah aplikasi (dapat digunakan untuk perintah `open -b`):

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Aplikasi</span>`"'`

- Jalankan sebuah perintah JavaScript:

`osascript -l JavaScript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log('Halo dunia');</span>`"`

- Mengeksekusi perintah dari file JavaScript:

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/javascript.js</span>
