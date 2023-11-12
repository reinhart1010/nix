---
layout: page
title: osx/shuf (Indonesia)
description: "Generate permutasi acak."
content_hash: 92f0958ef6eeed31e42214c7b11cbf29078d78ad
last_modified_at: 2023-11-12
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
Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/shuf/>.

- Acak urutan baris di sebuah file dan outputkan hasilnya:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Hanya mengoutputkan 5 entri dari hasil:

`shuf -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>

- Menuliskan output ke file lain:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_file_output</span>

- Men-generate angka acak dari 1-10:

`shuf -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
