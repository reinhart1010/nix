---
layout: page
title: linux/authconfig (español)
description: "Configura los recursos de autenticación del sistema."
content_hash: 04acff392e50d41dbee98ccacd5df137e75e9611
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/authconfig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/authconfig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/authconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/authconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# authconfig

Configura los recursos de autenticación del sistema.
Más información: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- Muestra la configuración actual (o realiza una simulación):

`authconfig --test`

- Configura el servidor para usar un algoritmo de hash de contraseñas diferente:

`authconfig --update --passalgo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algoritmo</span>

- Habilita la autenticación LDAP:

`authconfig --update --enableldapauth`

- Deshabilita la autenticación LDAP:

`authconfig --update --disableldapauth`

- Habilita el servicio de información de red (NIS):

`authconfig --update --enablenis`

- Habilita Kerberos:

`authconfig --update --enablekrb5`

- Habilita la autenticación Winbind (Active Directory):

`authconfig --update --enablewinbindauth`

- Habilita la autorización local:

`authconfig --update --enablelocauthorize`
