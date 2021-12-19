---
layout: page
title: osx/shuf (Indonesia)
description: "Generate permutasi acak."
content_hash: 8ad7aad692b20b3a4d7dc363df04beb6413a5e8e
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shuf.html
    icon: bi bi-globe
---
# shuf

Generate permutasi acak.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/shuf>.

- Acak urutan baris di sebuah file dan outputkan hasilnya:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Hanya mengoutputkan 5 entri dari hasil:

`shuf -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Menuliskan output ke file lain:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file_output</span>

- Men-generate angka acak dari 1-10:

`shuf -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
