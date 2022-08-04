---
layout: page
title: common/x11docker (English)
description: "Securely run GUI applications and desktop UIs in Docker containers."
content_hash: cf4786f4efa484ea273058ac1dea5c80d91256e7
---
# x11docker

Securely run GUI applications and desktop UIs in Docker containers.
See also `xephyr`.
More information: <https://github.com/mviereck/x11docker>.

- Launch VLC in a container:

`x11docker --pulseaudio --share=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME/Videos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jess/vlc</span>

- Launch Xfce in a window:

`x11docker --desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/xfce</span>

- Launch GNOME in a window:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/gnome</span>

- Launch KDE Plasma in a window:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/kde-plasma</span>

- Display help:

`x11docker --help`
