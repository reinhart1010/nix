---
layout: page
title: common/git-stripspace (Türkçe)
description: "Gereksiz boşlukları sil."
content_hash: fdfcc61502b11f2de56916c10a51db7f2f157075
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-stripspace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git stripspace

Gereksiz boşlukları sil.
Daha fazla bilgi için: <https://git-scm.com/docs/git-stripspace>.

- Gereksiz boşlukları dosyadan kırp:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>` | git stripspace`

- Gereksiz boşlukları ve Git yorumlarını dosyadan kırp:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>` | git stripspace --strip-comments`

- Bir dosyadaki tüm satırları Git yorumlarına çevir:

`git stripspace --comment-lines < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>
