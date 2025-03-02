---
layout: page
title: common/rails-server (español)
description: "Sirve la aplicación Rails en el directorio actual utilizando el servidor web Puma, que viene incluido con Rails."
content_hash: 23e212bb7ef4bb150796648ebcc83bc51259d86a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/rails-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails server

Sirve la aplicación Rails en el directorio actual utilizando el servidor web Puma, que viene incluido con Rails.
Más información: <https://guides.rubyonrails.org/command_line.html#bin-rails-server>.

- Ejecuta el servidor web:

`rails server`

- Ejecuta el servidor web en el puerto especificado:

`rails server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_puerto</span>

- Ejecuta el servidor web en una dirección IP especificada:

`rails server --binding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>

- Ejecuta el servidor web en un entorno especificado:

`rails server --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entorno</span>

- Muestra la ayuda:

`rails server --help`
