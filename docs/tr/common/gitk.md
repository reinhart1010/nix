---
layout: page
title: common/gitk (Türkçe)
description: "Görsel Git depo tarayıcısı."
content_hash: f59ab0bd787ae7975ee4014d19d0676d451efc3e
last_modified_at: 2024-04-04
related_topics:
  - title: English version
    url: /en/common/gitk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitk

Görsel Git depo tarayıcısı.
Daha fazla bilgi için: <https://git-scm.com/docs/gitk>.

- Mevcut Git deposu için depo tarayıcısını göster:

`gitk`

- Belirtilmiş dosya veya dizin için depo tarayıcısını göster:

`gitk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- 1 hafta önceden beri yapılan commit'leri göster:

`gitk --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 week ago</span>`"`

- 1/1/2016 tarihinden önceki commit'leri göster:

`gitk --until="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1/1/2016</span>`"`

- Tüm dallarda en fazla 100 değişiklik göster:

`gitk --max-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --all`
