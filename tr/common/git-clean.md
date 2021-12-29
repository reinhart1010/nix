---
layout: page
title: common/git-clean (Türkçe)
description: "Takip edilmeyen dosyaları çalışma ağacından sil."
content_hash: ba2811f42782447762b0e5180a9a628ff4ea3d25
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
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git clean

Takip edilmeyen dosyaları çalışma ağacından sil.
Daha fazla bilgi için: <https://git-scm.com/docs/git-clean>.

- Git tarafından takip edilmeyen dosyaları sil:

`git clean`

- Git tarafından takip edilmeyen dosyaları etkileşimli bir nizamda sil:

`git clean -i`

- Hangi dosyaların silinmeye aday olduğunu onları silmeden göster:

`git clean --dry-run`

- Git tarafından takip edilmeyen dosyaları zorla zil:

`git clean -f`

- Git tarafından takip edilmeyen dizinleri zorla zil:

`git clean -fd`

- `.gitignore` ve `.git/info/exclude`'deki yoksayılan dosyalar dahiş olmak üzere takip edilmeyen dosyaları sil:

`git clean -x`
