---
layout: page
title: common/helm (English)
description: "A package manager for Kubernetes."
content_hash: f7662afb50ed0cd1e00c702a665709a6bb0fccfa
last_modified_at: 2023-11-15
related_topics:
  - title: español version
    url: /es/common/helm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/helm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/helm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helm

A package manager for Kubernetes.
Some subcommands such as `install` have their own usage documentation.
More information: <https://helm.sh/>.

- Create a helm chart:

`helm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chart_name</span>

- Add a new helm repository:

`helm repo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- List helm repositories:

`helm repo list`

- Update helm repositories:

`helm repo update`

- Delete a helm repository:

`helm repo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Install a helm chart:

`helm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chart_name</span>

- Download helm chart as a tar archive:

`helm get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chart_release_name</span>

- Update helm dependencies:

`helm dependency update`
