---
layout: page
title: common/calendar (português (Brasil))
description: "Mostra eventos de um arquivo calendar."
content_hash: cd082f4d982d3f475dab9d48ec0e3030ed72585f
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/calendar.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/calendar.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/calendar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calendar

Mostra eventos de um arquivo calendar.
Mais informações: <https://manned.org/calendar>.

- Mostra eventos para hoje e amanhã (ou para o final de semana na sexta-feira) do calendário padrão:

`calendar`

- Mostra eventos marcados para os próximos 30 dias ([A]head):

`calendar -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Mostra eventos ocorridos nos últimos 7 dias ([B]ack):

`calendar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Mostra eventos de um calendário personalizado, salvo no caminho especificado ([f]ile):

`calendar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
