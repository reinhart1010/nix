---
layout: page
title: linux/chkconfig (português (Brasil))
description: "Gerencia o runlevel dos serviços no CentOS 6."
content_hash: 150028bb6f5da82edc5064564b6168134f1a8383
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/chkconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chkconfig

Gerencia o runlevel dos serviços no CentOS 6.
Mais informações: <https://manned.org/chkconfig>.

- Exibir os serviços com os respectivos runlevels:

`chkconfig --list`

- Exibir o runlevel de um serviço:

`chkconfig --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>

- Habilitar o início de um serviço durante o processo de boot:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- Habilitar o início do serviço durante o processo de boot para os runlevels 2, 3, 4 e 5:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2345</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- Desabilitar a inicialização de um determinado serviço durante o processo de boot:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`

- Desabilitar a inicialização de um determinado serviço durante o processo de boot para o runlevel 3:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`
