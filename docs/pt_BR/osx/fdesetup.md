---
layout: page
title: osx/fdesetup (português (Brasil))
description: "Define e recupera informações relacionadas ao FileVault."
content_hash: d1a515013a86b97406557822e9840e01f3b4f7dd
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/osx/fdesetup.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/fdesetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdesetup

Define e recupera informações relacionadas ao FileVault.
Mais informações: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- Lista os usuários atuais habilitados para o FileVault:

`sudo fdesetup list`

- Obtém o status atual do FileVault:

`fdesetup status`

- Adiciona usuário habilitado para o FileVault:

`sudo fdesetup add -usertoadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário1</span>

- Ativa o FileVault:

`sudo fdesetup enable`

- Desativa o FileVault:

`sudo fdesetup disable`
