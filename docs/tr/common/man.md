---
layout: page
title: common/man (Türkçe)
description: "Kılavuz sayfalarını biçimlendir ve göster."
content_hash: be5249a3d2e9bb1db1a8e703c10e2325ea3031c1
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/man.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/man.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/man.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/man.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># man

Kılavuz sayfalarını biçimlendir ve göster.
Daha fazla bilgi için: <https://manned.org/man>.

- Bir komut için man sayfasını görüntüle:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Sayfanın 7. bölümündeki bir komut için man sayfasını görüntüle:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Mansayfaları için aratılan yolu göster:

`man --path`

- Mansayfasını göstermek yerine mansayfasının konumunu göster:

`man -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>

- Belirtilen ifadeyi içeren mansayfalarını ara:

`man -k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_ifade</span>`"`
