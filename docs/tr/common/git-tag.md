---
layout: page
title: common/git-tag (Türkçe)
description: "Etiketleri oluştur, sırala, sil veya doğrula."
content_hash: b36f06347ca918c16ff19227e8ba8cf318b7a4d1
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
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
---
# git tag

Etiketleri oluştur, sırala, sil veya doğrula.
Bir etiket, belirtilmiş bir commit'e bağlı statik bir referanstır.
Daha fazla bilgi: <https://git-scm.com/docs/git-tag>.

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
