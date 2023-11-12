---
layout: page
title: linux/adig (português (Brasil))
description: "Imprime informações recebidas dos servidores do Sistema de Domínio de Nome(DNS)."
content_hash: 45da573dc445918c2fc4b8f60e06ffdfcb7d5272
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/adig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/adig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adig

Imprime informações recebidas dos servidores do Sistema de Domínio de Nome(DNS).
Mais informações: <https://manned.org/adig>.

- Exibe uma gravação A (padrão) do DNS por nome(s) de servidor(es):

`adig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">examplo.com</span>

- Exibe uma saída de [d]epuração extra:

`adig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">examplo.com</span>

- Conecte-se a um servidor DNS específico:

`adig -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">examplo.com</span>

- Use uma porta TCP específica para se conectar ao servidor DNS:

`adig -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">examplo.com</span>

- Use uma porta UDP específica para se conectar ao servidor DNS:

`adig -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">examplo.com</span>
