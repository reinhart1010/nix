---
layout: page
title: osx/indent (português (Brasil))
description: "Altera a aparência de um programa C/C++ inserindo ou excluindo espaços em branco."
content_hash: 27c912655e406e1e9f96e14e9b2a27405ba691ea
last_modified_at: 2022-11-20
related_topics:
  - title: English version
    url: /en/osx/indent.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># indent

Altera a aparência de um programa C/C++ inserindo ou excluindo espaços em branco.
Mais informações: <https://www.freebsd.org/cgi/man.cgi?query=indent>.

- Formata código fonte C/C++ de acordo com o estilo Berkeley:

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte_identado.c</span>` -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Formata código fonte C/C++ de acordo com o estilo Kernighan & Ritchie (K&R):

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte_identado.c</span>` -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
