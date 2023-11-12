---
layout: page
title: common/kubectl-create (English)
description: "Create a resource from a file or from `stdin`."
content_hash: 8a4dac4e927a5e9b1c67c90734f9d19ede31a096
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kubectl create

Create a resource from a file or from `stdin`.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create>.

- Create a resource using the resource definition file:

`kubectl create -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>

- Create a resource from `stdin`:

`kubectl create -f -`

- Create a deployment:

`kubectl create deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>` --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Create a deployment with replicas:

`kubectl create deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>` --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>` --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_replicas</span>

- Create a service:

`kubectl create service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` --tcp=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_port</span>

- Create a namespace:

`kubectl create namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace_name</span>
