---
layout: page
title: common/stat (한국어)
description: "파일 및 파일 시스템 정보를 표시."
content_hash: 4fa9e73099cf92105b0d361d5c11edfd7a97a08b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/stat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/stat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># stat

파일 및 파일 시스템 정보를 표시.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- 특정 파일에 대한 속성(크기, 권한, 생성 및 액세스 날짜 등) 표시:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 레이블 없이 특정 파일에 대한 속성(크기, 권한, 생성 및 액세스 날짜 등) 표시:

`stat --terse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일이 있는 파일 시스템에 대한 정보 표시:

`stat --file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 8진수 파일 권한만 표시:

`stat --format="%a %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일의 소유자 및 그룹 표시:

`stat --format="%U %G" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일의 크기를 바이트 단위로 표시:

`stat --format="%s %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
