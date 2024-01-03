---
layout: page
title: common/xwininfo (português (Brasil))
description: "Mostra informações sobre janelas."
content_hash: dcc31336808e2855661137c096555f8c57ad72a8
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/common/xwininfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xwininfo

Mostra informações sobre janelas.
Veja também: `xprop`, `xkill`.
Mais informações: <https://www.x.org/releases/current/doc/man/man1/xwininfo.1.xhtml>.

- Mostra um cursor para selecionar uma janela para mostrar seus atributos (ID, nome, tamanho, posição...):

`xwininfo`

- Mostra a árvore de todas as janelas:

`xwininfo -tree -root`

- Mostra os atributos de uma janela com um ID específico:

`xwininfo -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Mostra os atributos de uma janela com um nome específico:

`xwininfo -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Mostra o ID de uma janela buscando pelo nome:

`xwininfo -tree -root | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra_chave</span>` | head -1 | perl -ne 'print $1 if /(0x[\da-f]+)/ig;'`
