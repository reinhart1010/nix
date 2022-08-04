---
layout: page
title: common/git-clean (Türkçe)
description: "Takip edilmeyen dosyaları çalışma ağacından sil."
content_hash: a0ca4915310b998a0b84ec9b82b4f7da78f53b3f
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
# git clean

Takip edilmeyen dosyaları çalışma ağacından sil.
Daha fazla bilgi: <https://git-scm.com/docs/git-clean>.

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
