---
layout: page
title: common/kubectl-create (한국어)
description: "파일 또는 `stdin`에서 리소스를 생성."
content_hash: eccf811d630fda24b54654aa3b68294c050c16b4
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubectl-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl create

파일 또는 `stdin`에서 리소스를 생성.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create>.

- 리소스 정의 파일을 사용하여 리소스 생성:

`kubectl create -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yml</span>

- `stdin`에서 리소스 생성:

`kubectl create -f -`

- 배포 생성:

`kubectl create deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_이름</span>` --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 복제본과 함께 배포 생성:

`kubectl create deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_이름</span>` --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>` --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">복제본_수</span>

- 서비스 생성:

`kubectl create service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` --tcp=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_포트</span>

- 네임스페이스 생성:

`kubectl create namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스_이름</span>
