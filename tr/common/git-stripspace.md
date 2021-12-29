---
layout: page
title: common/git-stripspace (Türkçe)
description: "Gereksiz boşlukları sil."
content_hash: fdfcc61502b11f2de56916c10a51db7f2f157075
related_topics:
  - title: English version
    url: /en/common/git-stripspace.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git stripspace

Gereksiz boşlukları sil.
Daha fazla bilgi için: <https://git-scm.com/docs/git-stripspace>.

- Gereksiz boşlukları dosyadan kırp:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>` | git stripspace`

- Gereksiz boşlukları ve Git yorumlarını dosyadan kırp:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>` | git stripspace --strip-comments`

- Bir dosyadaki tüm satırları Git yorumlarına çevir:

`git stripspace --comment-lines < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>
