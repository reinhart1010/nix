---
layout: page
title: common/aws-eks (English)
description: "CLI for Amazon EKS (Elastic Kubernetes Service)."
content_hash: 1fa5e12c71ecdecdafa043de838c579ab652964b
last_modified_at: 2023-11-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-eks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws eks

CLI for Amazon EKS (Elastic Kubernetes Service).
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html>.

- Create an EKS Cluster:

`aws eks create-cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eks_service_role_arn</span>` --resources-vpc-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnetIds=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnet_ids</span>`,securityGroupIds=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">security_group_ids}</span>`}`

- Update kubeconfig to connect to the EKS Cluster:

`aws eks update-kubeconfig --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- List available EKS clusters:

`aws eks list-clusters`

- Describe EKS cluster details:

`aws eks describe-cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Delete an EKS Cluster:

`aws eks delete-cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- List nodegroups in an EKS cluster:

`aws eks list-nodegroups --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Describe nodegroup details:

`aws eks describe-nodegroup --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --nodegroup-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodegroup_name</span>
