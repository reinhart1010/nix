---
layout: page
title: common/argocd-app (español)
description: "Interfaz de línea de comandos para gestionar aplicaciones por CD Argo."
content_hash: e9a0007fd07d855b2230b3cdd6e4993f264fb119
last_modified_at: 2024-05-22
related_topics:
  - title: English version
    url: /en/common/argocd-app.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argocd-app.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd app

Interfaz de línea de comandos para gestionar aplicaciones por CD Argo.
Más información: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- Lista aplicaciones:

`argocd app list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>

- Obtén los detalles de la aplicación:

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

`argocd app rollback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_aplicacion</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_historial</span>` --prune`
