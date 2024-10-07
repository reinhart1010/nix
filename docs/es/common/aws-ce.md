---
layout: page
title: common/aws-ce (español)
description: "Ejecuta operaciones de gestión de costos a través del servicio AWS Cost Explorer."
content_hash: 75724ab06ba8b3156c1855b3cb85800f8cbaa5ca
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/aws-ce.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-ce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ce

Ejecuta operaciones de gestión de costos a través del servicio AWS Cost Explorer.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html>.

- Crea monitor de anomalías:

`aws ce create-anomaly-monitor --monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_monitor</span>` --monitor-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_monitor</span>

- Crea suscripción de anomalías:

`aws ce create-anomaly-subscription --subscription `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_suscripción</span>` --monitor-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_arn</span>` --subscribers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suscriptores</span>

- Obtiene anomalías:

`aws ce get-anomalies --monitor-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_arn</span>` --start-time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hora_de_inicio</span>` --end-time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hora_final</span>

- Obtiene coste y uso:

`aws ce get-cost-and-usage --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fecha_inicio</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fecha_final</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">granularidad</span>` --metrics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">métricas</span>

- Obtiene previsión de costes:

`aws ce get-cost-forecast --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fecha_inicio</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fecha_final</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">granularidad</span>` --metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">métrica</span>

- Obtiene la utilización de la reserva:

`aws ce get-reservation-utilization --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fecha_inicio</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fecha_final</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">granularidad</span>

- Lista de definiciones de categorías de costes:

`aws ce list-cost-category-definitions`

- Recurso de etiquetas:

`aws ce tag-resource --resource-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recurso_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiquetas</span>
