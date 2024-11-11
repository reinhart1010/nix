---
layout: page
title: linux/size (한국어)
description: "바이너리 파일 내부 섹션의 크기를 표시합니다."
content_hash: 69f2dabb07555cc657eb1fa181123b8fd00e3d28
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/size.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/size.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># size

바이너리 파일 내부 섹션의 크기를 표시합니다.
더 많은 정보: <https://sourceware.org/binutils/docs/binutils/size.html>.

- 주어진 오브젝트 또는 실행 파일의 섹션 크기 표시:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 오브젝트 또는 실행 파일의 섹션 크기를 [o]팔진수로 표시:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--radix=8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 오브젝트 또는 실행 파일의 섹션 크기를 [d]십진수로 표시:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--radix=10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 오브젝트 또는 실행 파일의 섹션 크기를 [x]십육진수로 표시:

`size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--radix=16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
