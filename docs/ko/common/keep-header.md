---
layout: page
title: common/keep-header (한국어)
description: "첫 번째 줄을 명령어에 의해 처리하지 않고 그대로 `stdout`에 전달."
content_hash: 7d73eefcca4862b0ec414d74b1172b2e39136948
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/keep-header.html
    icon: bi bi-globe
tldri18n_status: 2
---
# keep-header

첫 번째 줄을 명령어에 의해 처리하지 않고 그대로 `stdout`에 전달.
더 많은 정보: <https://github.com/eBay/tsv-utils#keep-header>.

- 파일을 정렬하고 첫 번째 줄을 맨 위에 유지:

`keep-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -- sort`

- 첫 번째 줄을 `stdout`에 직접 출력하고 파일의 나머지를 지정된 명령어로 처리:

`keep-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `stdin`에서 읽어 첫 번째 줄을 제외한 모든 줄을 정렬:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | keep-header -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 파일을 `grep`하여 검색 패턴에 상관없이 첫 번째 줄을 유지:

`keep-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -- grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>
