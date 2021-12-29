---
layout: page
title: common/git-stage (Türkçe)
description: "Değiştirilmiş dosyaları indekse ekle."
content_hash: 1bd2cf1cfa113209b5cab9d658df5ed727003e0e
related_topics:
  - title: English version
    url: /en/common/git-stage.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-stage.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stage.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git stage

Değiştirilmiş dosyaları indekse ekle.
Bu komut `git add`'in eş anlamlısıdır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-add>.

- İndekse bir dosya ekle:

`git stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Tüm (izlenen veya izlenmeyen) dosyaları ekle:

`git stage -A`

- Yalnızca izlenen dosyaları ekle:

`git stage -u`

- Yoksayılan dosyaları dahi ekle:

`git stage -f`

- Dosyaların parçalarını etkileşimli olarak sahnele:

`git stage -p`

- Belirtilen dosyaların parçalarını etkileşimli olarak sahnele:

`git stage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Bir dosyayı etkileşimli olarak sahnele:

`git stage -i`
