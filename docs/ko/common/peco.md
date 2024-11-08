---
layout: page
title: common/peco (한국어)
description: "인터랙티브 필터링 도구."
content_hash: 0f556e7349d6cdc412687111ebf6ca4982c53d7d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/peco.html
    icon: bi bi-globe
tldri18n_status: 2
---
# peco

인터랙티브 필터링 도구.
더 많은 정보: <https://github.com/peco/peco>.

- 지정된 디렉터리의 모든 파일에서 `peco` 시작:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -type f | peco`

- 실행 중인 프로세스에서 `peco` 시작:

`ps aux | peco`

- 지정된 쿼리와 함께 `peco` 시작:

`peco --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`"`
