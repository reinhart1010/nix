---
layout: page
title: linux/pacman-key (português (Brasil))
description: "Script envoltório para o GnuPG usado para gerenciar o chaveiro do pacman."
content_hash: 3dafb2a0150de0d49aa830b054aadafdb672ac65
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/pacman-key.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-key.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-key.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-key

Script envoltório para o GnuPG usado para gerenciar o chaveiro do pacman.
Veja também: `pacman`.
Mais informações: <https://manned.org/pacman-key>.

- Inicializa o chaveiro do `pacman`:

`sudo pacman-key --init`

- Adiciona as chaves padrão do Arch Linux:

`sudo pacman-key --populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archlinux</span>

- Lista chaves do chaveiro público:

`pacman-key --list-keys`

- Adiciona as chaves especificadas:

`sudo pacman-key --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_chave.gpg</span>

- Recebe uma chave do servidor de chaves:

`sudo pacman-key --recv-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nome|email</span>`"`

- Imprime a impressão digital de uma chave específica:

`pacman-key --finger "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nome|email</span>`"`

- Assina uma chave importada localmente:

`sudo pacman-key --lsign-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nome|email</span>`"`

- Remove uma chave específica:

`sudo pacman-key --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nome|email</span>`"`
