---
layout: page
title: common/git-cherry (Türkçe)
description: "Ana depoya aktarılması gereken commit'leri bul."
content_hash: 4a12308b1e17429d4a2570188803243a4a8bf43c
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cherry.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-cherry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry

Ana depoya aktarılması gereken commit'leri bul.
Daha fazla bilgi için: <https://git-scm.com/docs/git-cherry>.

- Commit'leri (ve mesajlarını) ana akımda kendilerine tekabül eden commit'ler ile göster:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- Farklı bir ana akım ve konu dalı belirt:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>

- Commit'leri verilen sınırlamalar ile sınırla:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
