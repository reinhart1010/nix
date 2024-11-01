---
layout: page
title: windows/pabcnetcclear (한국어)
description: "PascalABC.NET 소스 파일을 전처리하고 컴파일합니다."
content_hash: 13bceaa77378ec557a0844971a774c3a56727bd8
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/windows/pabcnetcclear.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/pabcnetcclear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pabcnetcclear

PascalABC.NET 소스 파일을 전처리하고 컴파일합니다.
더 많은 정보: <https://pascalabc.net>.

- 지정된 소스 파일을 동일한 이름의 실행 파일로 컴파일:

`pabcnetcclear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일.pas</span>

- 지정된 소스 파일을 지정된 이름의 실행 파일로 컴파일:

`pabcnetcclear /Output:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일.pas</span>

- 디버그 정보를 포함하거나 포함하지 않고 동일한 이름의 실행 파일로 지정된 소스 파일을 컴파일:

`pabcnetcclear /Debug:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일.pas</span>

- 컴파일 중 지정된 경로에서 유닛을 검색하도록 허용:

`pabcnetcclear /SearchDir:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일.pas</span>

- 지정된 소스 파일을 실행 파일로 컴파일하고 심볼 정의:

`pabcnetcclear /Define:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">심볼</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일.pas</span>
