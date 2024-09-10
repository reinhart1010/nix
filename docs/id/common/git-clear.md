---
layout: page
title: common/git-clear (Indonesia)
description: "Bersihkan isi direktori kerja Git menuju kondisi semula (seperti disalin melalui `git clone`) pada cabang saat ini, termasuk berkas-berkas yang dikecualikan menurut daftar `.gitignore`."
content_hash: 9b2fcce53645da4ea9c57a3deda0fd7c851e64ee
last_modified_at: 2024-09-10
related_topics:
  - title: English version
    url: /en/common/git-clear.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-clear.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git clear

Bersihkan isi direktori kerja Git menuju kondisi semula (seperti disalin melalui `git clone`) pada cabang saat ini, termasuk berkas-berkas yang dikecualikan menurut daftar `.gitignore`.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-clear>.

- Setel ulang seluruh isi berkas yang dilacak oleh Git, serta hapus seluruh berkas yang tak dilacak meskipun dikecualikan menurut daftar `.gitignore`:

`git clear`
