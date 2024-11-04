---
layout: page
title: common/html5validator (한국어)
description: "HTML5 유효성 검증."
content_hash: 9965b8ffcb0cfe99c63cb910eb08d49a5fdba9ad
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/html5validator.html
    icon: bi bi-globe
tldri18n_status: 2
---
# html5validator

HTML5 유효성 검증.
더 많은 정보: <https://github.com/svenkreiss/html5validator>.

- 특정 파일 유효성 검증:

`html5validator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 디렉토리에 있는 모든 HTML 파일의 유효성을 검사:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 경고와 오류 표시:

`html5validator --show-warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- glob 패턴을 사용하여 여러 파일을 일치시킴:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html *.php</span>`"`

- 특정 디렉터리 이름 무시:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --blacklist "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_modules vendor</span>`"`

- 특정 형식으로 결과를 출력:

`html5validator --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnu|xml|json|text</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 상세 수준으로 로그를 출력:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warning</span>
