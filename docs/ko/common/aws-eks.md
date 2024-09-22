---
layout: page
title: common/aws-eks (한국어)
description: "Amazon Elastic Kubernetes Service (EKS) 애드온, 클러스터 및 노드 그룹 관리."
content_hash: 0957e75f9dcb8b9619fc89f112068c3616211512
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-eks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws eks

Amazon Elastic Kubernetes Service (EKS) 애드온, 클러스터 및 노드 그룹 관리.
Amazon EKS는 AWS에서 Kubernetes를 쉽게 실행하기 위한 서비스.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html>.

- EKS 클러스터 생성:

`aws eks create-cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eks_service_role_arn</span>` --resources-vpc-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnetIds=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnet_ids</span>`,securityGroupIds=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">security_group_ids}</span>`}`

- EKS 클러스터에 연결하기 위한 kubeconfig를 업데이트:

`aws eks update-kubeconfig --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 사용 가능한 EKS 클러스터 목록 나열:

`aws eks list-clusters`

- Describe EKS 클러스터 세부정보 나열:

`aws eks describe-cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- EKS 클러스터 삭제:

`aws eks delete-cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- EKS 클러스터의 노드그룹 나열:

`aws eks list-nodegroups --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 노드 그룹 세부 정보 표시:

`aws eks describe-nodegroup --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --nodegroup-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드그룹_이름</span>
