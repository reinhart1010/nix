---
layout: page
title: common/gcloud (español)
description: "La herramienta CLI oficial de Google Cloud Platform."
content_hash: cf64c0a079f1682e2f3fc3c0669c12305f64ae52
last_modified_at: 2023-11-26
related_topics:
  - title: dansk version
    url: /da/common/gcloud.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/gcloud.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcloud.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud

La herramienta CLI oficial de Google Cloud Platform.
Más información: <https://cloud.google.com/sdk/gcloud>.

- Lista todas las propiedades de la configuración activa:

`gcloud config list`

- Inicia sesión en la cuenta de Google:

`gcloud auth login`

- Establece como proyecto activo:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proyecto</span>

- SSH en una instancia de máquina virtual:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instancia</span>

- Muestra todas las instancias de Google Compute Engine de un proyecto. Por defecto, se muestran las instancias de todas las zonas:

`gcloud compute instances list`

- Actualiza un archivo kubeconfig con las credenciales adecuadas para apuntar kubectl a un clúster específico en Google Kubernetes Engine:

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_cluster</span>

- Actualiza todos los componentes de la CLI de gcloud:

`gcloud components update`

- Muestra la ayuda para un comando determinado:

`gcloud help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
