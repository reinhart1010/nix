---
layout: page
title: common/cppclean (한국어)
description: "C++ 프로젝트에서 사용하지 않는 코드 찾기."
content_hash: 60e3973254f3a35cd14c0b91803017fe15ad48e3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cppclean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cppclean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cppclean

C++ 프로젝트에서 사용하지 않는 코드 찾기.
더 많은 정보: <https://github.com/myint/cppclean>.

- 프로젝트 디렉토리에서 실행:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트/의/경로</span>

- 헤더가 `inc1/` 및 `inc2/` 디렉토리에 있는 프로젝트에서 실행:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트/의/경로</span>` --include-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc1</span>` --include-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc2</span>

- 특정 팡리 `main.cpp`에서 실행:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main.cpp</span>

- `build`디렉토리를 제외한 현재 디렉토리에서 실행:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>
