---
layout: page
title: linux/export (Indonesia)
description: "Ekspor variabel menuju anak-anak proses syel sistem operasi."
content_hash: f0c6728c8c56146bab23826d8bca81e2962c8fee
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/linux/export.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/export.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/export.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># export

Ekspor variabel menuju anak-anak proses syel sistem operasi.
Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Setel nilai suatu variabel lingkungan syel (environment variable):

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABEL</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nilai</span>

- Hapus nilai variabel lingkungan:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABEL</span>

- Ekspor suatu fungsi perintah (function) menuju anak-anak proses syel:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAMA_FUNGSI</span>

- Tambahkan alamat direktori baru menuju variabel lingkungan `PATH`:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/append</span>

- Tampilkan daftar variabel yang telah diekspor dalam bentuk kode perintah syel:

`export -p`
