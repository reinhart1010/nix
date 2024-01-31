---
layout: page
title: osx/shuf (Indonesia)
description: "Generate permutasi acak."
content_hash: b795e36cfeb012aeb0343bd263441e5621c14445
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/shuf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

Generate permutasi acak.
Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/shuf.1.html>.

- Acak urutan baris di sebuah file dan outputkan hasilnya:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Hanya mengoutputkan 5 entri dari hasil:

`shuf --head-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Menuliskan output ke file lain:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file_output</span>

- Men-generate angka acak dari 1-10:

`shuf --input-range=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
