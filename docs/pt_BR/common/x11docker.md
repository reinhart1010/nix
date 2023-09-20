---
layout: page
title: common/x11docker (português (Brasil))
description: "Executar aplicativos de GUI e interfaces de desktop seguramente em contêineres do Docker."
content_hash: bbaf2836c71842d41277ae121904baa5e67ca973
last_modified_at: 2023-09-20
related_topics:
  - title: English version
    url: /en/common/x11docker.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># x11docker

Executar aplicativos de GUI e interfaces de desktop seguramente em contêineres do Docker.
Veja também `xephyr`.
Mais informações: <https://github.com/mviereck/x11docker>.

- Iniciar o VLC em um contêiner:

`x11docker --pulseaudio --share=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME/Videos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jess/vlc</span>

- Iniciar o Xfce em uma janela:

`x11docker --desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/xfce</span>

- Iniciar o GNOME em uma janela:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/gnome</span>

- Iniciar o KDE Plasma em uma janela:

`x11docker --desktop --gpu --init=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11docker/kde-plasma</span>

- Exibir ajuda:

`x11docker --help`
