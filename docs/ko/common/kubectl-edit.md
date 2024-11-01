---
layout: page
title: common/kubectl-edit (한국어)
description: "Kubernetes 리소스를 편집."
content_hash: 99a74c17e707d406ec678a8c257da37211567672
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubectl-edit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl edit

Kubernetes 리소스를 편집.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#edit>.

- Pod 편집:

`kubectl edit pod/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_이름</span>

- Deployment 편집:

`kubectl edit deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_이름</span>

- Service 편집:

`kubectl edit svc/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_이름</span>

- 특정 편집기를 사용하여 리소스 편집:

`KUBE_EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nano</span>` kubectl edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_이름</span>

- JSON 형식으로 리소스 편집:

`kubectl edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_이름</span>` --output json`
