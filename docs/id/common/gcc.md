---
layout: page
title: common/gcc (Indonesia)
description: "Praproses dan kompilasi kode sumber C dan C++, lalu rakit dan gabungkan bersama-sama."
content_hash: f38e4868c2cf5772b2a6f0fee5fa0f47e90091f3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/gcc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gcc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gcc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcc

Praproses dan kompilasi kode sumber C dan C++, lalu rakit dan gabungkan bersama-sama.
Informasi lebih lanjut: <https://gcc.gnu.org>.

- Mengubah beberapa sumber kode menjadi program:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sumber1.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sumber2.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Mengizinkan peringatan dan simbol debug di output:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sumber.c</span>` -Wall -Og --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Menyertakan pustaka dari direktori yang berbeda:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sumber.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalur_header</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalur_pustaka</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pustaka</span>

- Mengkompilasi kode sumber ke dalam bahasa tingkat rendah (assembly):

`gcc -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sumber.c</span>

- Mengkompilasi kode sumber tanpa digabungkan:

`gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sumber.c</span>
