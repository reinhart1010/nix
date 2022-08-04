---
layout: page
title: common/clang (한국어)
description: "C, C++ 그리고 Objective-C 소스 파일을 컴파일합니다. GCC의 드롭인 대체로 사용할 수 있습니다."
content_hash: 1db59dcd06946d9d66a551cfebdb80cf4ab27a72
related_topics:
  - title: English version
    url: /en/common/clang.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clang.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clang.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clang

C, C++ 그리고 Objective-C 소스 파일을 컴파일합니다. GCC의 드롭인 대체로 사용할 수 있습니다.
더 많은 정보: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- 실행 가능한 바이너리 파일로 소스 코드를 컴파일합니다:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_소스.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_실행가능파일</span>

- 모든 에러와 경고 메시지를 출력하도록 활성화합니다:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_소스.c</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_실행가능파일</span>

- 소스 파일과 다른 경로에 있는 라이브러리를 포함합니다:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_소스.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_실행가능파일</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">헤더_경로</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리_경로</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리명</span>

- 소스 코드를 LLVM Intermediate Representation(IR)로 컴파일 합니다:

`clang -S -emit-llvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.ll</span>
