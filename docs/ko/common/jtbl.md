---
layout: page
title: common/jtbl (한국어)
description: "JSON 및 JSON Lines 데이터를 터미널에서 표 형태로 출력하는 유틸리티."
content_hash: 1f6689a591f048f4b2ecd72606b2fe729556e18e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jtbl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jtbl

JSON 및 JSON Lines 데이터를 터미널에서 표 형태로 출력하는 유틸리티.
더 많은 정보: <https://github.com/kellyjonbrazil/jtbl>.

- JSON 또는 JSON Lines 입력으로부터 표 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jtbl`

- 표를 출력하고 열 너비를 지정하여 줄 바꿈 설정:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jtbl --cols=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>

- 표를 출력하고 줄 바꿈 대신 행 잘라내기:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jtbl -t`

- 표를 출력하고 행을 줄 바꾸거나 잘라내지 않음:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` | jtbl -n`
