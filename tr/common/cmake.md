---
layout: page
title: common/cmake (Türkçe)
description: "Çok platformlu yapım sistem oluşturucusu."
content_hash: c11e5388a70f7266135f6b92727d9a783ea0c38a
related_topics:
  - title: Deutsch version
    url: /de/common/cmake.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cmake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cmake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmake.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cmake.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cmake

Çok platformlu yapım sistem oluşturucusu.
Hedeflenen sisteme göre Makefile, Visual Studio projeleri ve benzerlerini oluşturur.
Daha fazla bilgi: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Bir Makefile oluştur ve onu aynı dizindeki bir projeyi derlemek için kullan:

`cmake && make`

- Bir Makefile oluştur ve onu farklı bir "yapim" dizinindeki projeyi derlemek için kullan (kaynak-dışı yapım):

`cmake -H. -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>` && make -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yapim</span>
