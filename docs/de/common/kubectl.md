---
layout: page
title: common/kubectl (Deutsch)
description: "Befehlszeilenschnittstelle zur Ausführung von Befehlen gegen Kubernetes-Cluster."
content_hash: 2d951af8547b179aeccca3c72ba98977e543bfc4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/kubectl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/kubectl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kubectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl

Befehlszeilenschnittstelle zur Ausführung von Befehlen gegen Kubernetes-Cluster.
Einige Unterbefehle wie `kubectl run` haben ihre eigene Dokumentation zur Verwendung.
Weitere Informationen: <https://kubernetes.io/docs/reference/kubectl/>.

- Liste Informationen über eine Ressource mit weiteren Details auf:

`kubectl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|service|deployment|ingress|...</span>` --output wide`

- Aktualisiere die angegebenen Pods mit dem Label 'unhealthy' und dem Wert 'true':

`kubectl label pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` unhealthy=true`

- Liste alle Ressourcen aller Typen auf:

`kubectl get all`

- Zeige die Ressourcennutzung (CPU/Memory/Storage) von Knoten oder Pods:

`kubectl top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|node</span>

- Zeige die Adresse der Master- und Clusterdienste:

`kubectl cluster-info`

- Zeige eine Erklärung zu einem bestimmten Feld an:

`kubectl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pods.spec.containers</span>

- Zeige Logs für einen Container in einem Pod oder einer bestimmten Ressource:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Führe einen Befehl in einem bestehenden Pod aus:

`kubectl exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls /</span>
