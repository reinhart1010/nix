---
layout: page
title: common/helm (italiano)
description: "Helm è un gestore di pacchetti per Kubernetes."
content_hash: c5888aca7398b3a40bc38c075c07ba8a3c8829e9
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/helm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/helm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/helm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helm

Helm è un gestore di pacchetti per Kubernetes.
Alcuni comandi aggiuntivi, come `install`, hanno la propria documentazione.
Maggiori informazioni: <https://helm.sh/>.

- Crea una helm chart:

`helm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_chart</span>

- Aggiungi un nuovo repository helm:

`helm repo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository</span>

- Elenca i repositories helm:

`helm repo list`

- Aggiorna i repositories helm:

`helm repo update`

- Cancella un repository helm:

`helm repo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository</span>

- Installa una helm chart:

`helm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_chart</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_chart</span>

- Scarica una helm chart sottoforma di archivio tar:

`helm get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_chart_rilasciata</span>

- Aggiorna le dipendenze helm:

`helm dependency update`
