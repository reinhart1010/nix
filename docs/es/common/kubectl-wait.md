---
layout: page
title: common/kubectl-wait (español)
description: "Espera a que los recursos alcancen un estado determinado."
content_hash: 66f28d73587ea75917f6cf65d47f9a0be4004abd
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/kubectl-wait.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl wait

Espera a que los recursos alcancen un estado determinado.
Más información: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#wait>.

- Espera a que un despliegue esté disponible:

`kubectl wait --for=condition=available deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_despliegue</span>

- Espera a que todos los pods con una determinada etiqueta ([l]) estén listos:

`kubectl wait --for=condition=ready pod -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta_clave</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta_valor</span>

- Espera a que se elimine un pod:

`kubectl wait --for=delete pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_pod</span>

- Espera a que se complete un trabajo, en un plazo de 120 segundos (si la condición no se cumple a tiempo, el estado de salida será fallido):

`kubectl wait --for=condition=complete job/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_trabajo</span>` --timeout 120s`
