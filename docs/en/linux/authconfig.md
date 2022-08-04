---
layout: page
title: linux/authconfig (English)
description: "A CLI interface for configuring system authentication resources."
content_hash: 02a10d8a7be42784a09ae80f38013de1880d304c
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/authconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/authconfig.html
    icon: bi bi-globe
---
# authconfig

A CLI interface for configuring system authentication resources.
More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- Display the current configuration (or dry run):

`authconfig --test`

- Configure the server to use a different password hashing algorithm:

`authconfig --update --passalgo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>

- Enable LDAP authentication:

`authconfig --update --enableldapauth`

- Disable LDAP authentication:

`authconfig --update --disableldapauth`

- Enable Network Information Service (NIS):

`authconfig --update --enablenis`

- Enable Kerberos:

`authconfig --update --enablekrb5`

- Enable Winbind (Active Directory) authentication:

`authconfig --update --enablewinbindauth`

- Enable local authorization:

`authconfig --update --enablelocauthorize`
