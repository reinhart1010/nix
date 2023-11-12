---
layout: page
title: common/helm (português (Brasil))
description: "Helm é um gerenciador de pacores para Kubernetes."
content_hash: 63ac665e2b2aaeed90ddcd11e4be4a9e5d66e17f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/helm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/helm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/helm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helm

Helm é um gerenciador de pacores para Kubernetes.
Mais informações: <https://helm.sh/>.

- Cria um chart do helm:

`helm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_chart</span>

- Adiciona um novo repositório helm:

`helm repo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_repositório</span>

- Lista os repositórios helm:

`helm repo list`

- Atualiza os repositórios helm:

`helm repo update`

- Remova um repositório helm:

`helm repo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_repositório</span>

- Instala um chart helm:

`helm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_repositório</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_chart</span>

- Obtém um chart helm chart como um arquivo tar:

`helm get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_release_do_chart</span>

- Atualiza as dependências helm:

`helm dependency update`
