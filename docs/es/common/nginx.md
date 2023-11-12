---
layout: page
title: common/nginx (español)
description: "Servidor web Nginx."
content_hash: b0a5ea75bfb7f1e70b30040382891e7ceb27dbc3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/nginx.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nginx.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/nginx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nginx

Servidor web Nginx.
Más información: <https://nginx.org/en/>.

- Inicia el servidor con el archivo de configuración por defecto:

`nginx`

- Inicia el servidor con un archivo de configuración personalizado:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_configuración</span>

- Inicia el servidor con un prefijo para todas las rutas relativas en el archivo de configuración:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_configuración</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo/para/rutas/relativas</span>

- Prueba la configuración sin afectar al servidor en ejecución:

`nginx -t`

- Recarga la configuración enviando una señal sin tiempo de inactividad:

`nginx -s reload`
