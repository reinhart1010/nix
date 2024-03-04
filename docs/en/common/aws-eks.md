---
layout: page
title: common/aws-eks (English)
description: "Manage Amazon Elastic Kubernetes Service (EKS) addons, clusters, and node groups."
content_hash: becc41bbdcbfdac5595b228fa3bea0721769dd6f
last_modified_at: 2024-03-04
tldri18n_status: 2
---
# aws eks

Manage Amazon Elastic Kubernetes Service (EKS) addons, clusters, and node groups.
Amazon EKS is a service for easily running Kubernetes on AWS.
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
