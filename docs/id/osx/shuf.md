---
layout: page
title: osx/shuf (Indonesia)
description: "Generate permutasi acak."
content_hash: f1e63440baf36228865ffd2f75912094f4fc817a
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/shuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/shuf.html
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

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Menuliskan output ke file lain:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file_output</span>

- Men-generate angka acak dari 1-10:

`shuf --input-range=1-10`
