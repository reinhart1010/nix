---
layout: page
title: linux/apache2ctl (português (Brasil))
description: "Interface de controle do servidor web HTTP Apache."
content_hash: d0f62a64f2bbf052b1eab3293c4d2a915fbfff92
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/linux/apache2ctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apache2ctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apache2ctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apache2ctl

Interface de controle do servidor web HTTP Apache.
Este comando está disponível nas distribuições baseadas em Debian, para as baseadas em RHEL veja `httpd`.
Mais informações: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- Inicia o Apache. Caso ele já esteja em execução, uma mensagem será apresentada:

`sudo apache2ctl start`

- Encerra o Apache:

`sudo apache2ctl stop`

- Reinicia o Apache:

`sudo apache2ctl restart`

- Verifica se o arquivo de configuração está correto sintaticamente:

`sudo apache2ctl -t`

- Lista os módulos carregados:

`sudo apache2ctl -M`
