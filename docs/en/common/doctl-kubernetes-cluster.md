---
layout: page
title: common/doctl-kubernetes-cluster (English)
description: "Manage Kubernetes clusters and view configuration options relating to clusters."
content_hash: feac679dbf334c8e6bc464cb214007b01cc6f219
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# doctl kubernetes cluster

Manage Kubernetes clusters and view configuration options relating to clusters.
More information: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>.

- Create a Kubernetes cluster:

`doctl kubernetes cluster create --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nyc1</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s-1vcpu-2gb</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- List all Kubernetes clusters:

`doctl kubernetes cluster list`

- Fetch and save the kubeconfig:

`doctl kubernetes cluster kubeconfig save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Check for available upgrades:

`doctl kubernetes cluster get-upgrades `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Upgrade a cluster to a new Kubernetes version:

`doctl kubernetes cluster upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Delete a cluster:

`doctl kubernetes cluster delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>
