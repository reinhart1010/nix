---
layout: page
title: linux/xrandr (Türkçe)
description: "Bir ekran için boyut, yön ve/veya çıkış yansımasını ayarla."
content_hash: 383050965ab79dca6768bd783807da1aa455eddc
related_topics:
  - title: Deutsch version
    url: /de/linux/xrandr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xrandr.html
    icon: bi bi-globe
---
# xrandr

Bir ekran için boyut, yön ve/veya çıkış yansımasını ayarla.
Daha fazla bilgi için: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Sistemin mevcut durumunu göster (bilinen ekranlar, çözünürlükler, ...):

`xrandr --query`

- Bağlantısı kesilmiş çıkışları devre dışı bırak ve bağlanmış olanları varsayılan ayarlar ile devreye sok:

`xrandr --auto`

- DisplayPort 1'in çözünürlük ve yenileme hızını 1920x1080, 60Hz olarak değiştir:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920x1080</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>

- HDMI2'nin çözünürlüğünü 1280x1024'e değiştirip, DP1'in sağına koy:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HDMI2</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1280x1024</span>` --right-of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>

- VGA1 çıkışını devre dışı bırak:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VGA1</span>` --off`

- LVDS1 için parlaklığı 50% yap:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LVDS1</span>` --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>
