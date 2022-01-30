---
layout: page
title: common/git-reflog (Türkçe)
description: "HEAD, dal ve etiketler gibi yerel referansların geçirdiği değişimlerin kaydını göster:"
content_hash: c1863eeb991a1af436537a963c86dfdea41614b3
related_topics:
  - title: English version
    url: /en/common/git-reflog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reflog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reflog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reflog.html
    icon: bi bi-globe
---
# git reflog

HEAD, dal ve etiketler gibi yerel referansların geçirdiği değişimlerin kaydını göster:
Daha fazla bilgi: <https://git-scm.com/docs/git-reflog>.

- HEAD için referans kaydını göster:

`git reflog`

- Belirtilen dal için referans kaydını göster:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Referans kaydında sadece son 5 değişimi göster:

`git reflog -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
