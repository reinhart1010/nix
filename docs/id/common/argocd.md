---
layout: page
title: common/argocd (Indonesia)
description: "Program baris perintah untuk mengatur suatu peladen (server) Argo CD."
content_hash: 1c4b175b6918ff3560668719eb8ac6f44da29f6c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/argocd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/argocd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argocd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd

Program baris perintah untuk mengatur suatu peladen (server) Argo CD.
Beberapa subperintah seperti `argocd app` mempunyai dokumentasi terpisah.
Informasi lebih lanjut: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Masuk (login) ke dalam suatu peladen Argo CD:

`argocd login --insecure --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">peladen_argocd:port</span>

- Dapatkan daftar aplikasi:

`argocd app list`
