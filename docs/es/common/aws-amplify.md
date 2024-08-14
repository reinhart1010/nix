---
layout: page
title: common/aws-amplify (español)
description: "Plataforma de desarrollo para crear aplicaciones móviles y web seguras y escalables."
content_hash: 24bcf241fd4995d3d2d08ed1a20652fde4502bc7
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/common/aws-amplify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws amplify

Plataforma de desarrollo para crear aplicaciones móviles y web seguras y escalables.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html>.

- Crea una nueva aplicación Amplify:

`aws amplify create-app --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_app</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">descripción</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositorio</span>` --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>` --environment-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variables_de_entorno</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiquetas</span>

- Elimina una aplicación Amplify existente:

`aws amplify delete-app --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_aplicación</span>

- Obtiene detalles de una aplicación Amplify determinada:

`aws amplify get-app --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_aplicación</span>

- Lista todas las aplicaciones de Amplify:

`aws amplify list-apps`

- Actualiza la configuración de una aplicación Amplify:

`aws amplify update-app --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_aplicación</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_nombre</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nueva_descripción</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_url_repositorio</span>` --environment-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variables_nuevo_entorno</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevas_etiquetas</span>

- Añade un nuevo entorno backend a una aplicación Amplify:

`aws amplify create-backend-environment --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_aplicación</span>` --environment-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_entorno</span>` --deployment-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artefactos</span>

- Elimina un entorno backend de una aplicación Amplify:

`aws amplify delete-backend-environment --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_aplicación</span>` --environment-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_entorno</span>

- Lista todos los entornos backend de una aplicación Amplify:

`aws amplify list-backend-environments --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_aplicación</span>
