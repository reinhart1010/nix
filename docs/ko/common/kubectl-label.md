---
layout: page
title: common/kubectl-label (한국어)
description: "Kubernetes 리소스에 레이블 지정."
content_hash: 7d0a89ffa5c9af3802727ce5e198d6009322ddb8
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubectl-label.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl label

Kubernetes 리소스에 레이블 지정.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label>.

- 포드에 레이블 지정:

`kubectl label pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 기존 값을 덮어쓰며 포드 레이블 업데이트:

`kubectl label --overwrite pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 네임스페이스의 모든 포드에 레이블 지정:

`kubectl label pods --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 포드 정의 파일로 식별된 포드에 레이블 지정:

`kubectl label -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_정의_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 포드에서 레이블 제거:

`kubectl label pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`-`
