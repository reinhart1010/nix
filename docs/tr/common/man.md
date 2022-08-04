---
layout: page
title: common/man (Türkçe)
description: "Kılavuz sayfalarını biçimlendir ve göster."
content_hash: fbb0f88900ea3ca2c3800d289591880249c6f8d0
related_topics:
  - title: English version
    url: /en/common/man.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/man.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/man.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># man

Kılavuz sayfalarını biçimlendir ve göster.
Daha fazla bilgi: <https://www.man7.org/linux/man-pages/man1/man.1.html>.

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
