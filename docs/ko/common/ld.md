---
layout: page
title: common/ld (한국어)
description: "오브젝트 파일을 함께 링크."
content_hash: ba273f66fb9de6f7eb0020d91baf5d15de130bff
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ld.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ld.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ld.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ld

오브젝트 파일을 함께 링크.
더 많은 정보: <https://sourceware.org/binutils/docs-2.38/ld.html>.

- 특정 오브젝트 파일을 의존성 없이 실행 파일로 링크:

`ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.o</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>

- 두 오브젝트 파일을 함께 링크:

`ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.o</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>

- x86_64 프로그램을 glibc에 동적으로 링크 (파일 경로는 시스템에 따라 달라짐):

`ld --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>` --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.o</span>` /lib/crtn.o`
