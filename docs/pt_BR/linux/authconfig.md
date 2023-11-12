---
layout: page
title: linux/authconfig (português (Brasil))
description: "Interface de linha comandos para configurar o sistema de autenticação."
content_hash: 2af339f43ecbf52e2225c1b39b5bcde1577f0c26
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/authconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/authconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# authconfig

Interface de linha comandos para configurar o sistema de autenticação.
Mais informações: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- Exibir as configurações atuais (ou dry run):

`authconfig --test`

- Configurar o servidor para utilizar diferentes algoritmos de hash para as senhas:

`authconfig --update --passalgo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algoritmo</span>

- Habilitar a autenticação via LDAP:

`authconfig --update --enableldapauth`

- Desabilitar a autenticação via LDAP:

`authconfig --update --disableldapauth`

- Habilitar o Network Information Service (NIS):

`authconfig --update --enablenis`

- Habilitar Kerberos:

`authconfig --update --enablekrb5`

- Habilitar a autenticação Winbind (Active Directory):

`authconfig --update --enablewinbindauth`

- Habilitar a autorização local:

`authconfig --update --enablelocauthorize`
