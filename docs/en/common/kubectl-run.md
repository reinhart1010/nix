---
layout: page
title: common/kubectl-run (English)
description: "Run pods in Kubernetes. Specifies pod generator to avoid deprecation error in some K8S versions."
content_hash: a9d8995587fc55b85228fd78366ec7c88dd8c0ed
last_modified_at: 2023-08-26
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-run.html
    icon: bi bi-globe
---
# kubectl run

Run pods in Kubernetes. Specifies pod generator to avoid deprecation error in some K8S versions.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Run an nginx pod and expose port 80:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --port 80`

- Run an nginx pod, setting the TEST_VAR environment variable:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --env="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TEST_VAR</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testing</span>`"`

- Show API calls that would be made to create an nginx container:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --dry-run=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|server|client</span>

- Run an Ubuntu pod interactively, never restart it, and remove it when it exits:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temp-ubuntu</span>` --image=ubuntu:22.04 --restart=Never --rm -- /bin/bash`

- Run an Ubuntu pod, overriding the default command with echo, and specifying custom arguments:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temp-ubuntu</span>` --image=ubuntu:22.04 --command -- echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>
