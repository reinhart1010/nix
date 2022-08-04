---
layout: page
title: linux/xfce4-screenshooter (English)
description: "The XFCE4 screenshot tool."
content_hash: 4c323b09dabd50f64794fae38bbb290fdc4a4b94
related_topics:
  - title: Türkçe version
    url: /tr/linux/xfce4-screenshooter.html
    icon: bi bi-globe
---
# xfce4-screenshooter

The XFCE4 screenshot tool.
More information: <https://docs.xfce.org/apps/xfce4-screenshooter/start>.

- Launch the screenshooter GUI:

`xfce4-screenshooter`

- Take a screenshot of the entire screen and launch the GUI to ask how to proceed:

`xfce4-screenshooter --fullscreen`

- Take a screenshot of the entire screen and save it in the specified directory:

`xfce4-screenshooter --fullscreen --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Wait some time before taking the screenshot:

`xfce4-screenshooter --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>

- Take a screenshot of a region of the screen (select using the mouse):

`xfce4-screenshooter --region`

- Take a screenshot of the active window, and copy it to the clipboard:

`xfce4-screenshooter --window --clipboard`

- Take a screenshot of the active window, and open it with a chosen program:

`xfce4-screenshooter --window --open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gimp</span>
