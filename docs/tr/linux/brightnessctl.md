---
layout: page
title: linux/brightnessctl (Türkçe)
description: "Linux işletim sistemlerinde cihaz parlaklığını okumak ve kontrol etmek için yardımcı program."
content_hash: cd72db43d32bba207a71803976bcfc9d6298bd2a
last_modified_at: 2024-01-30
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

Linux işletim sistemlerinde cihaz parlaklığını okumak ve kontrol etmek için yardımcı program.
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
