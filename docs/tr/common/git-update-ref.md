---
layout: page
title: common/git-update-ref (Türkçe)
description: "Git referanslarını yaratmak, güncellemek ve silmeye yarayan bir Git komutu."
content_hash: 79a80ab34d5fbd9d658e02d5427a5d0651a64c11
related_topics:
  - title: English version
    url: /en/common/git-update-ref.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-update-ref.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-update-ref.html
    icon: bi bi-globe
---
# git update-ref

Git referanslarını yaratmak, güncellemek ve silmeye yarayan bir Git komutu.
Daha fazla bilgi için: <https://git-scm.com/docs/git-update-ref>.

- Bir referansı sil (ilk commit'i hafifçe sıfırlamaya yarar):

`git update-ref -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Referansı bir mesaj ile güncelle:

`git update-ref -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mesaj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4e95e05</span>
