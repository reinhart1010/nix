---
layout: page
title: common/helm (español)
description: "Helm es un gestor de paquetes para Kubernetes."
content_hash: 1f1c299ee86367c29ddba06395ec8429e1c2da62
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/helm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/helm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/helm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helm

Helm es un gestor de paquetes para Kubernetes.
Algunos subcomandos como `install` tiene su propia documentación de uso.
Más información: <https://helm.sh/>.

- Crea un chart de helm:

`helm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_chart</span>

- Añade un nuevo repositorio de helm:

`helm repo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_repositorio</span>

- Lista de repositorios de helm:

`helm repo list`

- Actualiza los repositorios de helm:

`helm repo update`

- Elimina un repositorio de helm:

`helm repo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_repositorio</span>

- Instala un chart de helm:

`helm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_repositorio</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_chart</span>

- Descarga un chart de helm como un archivo tar:

`helm get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_lanzamiento_del_chart</span>

- Actualiza las dependencias de helm:

`helm dependency update`
