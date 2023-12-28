---
layout: page
title: linux/chkconfig (português (Brasil))
description: "Gerencia o runlevel dos serviços no CentOS 6."
content_hash: 80a5e693db7da9e31e1ee048b501e9f4d8e67c59
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/chkconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chkconfig

Gerencia o runlevel dos serviços no CentOS 6.
Mais informações: <https://manned.org/chkconfig>.

- Exibe os serviços com os respectivos runlevels:

`chkconfig --list`

- Exibe o runlevel de um serviço:

`chkconfig --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>

- Habilita o início de um serviço durante o processo de boot:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- Habilita o início do serviço durante o processo de boot para os runlevels 2, 3, 4 e 5:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2345</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- Desabilita a inicialização de um determinado serviço durante o processo de boot:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`

- Desabilita a inicialização de um determinado serviço durante o processo de boot para o runlevel 3:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`
