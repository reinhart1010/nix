---
layout: page
title: common/kubectl (português (Brasil))
description: "Linha de comando para executar comando em clusters do Kubernetes."
content_hash: 84337b424ad50a21fd1729bcf04c5c1082a1e8bf
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/kubectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl

Linha de comando para executar comando em clusters do Kubernetes.
Alguns subcomandos como `run` tem sua própia documentação de uso.
Mais informações: <https://kubernetes.io/docs/reference/kubectl/>.

- Lista toda a informação sobre um recurso em detalhes:

`kubectl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|service|deployment|ingress|...</span>` -o wide`

- Atualiza um pod específico com o label 'unhealthy' e o valor 'true':

`kubectl label pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` unhealthy=true`

- Lista todos os recursos de diferentes tipos:

`kubectl get all`

- Exibe os usos de recursos (CPU/Memória/Espaço alocado) dos nós ou pods:

`kubectl top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|node</span>

- Exibe os endereços dos serviços do master e do cluster:

`kubectl cluster-info`

- Exibe uma explicação de um campo específico:

`kubectl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pods.spec.containers</span>

- Exibe os logs de um container em um pod ou de um recurso específico:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Executa um comando em um pod existente:

`kubectl exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls /</span>
