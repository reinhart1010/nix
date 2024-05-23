---
layout: page
title: linux/xrandr (English)
description: "Set the size, orientation and/or reflection of the outputs for a screen."
content_hash: ebfa54b297b351e54be3af1ea3c7f972a67816af
last_modified_at: 2024-05-23
related_topics:
  - title: Deutsch version
    url: /de/linux/xrandr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/xrandr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xrandr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xrandr

Set the size, orientation and/or reflection of the outputs for a screen.
More information: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Display the current state of the system (known screens, resolutions, ...):

`xrandr --query`

- Disable disconnected outputs and enable connected ones with default settings:

`xrandr --auto`

- Change the resolution and update frequency of DisplayPort 1 to 1920x1080, 60Hz:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920x1080</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>

- Set the resolution of HDMI2 to 1280x1024 and put it on the right of DP1:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HDMI2</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1280x1024</span>` --right-of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>

- Disable the VGA1 output:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VGA1</span>` --off`

- Set the brightness for LVDS1 to 50%:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LVDS1</span>` --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>

- Display the current state of any X server:

`xrandr --display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --query`
