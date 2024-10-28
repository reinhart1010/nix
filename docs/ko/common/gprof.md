---
layout: page
title: common/gprof (한국어)
description: "다양한 프로그래밍 언어에 대한 성능 분석 도구."
content_hash: bce909b2a9d6f99db1359fbe7549ed603e8d5358
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/gprof.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gprof.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gprof

다양한 프로그래밍 언어에 대한 성능 분석 도구.
프로그램의 기능 실행을 프로파일링.
더 많은 정보: <https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html>.

- gprof 정보로 바이너리를 컴파일하고 실행하여 `gmon.out`을 얻음:

`gcc -pg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program.c</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./a.out</span>

- gprof를 실행하여 프로필 출력을 얻음:

`gprof`

- 프로필 필드의 설명을 제거:

`gprof -b`

- 사용량이 전혀 없는 루틴을 보여줌:

`gprof -bz`
