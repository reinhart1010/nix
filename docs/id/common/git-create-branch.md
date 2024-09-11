---
layout: page
title: common/git-create-branch (Indonesia)
description: "Buat suatu cabang (branch) baru dalam suatu repositori Git."
content_hash: 267b8f219354eb3f2cd6e13ab9d07eec88e1d0fb
last_modified_at: 2024-09-11
related_topics:
  - title: English version
    url: /en/common/git-create-branch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git create-branch

Buat suatu cabang (branch) baru dalam suatu repositori Git.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-create-branch>.

- Buat suatu cabang baru pada repositori lokal:

`git create-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Buat cabang baru pada repositori lokal dan sumber jarak jauh (remote) origin:

`git create-branch --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Buat cabang baru pada repositori lokal dan sumber jarak jauh (remote) upstream (yang dibentuk melalui proses pencangkokan/fork):

`git create-branch --remote upstream `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>
