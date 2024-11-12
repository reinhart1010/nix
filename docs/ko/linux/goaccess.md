---
layout: page
title: linux/goaccess (한국어)
description: "오픈 소스 실시간 웹 로그 분석기."
content_hash: 02ed56ac24bc28d07b675cd698a3df0ce9de3461
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/goaccess.html
    icon: bi bi-globe
tldri18n_status: 2
---
# goaccess

오픈 소스 실시간 웹 로그 분석기.
더 많은 정보: <https://goaccess.io>.

- 대화형 모드로 하나 이상의 로그 파일 분석:

`goaccess `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그파일1 경로/대상/파일2 ...</span>

- 특정 로그 포맷(또는 "combined" 같은 미리 정의된 포맷) 사용:

`goaccess `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그파일</span>` --log-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포맷</span>

- `stdin`에서 로그 분석:

`tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그파일</span>` | goaccess -`

- 로그를 실시간으로 분석하여 HTML 파일로 작성:

`goaccess `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그파일</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.html</span>` --real-time-html`
