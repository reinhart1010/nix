---
layout: page
title: common/helm (English)
description: "Helm is a package manager for Kubernetes."
content_hash: 8d9c165a7743445d445b71c94b909896a44eceeb
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/helm.html
    icon: bi bi-globe
---
# helm

Helm is a package manager for Kubernetes.
Some subcommands such as `helm install` have their own usage documentation.
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
