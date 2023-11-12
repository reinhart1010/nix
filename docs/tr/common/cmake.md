---
layout: page
title: common/cmake (Türkçe)
description: "Çok platformlu yapım sistem oluşturucusu."
content_hash: 2a0e7bd5647723ad058e91c86779ec8297f8559c
last_modified_at: 2023-11-12
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmake

Çok platformlu yapım sistem oluşturucusu.
Hedeflenen sisteme göre Makefile, Visual Studio projeleri ve benzerlerini oluşturur.
Daha fazla bilgi için: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Bir Makefile oluştur ve onu aynı dizindeki bir projeyi derlemek için kullan:

`cmake && make`

- Bir Makefile oluştur ve onu farklı bir "yapim" dizinindeki projeyi derlemek için kullan (kaynak-dışı yapım):

`cmake -H. -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>` && make -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yapim</span>
