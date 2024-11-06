---
layout: page
title: common/x11docker (한국어)
description: "Docker 컨테이너에서 GUI 애플리케이션 및 데스크톱 UI를 안전하게 실행."
content_hash: de0779917a8c9c2d4baf4da3d995bcfd279e8736
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/x11docker.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/x11docker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# x11docker

Docker 컨테이너에서 GUI 애플리케이션 및 데스크톱 UI를 안전하게 실행.
같이 보기: `xephyr`.
더 많은 정보: <https://github.com/mviereck/x11docker>.

- 컨테이너에서 VLC 실행:

`x11docker --pulseaudio --share=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME/Videos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jess/vlc</span>

- 창에서 Xfce 실행:

`x11docker --desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/xfce</span>

- 창에서 GNOME 실행:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/gnome</span>

- 창에서 KDE Plasma 실행:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/kde-plasma</span>

- 도움말 표시:

`x11docker --help`
