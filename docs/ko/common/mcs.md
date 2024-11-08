---
layout: page
title: common/mcs (한국어)
description: "Mono C# 컴파일러."
content_hash: 9e15ed892e93fa58bf0c9e25954691378fa58ba8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mcs.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/mcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mcs

Mono C# 컴파일러.
더 많은 정보: <https://manned.org/mcs.1>.

- 지정된 파일 컴파일:

`mcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일1.cs 경로/대상/입력_파일2.cs ...</span>

- 출력 프로그램 이름 지정:

`mcs -out:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일1.cs 경로/대상/입력_파일2.cs ...</span>

- 출력 프로그램 유형 지정:

`mcs -target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exe|winexe|library|module</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일1.cs 경로/대상/입력_파일2.cs ...</span>
