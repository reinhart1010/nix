---
layout: page
title: common/git-commit (Türkçe)
description: "Depoya dosya commit'le."
content_hash: 6f296045d4655a757a702320a6af9634532ac9e0
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git commit

Depoya dosya commit'le.
Daha fazla bilgi için: <https://git-scm.com/docs/git-commit>.

- Sahnelenmiş dosyaları belirtilen mesaj ile commit'le:

`git commit -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mesaj</span>

- Değişiklikleri otomatik olarak sahnele ve mesaj ile commit'le:

`git commit -a -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mesaj</span>

- Değerini değiştirecek şekilde son commit'i yeni sahnelenmiş değişiklikleri ekleyerek güncelle:

`git commit --amend`

- Yalnızca belirtilmiş (halihazırda sahnelenmiş) dosyaları commit'le:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya1 örnek/dosya2 ...</span>
