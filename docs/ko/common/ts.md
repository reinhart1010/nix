---
layout: page
title: common/ts (한국어)
description: "`stdin`의 각 줄에 타임스탬프를 추가."
content_hash: 4d4ce553b9bd751d340e16fd49aea9fa6a04678a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/ts.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ts

`stdin`의 각 줄에 타임스탬프를 추가.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 각 줄의 시작에 타임스탬프 추가:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | ts`

- 마이크로초 정밀도의 타임스탬프 추가:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | ts "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%b %d %H:%M:%.S</span>`"`

- 0부터 시작하여 마이크로초 정밀도의 [i]증분 타임스탬프 추가:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | ts -i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%H:%M:%.S</span>`"`

- 텍스트 파일(예: 로그 파일)의 기존 타임스탬프를 [r]상대적 형식으로 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | ts -r`
