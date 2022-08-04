---
layout: page
title: common/git-cherry (Türkçe)
description: "Ana depoya aktarılması gereken commit'leri bul."
content_hash: 1b56ae57c4181a616465f997156ce71df07e39aa
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
---
# git cherry

Ana depoya aktarılması gereken commit'leri bul.
Daha fazla bilgi: <https://git-scm.com/docs/git-cherry>.

- Commit'leri (ve mesajlarını) ana akımda kendilerine tekabül eden commit'ler ile göster:

`git cherry -v`

- Farklı bir ana akım ve konu dalı belirt:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>

- Commit'leri verilen sınırlamalar ile sınırla:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
