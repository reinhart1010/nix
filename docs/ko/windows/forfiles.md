---
layout: page
title: windows/forfiles (한국어)
description: "지정한 명령어를 실행할 파일을 선택."
content_hash: 09c2c8100852636cc520f3731adaca1e9df44013
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/forfiles.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/forfiles.html
    icon: bi bi-globe
tldri18n_status: 2
---
# forfiles

지정한 명령어를 실행할 파일을 선택.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- 현재 디렉토리에서 파일 검색:

`forfiles`

- 특정 디렉토리에서 파일 검색:

`forfiles /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>

- 각 파일에 대해 지정된 명령어 실행:

`forfiles /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 특정 글로브 패턴을 사용하여 파일 검색:

`forfiles /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">글로브_패턴</span>

- 파일을 재귀적으로 검색:

`forfiles /s`

- 5일 이상된 파일 검색:

`forfiles /d +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
