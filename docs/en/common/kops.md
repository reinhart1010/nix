---
layout: page
title: common/kops (English)
description: "Create, destroy, upgrade and maintain Kubernetes clusters."
content_hash: aeff9340457c56d9afc8766296b97d90b2ca23c3
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# kops

Create, destroy, upgrade and maintain Kubernetes clusters.
More information: <https://github.com/kubernetes/kops/>.

- Create a cluster from the configuration specification:

`kops create cluster -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name.yaml</span>

- Create a new SSH public key:

`kops create secret sshpublickey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/id_rsa.pub</span>

- Export the cluster configuration to the `~/.kube/config` file:

`kops export kubecfg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Get the cluster configuration as YAML:

`kops get cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` -o yaml`

- Delete a cluster:

`kops delete cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --yes`

- Validate a cluster:

`kops validate cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wait_time_until_ready</span>` --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_required_validations</span>
