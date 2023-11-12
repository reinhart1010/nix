---
layout: page
title: common/dig (Türkçe)
description: "DNS sunucularına sorgulama yapmak için kullanılan bir komuttur."
content_hash: 342b25eef659afb676d292176da191240d06965f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dig.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/dig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dig

DNS sunucularına sorgulama yapmak için kullanılan bir komuttur.
Daha fazla bilgi için: <https://manned.org/dig>.

- İlgili sunucu ile ilgili IP adresi sorgulaması yapılır:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- DNS sorgulaması için alternatif server kullanılır:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Tersine DNS sorgulaması yapılır:

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- Belli başlı DNS sunucuları ile ilgili kayıtları sorgular:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|MX|TXT|CNAME|NS</span>
