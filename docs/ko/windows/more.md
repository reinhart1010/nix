---
layout: page
title: windows/more (한국어)
description: "`stdin` 또는 파일에서 페이지 단위 출력을 표시합니다."
content_hash: dda08eeb492532f041e414b222b19708511a31eb
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/more.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/more.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/more.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/more.html
    icon: bi bi-globe
tldri18n_status: 2
---
# more

`stdin` 또는 파일에서 페이지 단위 출력을 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- `stdin`에서 페이지 단위 출력 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo test</span>` | more`

- 하나 이상의 파일에서 페이지 단위 출력 표시:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 탭을 지정된 수의 공백으로 변환:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` /t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공백</span>

- 페이지 표시 전에 화면 지우기:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` /c`

- 출력을 5번째 줄에서 시작:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 확장된 대화형 모드 활성화 (사용법 보기):

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` /e`

- 도움말 표시:

`more /?`
