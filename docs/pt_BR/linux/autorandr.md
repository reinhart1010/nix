---
layout: page
title: linux/autorandr (português (Brasil))
description: "Altera o layout da tela automaticamente."
content_hash: fb582742e92a78290bb09ef0ac15231ad084f733
last_modified_at: 2024-10-02
related_topics:
  - title: English version
    url: /en/linux/autorandr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/autorandr.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># autorandr

Altera o layout da tela automaticamente.
Mais informações: <https://github.com/phillipberndt/autorandr>.

- Salva o layout da tela em uso:

`autorandr --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_perfil</span>

- Exibe os perfis salvos:

`autorandr`

- Carrega o primeiro perfil detectado:

`autorandr --change`

- Carrega um perfil específico:

`autorandr --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_perfil</span>

- Define o perfil padrão:

`autorandr --default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_perfil</span>
