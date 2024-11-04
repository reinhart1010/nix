---
layout: page
title: windows/if (한국어)
description: "배치 스크립트에서 조건부 처리를 수행합니다."
content_hash: e0a2d9809b4c68ccdd98bd86c7296f3d93e6da0c
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/if.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/if.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/if.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># if

배치 스크립트에서 조건부 처리를 수행합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/if>.

- 조건이 참이면 지정된 명령을 실행:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조건</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is true</span>`)`

- 조건이 거짓이면 지정된 명령을 실행:

`if not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조건</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is true</span>`)`

- 조건이 참이면 첫 번째 지정된 명령을 실행하고, 거짓이면 두 번째 지정된 명령을 실행:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조건</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is true</span>`) else (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is false</span>`)`

- `%errorlevel%`이 지정된 종료 코드보다 크거나 같은지 확인:

`if errorlevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is true</span>`)`

- 두 문자열이 같은지 확인:

`if %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`% == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is true</span>`)`

- 대소문자를 구분하지 않고 두 문자열이 같은지 확인:

`if /i %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`% == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is true</span>`)`

- 파일이 존재하는지 확인:

`if exist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 조건 is true</span>`)`
