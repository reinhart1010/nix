---
layout: page
title: common/googler (한국어)
description: "명령줄에서 Google 검색하기."
content_hash: c5f852da13a6572e8fb6cb5a2c666dc6fd866b17
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/googler.html
    icon: bi bi-globe
tldri18n_status: 2
---
# googler

명령줄에서 Google 검색하기.
더 많은 정보: <https://github.com/jarun/googler>.

- Google에서 키워드 검색:

`googler `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- Google을 검색하고 웹 브라우저에서 첫 번째 결과를 열기:

`googler -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- N개의 검색 결과 표시 (기본값 10):

`googler -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 자동 맞춤법 교정 비활성화:

`googler -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 하나의 사이트에서 키워드를 검색:

`googler -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사이트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- Google 검색 결과를 JSON 형식으로 표시:

`googler --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 내부적으로 자체 업그레이드 수행:

`googler -u`

- 대화형 모드에서 도움말 표시:

`?`
