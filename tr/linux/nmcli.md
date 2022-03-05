---
layout: page
title: linux/nmcli (Türkçe)
description: "NetworkManager'ı denetlemek için bir komut satırı aracı."
content_hash: acd58396a0326f8debc3a341755a4c68af51b26a
related_topics:
  - title: English version
    url: /en/linux/nmcli.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/nmcli.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nmcli

NetworkManager'ı denetlemek için bir komut satırı aracı.
`nmcli monitor` gibi bazı alt komutların kendi kullanım belgeleri vardır.
Daha fazla bilgi: <https://manned.org/nmcli>.

- Bir `nmcli` alt komutunu çalıştır:

`nmcli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent|connection|device|general|help|monitor|networking|radio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut_seçenekleri</span>

- Kullanılan NetworkManager sürümünü görüntüle:

`nmcli --version`

- Yardımı görüntüle:

`nmcli --help`

- Bir alt komut için yardımı görüntüle:

`nmcli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alt_komut</span>` --help`
