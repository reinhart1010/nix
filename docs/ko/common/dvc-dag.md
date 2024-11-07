---
layout: page
title: common/dvc-dag (한국어)
description: "`dvc.yaml`에 정의된 파이프라인을 시각화."
content_hash: c2d7a69dff393f541fbb9450118377e2b62fac66
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/dvc-dag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc dag

`dvc.yaml`에 정의된 파이프라인을 시각화.
더 많은 정보: <https://dvc.org/doc/command-reference/dag>.

- 전체 파이프라인 시각화:

`dvc dag`

- 지정된 대상 스테이지까지의 파이프라인 스테이지 시각화:

`dvc dag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 파이프라인을 dot 형식으로 내보내기:

`dvc dag --dot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파이프라인.dot</span>
