---
layout: page
title: common/git-tag (Türkçe)
description: "Etiketleri oluştur, sırala, sil veya doğrula."
content_hash: 590b8dbb90fe6270e324f0a852d481acf51dd1f4
last_modified_at: 2024-06-21
related_topics:
  - title: Deutsch version
    url: /de/common/git-tag.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-tag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-tag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-tag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-tag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git tag

Etiketleri oluştur, sırala, sil veya doğrula.
Bir etiket, belirtilmiş bir commit'e bağlı statik bir referanstır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-tag>.

- Tüm etiketleri sırala:

`git tag`

- Belirtilen isim ile mevcut commit'e bağlı bir etiket yarat:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket_ismi</span>

- Belirtilen isim ile belirtilen commit'e bağlı bir etiket yarat:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Belirtilen mesaja sahip açıklamalı bir etiket yarat:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket_ismi</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket_mesajı</span>

- Belirtilen isimdeki etiketi sil:

`git tag -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket_ismi</span>

- Ana projeden güncellenmiş etiketleri al:

`git fetch --tags`

- Belirtilen commit'i içeren/içermiş tüm etiketleri sırala:

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
