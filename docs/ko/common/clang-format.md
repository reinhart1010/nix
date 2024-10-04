---
layout: page
title: common/clang-format (한국어)
description: "C/C++/Java/JavaScript/Objective-C/Protobuf/C# 코드 자동 형식화."
content_hash: 9d4ff3d67c0e403107d73bbb500464d3b7f53524
last_modified_at: 2024-10-04
related_topics:
  - title: Deutsch version
    url: /de/common/clang-format.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clang-format.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clang-format

C/C++/Java/JavaScript/Objective-C/Protobuf/C# 코드 자동 형식화.
더 많은 정보: <https://clang.llvm.org/docs/ClangFormat.html>.

- 파일 형식을 지정하고 결과를 `stdout`으로 출력:

`clang-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 그 자리에서 파일 형식을 지정:

`clang-format -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 미리 정의된 코딩 스타일을 사용하여 파일 형식을 지정:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 소스 파일의 상위 디렉터리 중 하나에 있는 `.clang-format` 파일을 사용하여 파일 형식을 지정:

`clang-format --style=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자 정의 `.clang-format` 파일을 생성:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` --dump-config > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.clang-format</span>
