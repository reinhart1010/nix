---
layout: page
title: common/argocd-app (español)
description: "Interfaz de línea de comandos para gestionar aplicaciones por CD Argo."
content_hash: cbdb05d49a0eed0b8a46c309751089b1fd1eebe1
last_modified_at: 2023-03-21
related_topics:
  - title: English version
    url: /en/common/argocd-app.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># argocd app

Interfaz de línea de comandos para gestionar aplicaciones por CD Argo.
Más información: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- Lista aplicaciones:

`argocd app list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>` `

- Obtiene detalles de la aplicación:

`argocd app get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicacion</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>

- Despliega la aplicación internamente (en el mismo clúster en el que se ejecuta Argo CD):

`argocd app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicación</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_repo_url</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repo</span>` --dest-server https://kubernetes.default.svc --dest-namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ns</span>

- Elimina una aplicación:

`argocd app delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicación</span>

- Activa la sincronización automática de aplicaciones:

`argocd app set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicacion</span>` --sync-policy auto --auto-prune --self-heal`

- Previsualiza la sincronización de aplicaciones sin afectar al clúster:

`argocd app sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicacion</span>` --dry-run --prune`

- Muestra el historial de despliegue de aplicaciones:

`argocd app history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicacion</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wide|id</span>

- Retrocede la aplicación a una versión anterior desplegada por ID de historial (eliminando recursos inesperados):

`argocd app rollback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicacion</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">history_id</span>` --prune`