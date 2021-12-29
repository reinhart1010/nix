---
layout: page
title: common/git-fetch (Türkçe)
description: "Uzak bir depodaki cisim ve referansları indir."
content_hash: 1fb1010668815536ed79ee149727b1f510684a99
related_topics:
  - title: Deutsch version
    url: /de/common/git-fetch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-fetch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-fetch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-fetch.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git fetch

Uzak bir depodaki cisim ve referansları indir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-fetch>.

- (Eğer belirtildiyse) Uzaktaki varsayılan ana akım depodan son değişiklikleri çek:

`git fetch`

- Belirtilen uzak ana akım depodan yeni dalları çek:

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>

- Uzaktaki tüm ana akım depolardaki son değişiklikleri çek:

`git fetch --all`

- Uzaktaki ana akım depodan etiketleri dahi çek:

`git fetch --tags`

- Ana akım depodan silinmiş uzak dallara giden yerel referansları sil:

`git fetch --prune`
