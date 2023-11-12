---
layout: page
title: common/kubectl-expose (English)
description: "Expose a resource as a new Kubernetes service."
content_hash: 39b7a6e5609b5bb04cbbae37d40b62070a440737
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kubectl edit

Expose a resource as a new Kubernetes service.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose>.

- Create a service for a resource, which will be served from container port to node port:

`kubectl expose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_port</span>` --target-port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_port</span>

- Create a service for a resource identified by a file:

`kubectl expose -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_port</span>` --target-port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_port</span>

- Create a service with a name, to serve to a node port which will be same for container port:

`kubectl expose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_port</span>` --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>
