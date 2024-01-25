---
layout: page
title: osx/indent (português (Brasil))
description: "Altera a aparência de um programa C/C++ inserindo ou excluindo espaços em branco."
content_hash: a84c9c6ddc3ca3a517d9452d1522126012320080
last_modified_at: 2024-01-25
related_topics:
  - title: English version
    url: /en/osx/indent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# indent

Altera a aparência de um programa C/C++ inserindo ou excluindo espaços em branco.
Mais informações: <https://keith.github.io/xcode-man-pages/indent.1.html>.

- Formata código fonte C/C++ de acordo com o estilo Berkeley:

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte_identado.c</span>` -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Formata código fonte C/C++ de acordo com o estilo Kernighan & Ritchie (K&R):

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte_identado.c</span>` -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
