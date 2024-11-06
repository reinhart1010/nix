---
layout: page
title: windows/find (한국어)
description: "파일에서 지정된 문자열 찾기."
content_hash: b19e31f6e3f910e6950177c96838e7fb99dd663f
last_modified_at: 2024-11-06
related_topics:
  - title: বাংলা version
    url: /bn/windows/find.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/find.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/find.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/find.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/find.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/find.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

파일에서 지정된 문자열 찾기.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- 지정된 문자열을 포함하는 줄 찾기:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_폴더</span>

- 지정된 문자열을 포함하지 않는 줄 표시:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_폴더</span>` /v`

- 지정된 문자열을 포함하는 줄의 개수 표시:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_폴더</span>` /c`

- 줄 번호와 함께 줄 목록 표시:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_폴더</span>` /n`
