---
layout: page
title: common/kubectl-taint (한국어)
description: "노드에 taint 업데이트."
content_hash: 2c08808684f58e17f48e0a94af023a257449e706
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubectl-taint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl taint

노드에 taint 업데이트.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint>.

- 노드에 taint 적용:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨_키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨_값</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">효과</span>

- 노드에서 taint 제거:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨_키</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">효과</span>`-`

- 노드에서 모든 taint 제거:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨_키</span>`-`
