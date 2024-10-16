---
layout: page
title: common/ed (한국어)
description: "Unix의 원본 텍스트 편집기."
content_hash: af39f2e77120112947ea9010ca7e48bc111b62a8
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/ed.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ed

Unix의 원본 텍스트 편집기.
참고: `awk`, `sed`.
더 많은 정보: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- 빈 문서로 대화형 편집기 세션을 시작:

`ed`

- 빈 문서와 특정 프롬프트로 대화형 편집기 세션을 시작:

`ed --prompt='> '`

- 사용자에게 친숙한 오류로 대화형 편집기 세션을 시작:

`ed --verbose`

- 진단, 바이트 수 및 '!' 프롬프트가 없는 빈 문서로 대화형 편집기 세션을 시작:

`ed --quiet`

- 명령이 실패할 때, 종료 상태 변경 없이 대화형 편집기 세션을 시작:

`ed --loose-exit-status`

- 특정 파일을 편집 (로드된 파일의 바이트가 표시):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 문자열을 모든 줄에 대한 특정 대체 문자열로 대체:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[대체_문자열]</span>`/g`
