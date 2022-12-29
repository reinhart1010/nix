---
layout: page
title: common/kubectl (italiano)
description: "Interfaccia interattiva da linea di comando per eseguire comandi sui clusters Kubernetes."
content_hash: b5c9e736e55c221a56911b0e33996103510320c4
last_modified_at: 2022-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kubectl.html
    icon: bi bi-globe
---
# kubectl

Interfaccia interattiva da linea di comando per eseguire comandi sui clusters Kubernetes.
Alcuni comandi aggiuntivi, come `kubectl run`, hanno la propria documentazione..
Maggiori informazioni: <https://kubernetes.io/docs/reference/kubectl/>.

- Elenca le informazioni su una risorsa in maniera dettagliata:

`kubectl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|service|deployment|ingress|...</span>` -o wide`

- Aggiorna il pod specificato con l'etichetta 'unhealthy' e il valore 'true':

`kubectl label pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` unhealthy=true`

- Elenca tutte le risorse:

`kubectl get all`

- Mostra l'utilizzo delle risorse (CPU/Memory/Storage) di nodi o pods:

`kubectl top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|nodo</span>

- Mostra l'indirizzo del master e i servizi del cluster:

`kubectl cluster-info`

- Mostra la spiegazione di un campo specifico:

`kubectl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pods.spec.containers</span>

- Mostra i logs di un container in un pod o in una risorsa specificata:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pod</span>

- Esegue un commando in un pod esistente:

`kubectl exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pod</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls /</span>
