---
layout: page
title: common/crontab (español)
description: "Programa trabajos recurrentes (cron jobs) para ejecutarse a intervalos de tiempo para el usuario actual."
content_hash: 111d94ca848bb0a6a5d1b2d69a37486e4a12dc3b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/crontab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/crontab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crontab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/crontab.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/crontab.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/crontab.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crontab.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crontab

Programa trabajos recurrentes (cron jobs) para ejecutarse a intervalos de tiempo para el usuario actual.
Más información: <https://crontab.guru/>.

- Edita el archivo crontab para el usuario actual:

`crontab -e`

- Edita el archivo crontab para un usuario específico:

`sudo crontab -e -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Reemplaza el crontab actual con el contenido del archivo dado:

`crontab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Ver una lista de cron jobs existentes para el usuario actual:

`crontab -l`

- Elimina todos los cron jobs para el usuario actual:

`crontab -r`

- Ejemplo de entrada contrab que ejecuta un comando a las 10:00 cada día (* significa cualquier valor):

`0 10 * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Ejemplo de entrada crontab, que ejecuta un comando cada 10 minutos:

`*/10 * * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Ejemplo de entrada crontab, que ejecuta un script a las 02:30 cada viernes:

`30 2 * * Fri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/absoluta/a/script.sh</span>
