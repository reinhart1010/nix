---
layout: page
title: common/tldr-lint (Türkçe)
description: "`tldr` sayfalarını gözden geçir ve biçimlendir."
content_hash: ed407756c9ba452e7a84dde31d5fb437becdbfa2
related_topics:
  - title: English version
    url: /en/common/tldr-lint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr-lint.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr-lint.html
    icon: bi bi-globe
---
# tldr-lint

`tldr` sayfalarını gözden geçir ve biçimlendir.
Daha fazla bilgi: <https://github.com/tldr-pages/tldr-lint>.

- Tüm sayfaları gözden geçir:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sayfa_dizini</span>

- Belirtilmiş bir sayfayı stdout'a biçimlendir:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page.md</span>

- Bir konumdaki tüm sayfaları biçimlendir:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sayfa_dizini</span>
