---
layout: page
title: common/lz4 (한국어)
description: ".lz4 파일을 압축하거나 압축 해제합니다."
content_hash: 5f222959f97ec562cea696137e3dc86225896e84
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lz4.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lz4.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lz4

.lz4 파일을 압축하거나 압축 해제합니다.
더 많은 정보: <https://github.com/lz4/lz4>.

- 파일 압축:

`lz4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 압축 해제:

`lz4 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.lz4</span>

- 파일 압축 해제 후 `stdout`에 출력:

`lz4 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.lz4</span>

- 디렉토리 및 그 내용 패키징 및 압축:

`tar cvf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` | lz4 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리.tar.lz4</span>

- 디렉토리 및 그 내용 압축 해제 및 풀기:

`lz4 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리.tar.lz4</span>` | tar -xv`

- 최고 압축률로 파일 압축:

`lz4 -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
