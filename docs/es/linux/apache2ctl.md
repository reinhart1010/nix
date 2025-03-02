---
layout: page
title: linux/apache2ctl (español)
description: "Administra el servidor web Apache HTTP."
content_hash: 9cbda8c45919e8e5424210da393bbfc5bad45314
last_modified_at: 2025-03-02
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
  - title: 한국어 version
    url: /ko/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apache2ctl

Administra el servidor web Apache HTTP.
Este comando viene con los sistemas operativos basados en Debian; para los basados en RHEL, consulte `httpd`.
Más información: <https://manned.org/apache2ctl.8>.

- Inicia el programa residente (daemon) de Apache. Muestra un mensaje si ya está en ejecución:

`sudo apache2ctl start`

- Detiene el programa residente (daemon) de Apache:

`sudo apache2ctl stop`

- Reinicia el programa residente (daemon) de Apache:

`sudo apache2ctl restart`

- Prueba la sintaxis del archivo de configuración:

`sudo apache2ctl -t`

- Lista los módulos cargados:

`sudo apache2ctl -M`
