---
layout: page
title: common/gitk (Türkçe)
description: "Görsel Git depo tarayıcısı."
content_hash: ed0b7fdafbd6b8aefa438b8313ba8e7a4ca46773
related_topics:
  - title: English version
    url: /en/common/gitk.html
    icon: bi bi-globe
---
# gitk

Görsel Git depo tarayıcısı.
Daha fazla bilgi: <https://git-scm.com/docs/gitk>.

- Mevcut Git deposu için depo tarayıcısını göster:

`gitk`

- Belirtilmiş dosya veya dizin için depo tarayıcısını göster:

`gitk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- 1 hafta önceden beri yapılan commit'leri göster:

`gitk --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 week ago</span>`"`

- 1/1/2016 tarihinden önceki commit'leri göster:

`gitk --until="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1/1/2016</span>`"`

- Tüm dallarda en fazla 100 değişiklik göster:

` gitk --max-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --all`
