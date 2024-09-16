---
layout: page
title: common/ruby (Indonesia)
description: "Interpreter bahasa pemrograman Ruby."
content_hash: 6e5f163c46c2caaee7c20e38bb68d577cda6dd1a
last_modified_at: 2024-09-16
related_topics:
  - title: English version
    url: /en/common/ruby.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ruby.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ruby.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ruby

Interpreter bahasa pemrograman Ruby.
Informasi lebih lanjut: <https://www.ruby-lang.org>.

- Jalankan suatu berkas skrip atau program Ruby:

`ruby `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/skrip.rb</span>

- Jalankan suatu perintah Ruby dalam command-line:

`ruby -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Periksa kesalahan sintaks dari suatu berkas skrip Ruby:

`ruby -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/skrip.rb</span>

- Jalankan program peladen (server) HTTP bawaan terrhadap direktori saat ini menuju port 8080:

`ruby -run -e httpd`

- Jalankan suatu berkas biner program Ruby tanpa memasang suatu pustaka (library) pendukung yang diwajibkan:

`ruby -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_pustaka</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pustaka_yang_dikecualikan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_bin/nama_berkas_bin</span>

- Tampilkan [v]ersi Ruby saat ini:

`ruby -v`
