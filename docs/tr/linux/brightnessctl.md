---
layout: page
title: linux/brightnessctl (Türkçe)
description: "GNU/Linux işletim sistemlerinde cihaz parlaklığını okumak ve kontrol etmek için yardımcı program."
content_hash: ea0a1b9733f1c051b00a12df2b9f1f7b7c703d64
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/brightnessctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/brightnessctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brightnessctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brightnessctl

GNU/Linux işletim sistemlerinde cihaz parlaklığını okumak ve kontrol etmek için yardımcı program.
Daha fazla bilgi için: <https://github.com/Hummer12007/brightnessctl>.

- Değiştirilebilir parlaklığa sahip cihazları listele:

`brightnessctl --list`

- Ekran arka ışığının şu andaki seviyesini yazdır:

`brightnessctl get`

- Ekran parlaklığını belli bir aralık dahilinde belirli yüzdeye eşitle:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>

- Parlaklığı belirli bir seviyede artır:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+10%</span>

- Parlaklığı belirli bir seviyede düşür:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
