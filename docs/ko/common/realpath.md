---
layout: page
title: common/realpath (한국어)
description: "파일이나 디렉터리에 대한 절대 경로를 표시."
content_hash: bd03b19d28ebec168ec66c40279fbf94600e243f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/realpath.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/realpath.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/realpath.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># realpath

파일이나 디렉터리에 대한 절대 경로를 표시.
더 많은 정보: <https://www.gnu.org/software/coreutils/realpath>.

- 파일이나 디렉터리에 대한 절대 경로 표시:

`realpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 모든 경로 구성 요소가 존재해야 함:

`realpath --canonicalize-existing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 심볼릭 링크 전에 ".." 구성 요소 해결:

`realpath --logical `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 심볼릭 링크 확장 비활성화:

`realpath --no-symlinks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 오류 메시지 억제:

`realpath --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
