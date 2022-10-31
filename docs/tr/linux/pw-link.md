---
layout: page
title: linux/pw-link (Türkçe)
description: "PipeWire'daki portlar arası linkleri yönet."
content_hash: 7078351168239f721c52551f4eabff85bcc1324c
related_topics:
  - title: English version
    url: /en/linux/pw-link.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-link

PipeWire'daki portlar arası linkleri yönet.
Daha fazla bilgi için: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Tüm ses çıktı ve girdi portlarını sırala:

`pw-link --output --input'`

- Çıktı ve girdi portları arasında bir bağlantı yarat:

`pw-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">çıktı_port_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">girdi_port_ismi</span>

- Disconnect two ports:

`pw-link --disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">çıktı_port_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">girdi_port_ismi</span>

- Yardım sayfası göster:

`pw-link -h`
