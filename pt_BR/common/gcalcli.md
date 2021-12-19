---
layout: page
title: common/gcalcli (português (Brasil))
description: "Ferramenta de linha de comando para interagir com o Google Agenda."
content_hash: ece58e06d2bad00e99aae97a7be11ccac14dbf23
related_topics:
  - title: English version
    url: /en/common/gcalcli.html
    icon: bi bi-globe
---
# gcalcli

Ferramenta de linha de comando para interagir com o Google Agenda.
Solicita autorização da API do Google na primeira inicialização.
Mais informações: <https://github.com/insanum/gcalcli>.

- Lista seus eventos para todos os seus calendários nos próximos 7 dias:

`gcalcli agenda`

- Mostra eventos começando em ou entre datas específicas (também recebe datas relativas, por exemplo, "amanhã"):

`gcalcli agenda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>`]`

- Lista eventos de um calendário específico:

`gcalcli --calendar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_calendário</span>` agenda`

- Exibe um calendário ASCII de eventos por semana:

`gcalcli calw`

- Exibe um calendário ASCII de eventos para um mês:

`gcalcli calm`

- Adiciona um evento rapidamente ao seu calendário:

`gcalcli --calendar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_calendário</span>` quick "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HH:MM</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_evento</span>`"`

- Adiciona um evento ao calendário. Dispara prompt interativo:

`gcalcli --calendar "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_calendário</span>`" add`
