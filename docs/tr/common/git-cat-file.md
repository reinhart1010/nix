---
layout: page
title: common/git-cat-file (Türkçe)
description: "Git depo cisimlerine dair içerik, tür ve boyut bilgisini sağla."
content_hash: 4634e277ea1758e8f7eae007f39847ecf6d1530e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-cat-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cat-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cat-file.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cat-file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cat-file

Git depo cisimlerine dair içerik, tür ve boyut bilgisini sağla.
Daha fazla bilgi için: <https://git-scm.com/docs/git-cat-file>.

- HEAD commit'inin byte bazında boyutunu öğren:

`git cat-file -s HEAD`

- Belirtilen Git cisminin türünü (blob, ağaç, commit, etiket) öğren:

`git cat-file -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8c442dc3</span>

- Git objesinin içeriğini, türüne uygun olarak hoş şekilde yansıt:

`git cat-file -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>
