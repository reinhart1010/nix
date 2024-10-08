---
layout: page
title: linux/makepkg (português (Brasil))
description: "Monta um pacote que pode ser usado junto ao `pacman`."
content_hash: 4973f31a8887d85c1ac7ce678610ed2ef93d42ee
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/makepkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/makepkg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/makepkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# makepkg

Monta um pacote que pode ser usado junto ao `pacman`.
Utiliza por padrão o arquivo `PKGBUILD` no diretório de trabalho atual.
Mais informações: <https://manned.org/makepkg.8>.

- Monta um pacote:

`makepkg`

- Monta um pacote e instala suas dependências:

`makepkg --syncdeps`

- Monta um pacote, instala suas dependências e então o instala no sistema:

`makepkg --syncdeps --install`

- Monta um pacote, mas pula a verificação de hashes da fonte:

`makepkg --skipchecksums`

- Limpa os diretórios de trabalho após uma compilação bem sucedida:

`makepkg --clean`

- Verifica os hashes das fontes:

`makepkg --verifysource`

- Gera e salva as informações da fonte no arquivo `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`
