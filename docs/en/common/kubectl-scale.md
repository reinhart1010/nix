---
layout: page
title: common/kubectl-scale (English)
description: "Set a new size for a deployment, replica set, replication controller, or stateful set."
content_hash: 371f4b9c0b9dc03964105933d3e81d9fe8f2de2b
last_modified_at: 2023-10-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kubectl edit

Set a new size for a deployment, replica set, replication controller, or stateful set.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale>.

- Scale a replica set:

`kubectl scale --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_replicas</span>` rs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replica_name</span>

- Scale a resource identified by a file:

`kubectl scale --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_replicas</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>

- Scale a deployment based on current number of replicas:

`kubectl scale --current-replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current_replicas</span>` --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_replicas</span>` deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>
