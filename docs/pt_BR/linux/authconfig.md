---
layout: page
title: linux/authconfig (português (Brasil))
description: "Interface de linha comandos para configurar o sistema de autenticação."
content_hash: ac56f84f723408649d41fa21810903d5e5b25af3
last_modified_at: 2023-12-28
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

- Exibe as configurações atuais (ou dry run):

`authconfig --test`

- Configura o servidor para utilizar diferentes algoritmos de hash para as senhas:

`authconfig --update --passalgo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algoritmo</span>

- Habilita a autenticação via LDAP:

`authconfig --update --enableldapauth`

- Desabilita a autenticação via LDAP:

`authconfig --update --disableldapauth`

- Habilita o Network Information Service (NIS):

`authconfig --update --enablenis`

- Habilita Kerberos:

`authconfig --update --enablekrb5`

- Habilita a autenticação Winbind (Active Directory):

`authconfig --update --enablewinbindauth`

- Habilita a autorização local:

`authconfig --update --enablelocauthorize`
