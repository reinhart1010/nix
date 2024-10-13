---
layout: page
title: common/git-reflog (Türkçe)
description: "HEAD, dal ve etiketler gibi yerel referansların geçirdiği değişimlerin kaydını göster."
content_hash: 8d8f3fff4b65117714ca15b6f883780cfd289be4
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-reflog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reflog

HEAD, dal ve etiketler gibi yerel referansların geçirdiği değişimlerin kaydını göster.
Daha fazla bilgi için: <https://git-scm.com/docs/git-reflog>.

- HEAD için referans kaydını göster:

`git reflog`

- Belirtilen dal için referans kaydını göster:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Referans kaydında sadece son 5 değişimi göster:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--max-count</span>` 5`
