---
layout: page
title: common/argocd (Indonesia)
description: "Program baris perintah untuk mengatur suatu peladen (server) Argo CD."
content_hash: 34bcd5fa788249a6a34ce5d3058e3ac36d96112f
last_modified_at: 2024-06-18
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/argocd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># argocd

Program baris perintah untuk mengatur suatu peladen (server) Argo CD.
Beberapa subperintah seperti `argocd app` memiliki dokumentasi terpisah.
Informasi lebih lanjut: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Masuk (login) ke dalam suatu peladen Argo CD:

`argocd login --insecure --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">peladen_argocd:port</span>

- Dapatkan daftar aplikasi:

`argocd app list`
