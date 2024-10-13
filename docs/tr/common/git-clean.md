---
layout: page
title: common/git-clean (Türkçe)
description: "Takip edilmeyen dosyaları çalışma ağacından sil."
content_hash: c32814a90ba2e56210d4ae7f9c29270d7076a5cc
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clean

Takip edilmeyen dosyaları çalışma ağacından sil.
Daha fazla bilgi için: <https://git-scm.com/docs/git-clean>.

- Git tarafından takip edilmeyen dosyaları sil:

`git clean`

- Git tarafından takip edilmeyen dosyaları etkileşimli bir nizamda sil:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>

- Hangi dosyaların silinmeye aday olduğunu onları silmeden göster:

`git clean --dry-run`

- Git tarafından takip edilmeyen dosyaları zorla zil:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Git tarafından takip edilmeyen dizinleri zorla zil:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` -d`

- `.gitignore` ve `.git/info/exclude`'deki yoksayılan dosyalar dahiş olmak üzere takip edilmeyen dosyaları sil:

`git clean -x`
