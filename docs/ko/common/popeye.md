---
layout: page
title: common/popeye (한국어)
description: "Kubernetes 배포 매니페스트의 잠재적 문제 보고."
content_hash: b8a6a81f04398044489f9474c11fa437083f1a61
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/popeye.html
    icon: bi bi-globe
tldri18n_status: 2
---
# popeye

Kubernetes 배포 매니페스트의 잠재적 문제 보고.
더 많은 정보: <https://github.com/derailed/popeye>.

- 현재 Kubernetes 클러스터 스캔:

`popeye`

- 특정 네임스페이스 스캔:

`popeye -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 특정 Kubernetes 컨텍스트 스캔:

`popeye --context=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨텍스트</span>

- 스캐닝에 스피니치 구성 파일 사용:

`popeye -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spinach.yaml</span>
