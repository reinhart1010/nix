---
layout: page
title: linux/pacman-mirrors (português (Brasil))
description: "Gera uma lista de mirrors do pacman para o Manjaro Linux."
content_hash: 966ef645c88c0262ffe4b7630fb75ceea0a525eb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-mirrors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-mirrors

Gera uma lista de mirrors do pacman para o Manjaro Linux.
Toda execução do pacman-mirrors requer que você sincronize seu bando de dados e atualize seu sistema usado `sudo pacman -Syyu`.
Veja também: `pacman`.
Mais informações: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Gera uma lista de mirrors usando as configurações padrão:

`sudo pacman-mirrors --fasttrack`

- Obtém o status dos mirrors atuais:

`pacman-mirrors --status`

- Exibe a branch atual:

`pacman-mirrors --get-branch`

- Muda para uma branch diferente:

`sudo pacman-mirrors --api --set-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|unstable|testing</span>

- Gera uma lista de mirror, usando apenas mirrors em seu país:

`sudo pacman-mirrors --geoip`
