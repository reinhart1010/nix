---
layout: page
title: common/kubectl-config (English)
description: "Manage Kubernetes configuration (kubeconfig) files for accessing clusters via `kubectl` or the Kubernetes API."
content_hash: 1c238487537e6c3f600fac3e7560bf863f09ceb7
last_modified_at: 2024-07-08
tldri18n_status: 2
---
# kubectl config

Manage Kubernetes configuration (kubeconfig) files for accessing clusters via `kubectl` or the Kubernetes API.
By default, the Kubernetes will get its configuration from `${HOME}/.kube/config`.
See also: `kubectx`, `kubens`.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config>.

- Get all contexts in the default kubeconfig file:

`kubectl config get-contexts`

- Get all clusters/contexts/users in a custom kubeconfig file:

`kubectl config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">get-clusters|get-contexts|get-users</span>` --kubeconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/kubeconfig.yaml</span>

- Get the current context:

`kubectl config current-context`

- Switch to another context:

`kubectl config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use|use-context</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context_name</span>

- Delete clusters/contexts/users:

`kubectl config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delete-cluster|delete-context|delete-user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster|context|user</span>

- Permanently add custom kubeconfig files:

`export KUBECONFIG="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME.kube/config:path/to/custom/kubeconfig.yaml</span>`" kubectl config get-contexts`
