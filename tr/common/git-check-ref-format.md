---
layout: page
title: common/git-check-ref-format (Türkçe)
description: "Girilen referans isminin kabul edilebilir olup olmadığını kontrol eder, ve eğer kabul edilemezse sıfır olmayan bir çıktı verir."
content_hash: 0e8ba06ef98ee2591dddf0b55b8ece95571d483f
related_topics:
  - title: English version
    url: /en/common/git-check-ref-format.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git check-ref-format

Girilen referans isminin kabul edilebilir olup olmadığını kontrol eder, ve eğer kabul edilemezse sıfır olmayan bir çıktı verir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-check-ref-format>.

- Belirtilen referans ismini biçimini kontrol et:

`git check-ref-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/referans_ismi</span>

- Son kontrol edilen dalın ismini göster:

`git check-ref-format --branch @{-1}`

- Bir referans ismi dosyasını normalleştir:

`git check-ref-format --normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/referans_ismi</span>
