---
layout: page
title: common/dvc-unfreeze (한국어)
description: "DVC 파이프라인에서 스테이지의 동결을 해제."
content_hash: 972d3f5d5b5e4e611320bb0e9d2e801a00d63c0d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/dvc-unfreeze.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc unfreeze

DVC 파이프라인에서 스테이지의 동결을 해제.
이는 동결된 후 스테이지의 의존성 변경 사항을 DVC가 다시 추적할 수 있게 합니다.
같이 보기: `dvc freeze`.
더 많은 정보: <https://dvc.org/doc/command-reference/unfreeze>.

- 하나 이상의 지정된 스테이지 동결 해제:

`dvc unfreeze `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스테이지_이름1 스테이지_이름2 ...</span>
