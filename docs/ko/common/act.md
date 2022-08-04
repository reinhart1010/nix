---
layout: page
title: common/act (한국어)
description: "Docker를 사용하여 로컬로 GitHub작업 실행."
content_hash: d13d0dd09abf464ca26c8b3a599f16fedb0aa75c
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
---
# act

Docker를 사용하여 로컬로 GitHub작업 실행.
더 많은 정보: <https://github.com/nektos/act>.

- 가능한 작업들 목록:

`act -l`

- 기본 이벤트 실행:

`act`

- 특정 이벤트 실행:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_type</span>

- 특정 작업 실행:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_id</span>

- 실제론 작업을 실행하지 않기 (예 : a dry run):

`act -n`

- 자세한 로그 표시:

`act -v`
