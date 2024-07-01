---
layout: page
title: common/kubectl-logs (español)
description: "Muestra los registros de los contenedores de un pod."
content_hash: c22220a77070509e04de4e604dba016b5b316bfd
last_modified_at: 2024-07-01
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-logs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl logs

Muestra los registros de los contenedores de un pod.
Más información: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

- Muestra los registros de un pod de un contenedor:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_pod</span>

- Muestra los registros de un contenedor especificado en un pod:

`kubectl logs --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Muestra los registros de todos los contenedores de un pod:

`kubectl logs --all-containers=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Transmite los registros del pod:

`kubectl logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_pod</span>

- Muestra los registros de pods más recientes dado un tiempo relativo como `10s`, `5m` o `1h`:

`kubectl logs --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_relativo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_pod</span>

- Muestra los 10 registros más recientes de un pod:

`kubectl logs --tail=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_pod</span>

- Muestra todos los registros de un pod para un despliegue determinado:

`kubectl logs deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_despliegue</span>
