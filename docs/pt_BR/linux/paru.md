---
layout: page
title: linux/paru (português (Brasil))
description: "Um auxiliar do AUR e um wrapper do pacman."
content_hash: 846aa4b90ffa7b59369f194cbc464a9550b096e5
related_topics:
  - title: English version
    url: /en/linux/paru.html
    icon: bi bi-globe
---
# paru

Um auxiliar do AUR e um wrapper do pacman.
Mais informações: <https://github.com/Morganamilo/paru>.

- Pesquisa e instala interativamente um pacote:

`paru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote_ou_termo_de_pesquisa</span>

- Sincroniza e atualizar todos os pacotes:

`paru`

- Atualiza pacotes do AUR:

`paru -Sua`

- Obtém informações sobre um pacote:

`paru -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Faz o download do `PKGBUILD` e outros arquivos de origem do pacote do AUR ou ABS:

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibe o arquivo `PKGBUILD` de um pacote:

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>
