---
layout: page
title: osx/ed (한국어)
description: "오리지널 유닉스 텍스트 편집기."
content_hash: 4ecf8484affa782438e9d2448dba5c169a735d1e
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/ed.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/ed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ed

오리지널 유닉스 텍스트 편집기.
같이 보기: `awk`, `sed`.
더 많은 정보: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- 빈 문서로 대화형 편집기 세션 시작:

`ed`

- 빈 문서로 특정 [p]프롬프트와 함께 대화형 편집기 세션 시작:

`ed -p '> '`

- 빈 문서로 진단, 바이트 수, '!' 프롬프트 없이 대화형 편집기 세션 시작:

`ed -s`

- 특정 [f]파일 편집 (로딩된 파일의 바이트 수를 표시):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 줄에서 문자열을 특정 교체문으로 대체:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">교체문</span>`/g`
