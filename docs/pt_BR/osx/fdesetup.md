---
layout: page
title: osx/fdesetup (português (Brasil))
description: "Define e recupera informações relacionadas ao FileVault."
content_hash: 0960318739bdaf424e6999357f8d5b88b1f88209
related_topics:
  - title: English version
    url: /en/osx/fdesetup.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fdesetup

Define e recupera informações relacionadas ao FileVault.
Mais informações: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- Lista os usuários atuais habilitados para o FileVault:

`sudo fdesetup list`

- Obtém o status atual do FileVault:

`fdesetup status`

- Adiciona usuário habilitado para o FileVault:

`sudo fdesetup add -usertoadd user1`

- Ativa o FileVault:

`sudo fdesetup enable`

- Desativa o FileVault:

`sudo fdesetup disable`
