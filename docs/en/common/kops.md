---
layout: page
title: common/kops (English)
description: "Create, destroy, upgrade and maintain Kubernetes clusters from the command-line."
content_hash: 2cc814f16d8c948c5baf9a451bab8c2f57d8e22a
---
# kops

Create, destroy, upgrade and maintain Kubernetes clusters from the command-line.
More information: <https://github.com/kubernetes/kops/>.

- Create a cluster from the configuration specification:

`kops create cluster -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name.yaml</span>

- Create a new ssh public key:

`kops create secret sshpublickey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/id_rsa.pub</span>

- Export the cluster configuration to the `~/.kube/config` file:

`kops export kubecfg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Get the cluster configuration as YAML:

`kops get cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` -o yaml`

- Delete a cluster:

`kops delete cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --yes`
