---
layout: page
title: common/git-pull (Türkçe)
description: "Uzak bir depodan dal getir ve yerel depo ile birleştir."
content_hash: 98df5a56c22d99565a032ed7185cb50d4e7e7d79
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
---
# git pull

Uzak bir depodan dal getir ve yerel depo ile birleştir.
Daha fazla bilgi: <https://git-scm.com/docs/git-pull>.

- Varsayılan uzak depodan değişiklikleri indir ve birleştir:

`git pull`

- Varsayılan uzak depodan değişiklikleri indir ve ileri sarmayı kullan:

`git pull --rebase`

- Belirtilen uzak depodan ve daldan değişiklikleri indir, ve sonra onları HEAD ile birleştir:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal</span>
