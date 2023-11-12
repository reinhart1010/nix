---
layout: page
title: common/git-push (Türkçe)
description: "Commit'leri uzak depoya yolla."
content_hash: 01420e9b6c2413b6d3c17766023a33339a91f68e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-push.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-push.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git push

Commit'leri uzak depoya yolla.
Daha fazla bilgi için: <https://git-scm.com/docs/git-push>.

- Mevcut daldaki yerel değişiklikleri onun uzak eşine gönder:

`git push`

- Belirtilen daldaki yerel değişiklikleri onun uzak eşine gönder:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yerel_dal</span>

- Mevcut dalı bir uzak dal ismi ayarlayarak uzak depoda yayınla:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_dal</span>

- Yerel dallardaki tüm değişiklikleri onların belirtilen uzak depodaki uzak eşlerine gönder:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>

- Uzak depodaki bir dalı sil:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_dal</span>

- Yerel eşi olmayan uzak dalları sil:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>

- Daha yzak depoda olmayan etiketleri yayınla:

`git push --tags`
