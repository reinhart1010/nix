---
layout: page
title: common/csc (한국어)
description: "마이크로 소프트 사의 C# 컴파일러."
content_hash: 71c58d3f5e7794f968c559cbbc442c002f2a8789
related_topics:
  - title: English version
    url: /en/common/csc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csc.html
    icon: bi bi-globe
---
# csc

마이크로 소프트 사의 C# 컴파일러.
더 많은 정보: <https://docs.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

- 하나 이상의 C# 파일을 CIL 실행파일로 컴파일:

`csc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일_a.cs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일_b.cs</span>

- 출력 파일 이름 지정:

`csc /out:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일.cs</span>

- 실행 파일 대신 '.dll' 라이브러리로 컴파일:

`csc /target:library `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일.cs</span>

- 다른 어셈블리 참조:

`csc /reference:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/라이브러리.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일.cs</span>

- 리소스 포함:

`csc /resource:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/리소스파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일.cs</span>

- XML 문서 자동 생성:

`csc /doc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/출력파일.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일.cs</span>

- 아이콘 지정:

`csc /win32icon:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/아이콘.ico</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일.cs</span>

- 키 파일을 사용하여 결과 어셈블리의 이름 지정:

`csc /keyfile:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/키파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/입력파일.cs</span>
