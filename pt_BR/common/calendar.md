---
layout: page
title: common/calendar (português (Brasil))
description: "Mostra eventos de um arquivo calendar."
content_hash: 98fba375647f74ed42bc5d99309c2d77f17046ea
related_topics:
  - title: English version
    url: /en/common/calendar.html
    icon: bi bi-globe
---
# calendar

Mostra eventos de um arquivo calendar.
Mais informações: <https://www.commandlinux.com/man-page/man1/calendar.1.html>.

- Mostra eventos para hoje e amanhã (ou para o final de semana na sexta-feira) do calendário padrão:

`calendar`

- Mostra eventos marcados para os próximos 30 dias ([A]head):

`calendar -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Mostra eventos ocorridos nos últimos 7 dias ([B]ack):

`calendar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Mostra eventos de um calendário personalizado, salvo no caminho especificado ([f]ile):

`calendar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
