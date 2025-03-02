---
layout: page
title: common/kubeadm (español)
description: "Interfaz de línea de comandos para crear y gestionar clusters Kubernetes."
content_hash: c84bd31ed8b92245948aed9768044494eb3a86fb
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/kubeadm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kubeadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubeadm

Interfaz de línea de comandos para crear y gestionar clusters Kubernetes.
Más información: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

- Crea un plano de control de Kubernetes:

`kubeadm init`

- Arranca un nodo trabajador de Kubernetes y lo une a un clúster:

`kubeadm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Crea un nuevo token de arranque con un TTL de 12 horas:

`kubeadm token create --ttl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12h0m0s</span>

- Comprueba si el clúster Kubernetes es actualizable y qué versiones están disponibles:

`kubeadm upgrade plan`

- Actualiza el clúster Kubernetes a la versión especificada:

`kubeadm upgrade apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Observa el ConfigMap de kubeadm que contiene la configuración del clúster:

`kubeadm config view`

- Revierte los cambios realizados en el host por `kubeadm init` o `kubeadm join`:

`kubeadm reset`
