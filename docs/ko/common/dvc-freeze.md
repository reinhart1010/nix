---
layout: page
title: common/dvc-freeze (한국어)
description: "DVC 파이프라인의 스테이지를 동결."
content_hash: fbae832a5bdadb65e6931d219df49a2f4587fb3d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/dvc-freeze.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc freeze

DVC 파이프라인의 스테이지를 동결.
이는 스테이지 종속성의 변경 사항을 추적하고, 해동될 때까지 재실행을 방지합니다.
같이 보기: `dvc unfreeze`.
더 많은 정보: <https://dvc.org/doc/command-reference/freeze>.

- 하나 이상의 특정 스테이지를 동결:

`dvc freeze `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스테이지_이름1 스테이지_이름2 ...</span>
