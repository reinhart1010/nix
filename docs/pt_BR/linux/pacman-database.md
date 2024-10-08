---
layout: page
title: linux/pacman-database (português (Brasil))
description: "Atua no banco de dados de pacotes do Arch Linux."
content_hash: 9f4ab286baff16bde2774fb58775e4c76a2dd1f9
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-database.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-database.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-database.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --database

Atua no banco de dados de pacotes do Arch Linux.
Modifica certos atributos dos pacotes instalados.
Veja também: `pacman`.
Mais informações: <https://manned.org/pacman.8>.

- Marca um pacote como instalado implicitamente:

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Marca um pacote como instalado explicitamente:

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Verifica se todas as dependências de pacotes estão instaladas:

`pacman --database --check`

- Verifica os repositórios para garantir que todas as dependências especificadas estejam disponíveis:

`pacman --database --check --check`

- Exibe apenas mensagens de erro:

`pacman --database --check --quiet`

- Exibe ajuda:

`pacman --database --help`
