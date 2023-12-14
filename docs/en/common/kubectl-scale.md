---
layout: page
title: common/kubectl-scale (English)
description: "Set a new size for a deployment, replica set, replication controller, or stateful set."
content_hash: 67517a111844487b188d8adece044ff5bc5bcfda
last_modified_at: 2023-12-14
tldri18n_status: 2
---
# kubectl scale

Set a new size for a deployment, replica set, replication controller, or stateful set.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale>.

- Scale a replica set:

`kubectl scale --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_replicas</span>` rs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replica_name</span>

- Scale a resource identified by a file:

`kubectl scale --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_replicas</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>

- Scale a deployment based on current number of replicas:

`kubectl scale --current-replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current_replicas</span>` --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_replicas</span>` deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>
