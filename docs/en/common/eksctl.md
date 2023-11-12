---
layout: page
title: common/eksctl (English)
description: "The official CLI for Amazon EKS."
content_hash: c3d8a07a1f0eab4f292c6b0c12c08fea524ad9d9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# eksctl

The official CLI for Amazon EKS.
More information: <https://eksctl.io>.

- Create a basic cluster:

`eksctl create cluster`

- List the details about a cluster or all of the clusters:

`eksctl get cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --region=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>

- Create a cluster passing all configuration information in a file:

`eksctl create cluster --config-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a cluster using a configuration file and skip creating nodegroups until later:

`eksctl create cluster --config-file=<path> --without-nodegroup`

- Delete a cluster:

`eksctl delete cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --region=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>

- Create cluster and write cluster credentials to a file other than the default:

`eksctl create cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --kubeconfig=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>

- Create a cluster and prevent storing cluster credentials locally:

`eksctl create cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --write-kubeconfig=false`

- Create a cluster and let `eksctl` manage cluster credentials under the `~/.kube/eksctl/clusters` directory:

`eksctl create cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --auto-kubeconfig`
