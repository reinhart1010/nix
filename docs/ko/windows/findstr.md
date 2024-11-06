---
layout: page
title: windows/findstr (한국어)
description: "하나 이상의 파일에서 지정된 텍스트를 찾기."
content_hash: eee08babd5e0b86f60c113d02ca65b6f87e51a10
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/findstr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/findstr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/findstr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# findstr

하나 이상의 파일에서 지정된 텍스트를 찾기.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>.

- 모든 파일에서 하나 이상의 문자열 찾기:

`findstr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1 문자열2 ...</span>`" *`

- 파이프된 명령의 출력에서 하나 이상의 문자열 찾기:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | findstr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1 문자열2 ...</span>`"`

- 모든 파일을 [s]재귀적으로 검색하여 하나 이상의 문자열 찾기:

`findstr /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1 문자열2 ...</span>`" *`

- 대소문자를 구분하지 않고 문자열 찾기:

`findstr /i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1 문자열2 ...</span>`" *`

- 정규 표현식을 사용하여 모든 파일에서 문자열 찾기:

`findstr /r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>`" *`

- 모든 텍스트 파일에서 공백이 포함된 문자열을 그대로 찾기:

`findstr /c:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1 문자열2 ...</span>`" *.txt`

- 일치하는 각 줄 앞에 줄 번호 표시:

`findstr /n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1 문자열2 ...</span>`" *`

- 일치하는 내용을 포함하는 파일 이름만 표시:

`findstr /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열1 문자열2 ...</span>`" *`
