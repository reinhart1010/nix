---
layout: page
title: common/asciidoctor (Indonesia)
description: "Ubah isi berkas AsciiDoc ke dalam format berkas layak publikasi."
content_hash: fb88429d505affc7428ac5091094ade73d523139
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciidoctor.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciidoctor.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/asciidoctor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciidoctor

Ubah isi berkas AsciiDoc ke dalam format berkas layak publikasi.
Informasi lebih lanjut: <https://docs.asciidoctor.org>.

- Ubah suatu berkas `.adoc` ke dalam format HTML (format berkas luaran secara default):

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.adoc</span>

- Ubah suatu berkas `.adoc` ke dalam format HTML dengan menggunakan suatu berkas definisi penggayaan (stylesheet) CSS:

`asciidoctor -a stylesheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/stylesheet.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.adoc</span>

- Ubah suatu berkas `.adoc` menuju format HTML layak semat (embeddable), hanya bangunkan isi tag body HTML:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.adoc</span>

- Ubah suatu berkas `.adoc` menuju PDF melalui pustaka pendukung `asciidoctor-pdf`:

`asciidoctor --backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.adoc</span>
