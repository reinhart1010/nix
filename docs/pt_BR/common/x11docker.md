---
layout: page
title: common/x11docker (português (Brasil))
description: "Executar aplicativos de GUI e interfaces de desktop seguramente em contêineres do Docker."
content_hash: 01c41d2c40a5dbdcf9533758f8aa9ea5d3698b17
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/x11docker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# x11docker

Executar aplicativos de GUI e interfaces de desktop seguramente em contêineres do Docker.
Veja também `xephyr`.
Mais informações: <https://github.com/mviereck/x11docker>.

- Inicia o VLC em um contêiner:

`x11docker --pulseaudio --share=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME/Videos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jess/vlc</span>

- Inicia o Xfce em uma janela:

`x11docker --desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/xfce</span>

- Inicia o GNOME em uma janela:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/gnome</span>

- Inicia o KDE Plasma em uma janela:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/kde-plasma</span>

- Exibe ajuda:

`x11docker --help`
