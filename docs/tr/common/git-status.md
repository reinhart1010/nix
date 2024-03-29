---
layout: page
title: common/git-status (Türkçe)
description: "Bir git deposundaki dosyalara yapılan değişiklikleri göster."
content_hash: 6e16453b4123473ccfedf6ab3666d588f608cb46
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-status.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-status.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-status.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git status

Bir git deposundaki dosyalara yapılan değişiklikleri göster.
Mevcut commit'e kıyasla değiştirilen, eklenen ve silinen dosyaları sıralar.
Daha fazla bilgi için: <https://git-scm.com/docs/git-status>.

- Daha commit'e eklenmemiş değiştirilen dosyaları göster:

`git status`

- Çıktıyı özetlenmiş şekilde göster:

`git status -s`

- Çıktıda izlenmeyen dosyaları gösterme:

`git status --untracked-files=no`

- Çıktıyı özetlenmiş şekilde dal bilgisiyle beraber göster:

`git status -sb`
