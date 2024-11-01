---
layout: page
title: freebsd/cal (português (Brasil))
description: "Mostra um calendário com o dia atual destacado."
content_hash: 164f65ff8fc5aa2eb0f88438c118490895c01b7f
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/freebsd/cal.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/cal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Mostra um calendário com o dia atual destacado.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Exibe um calendário para o mês atual:

`cal`

- Exibe um calendário para um ano específico:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ano</span>

- Exibe um calendário para um ano e mês específicos:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mês</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ano</span>

- Exibe o calendário inteiro para o ano atual:

`cal -y`

- Não destaca hoje e exibe [3] meses abrangendo a data:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mês</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ano</span>

- Exibe os 2 meses [A]ntes e 3 [D]epois de um [m]ês específico do ano atual:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mês</span>

- Exibe dias [j]ulianos (começando de um, numerados de 1º de janeiro):

`cal -j`
