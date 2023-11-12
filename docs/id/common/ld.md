---
layout: page
title: common/ld (Indonesia)
description: "Menghubungkan file-file obyek berbarengan."
content_hash: 649171a07b8466e5b8b57f9e81c1d4c543aeb0a0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ld.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ld

Menghubungkan file-file obyek berbarengan.
Informasi lebih lanjut: <https://sourceware.org/binutils/docs-2.38/ld.html>.

- Menghubungkan file obyek tertentu yang tidak memiliki kebergantungan ke suatu executable:

`ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.o</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/output_executable</span>

- Menghubungkan 2 file obyek berbarengan:

`ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file1.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file2.o</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/output_executable</span>

- Menghubungkan secara dinamis sebuah program x86_64 ke glibc (jalan-jalan file berubah bergantung pada sistem):

`ld --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/output_executable</span>` --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.o</span>` /lib/crtn.o`
