---
layout: page
title: common/yes (Türkçe)
description: "Bir şeyi tekrar tekrar yazdır."
content_hash: ab1faee9565ed6e612cf268cdbf26fee3fe4f0ba
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yes.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/yes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yes.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yes.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yes

Bir şeyi tekrar tekrar yazdır.
Bu komut genelde yükleme işlemleri sırasında onay için yes yazmak için kullanılır (apt-get gibi).
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- Tekrar tekrar "mesaj" yazdır:

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mesaj</span>

- Tekrar tekrar "y" yazdır:

`yes`

- `apt-get` komutu tarafından sorulan her şeyi kabul et:

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
