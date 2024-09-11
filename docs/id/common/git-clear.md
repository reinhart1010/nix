---
layout: page
title: common/git-clear (Indonesia)
description: "Bersihkan isi direktori kerja Git menuju kondisi semula (seperti disalin melalui `git clone`) pada cabang saat ini, termasuk berkas-berkas yang dikecualikan menurut daftar `.gitignore`."
content_hash: 9b2fcce53645da4ea9c57a3deda0fd7c851e64ee
last_modified_at: 2024-09-11
related_topics:
  - title: English version
    url: /en/common/git-clear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clear

Bersihkan isi direktori kerja Git menuju kondisi semula (seperti disalin melalui `git clone`) pada cabang saat ini, termasuk berkas-berkas yang dikecualikan menurut daftar `.gitignore`.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-clear>.

- Setel ulang seluruh isi berkas yang dilacak oleh Git, serta hapus seluruh berkas yang tak dilacak meskipun dikecualikan menurut daftar `.gitignore`:

`git clear`
