---
layout: page
title: linux/xcursorgen (한국어)
description: "PNG 모음에서 X 커서 파일 생성."
content_hash: 8c9042ae943e34aaa063a857b21bf65426984c4f
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xcursorgen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xcursorgen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xcursorgen

PNG 모음에서 X 커서 파일 생성.
`--prefix`가 생략되면 이미지 파일은 현재 작업 디렉터리에 위치해야 합니다.
더 많은 정보: <https://manned.org/xcursorgen>.

- 구성 파일을 사용하여 X 커서 파일 생성:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 구성 파일을 사용하여 X 커서 파일을 만들고 이미지 파일의 경로 지정:

`xcursorgen --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_디렉터리/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 구성 파일을 사용하여 X 커서 파일을 만들고 출력을 `stdout`에 쓰기:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.cursor</span>
