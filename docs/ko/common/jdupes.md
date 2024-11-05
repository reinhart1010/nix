---
layout: page
title: common/jdupes (한국어)
description: "강력한 중복 파일 찾기 도구이며, fdupes의 개선된 포크입니다."
content_hash: 2eac2258dc3129481f580707a9dd1248e28a640a
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jdupes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jdupes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jdupes

강력한 중복 파일 찾기 도구이며, fdupes의 개선된 포크입니다.
더 많은 정보: <https://codeberg.org/jbruchon/jdupes>.

- 단일 디렉터리 검색:

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 여러 디렉터리 검색:

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리2</span>

- 모든 디렉터리를 재귀적으로 검색:

`jdupes --recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 디렉터리를 재귀적으로 검색하고 사용자가 보관할 파일을 선택하도록 허용:

`jdupes --delete --recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 여러 디렉터리를 검색하고 디렉터리1이 아닌 디렉터리2의 하위 디렉터리를 따라가며 검색:

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리1</span>` --recurse: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리2</span>

- 여러 디렉터리를 검색하고 결과에서 디렉터리 순서를 유지:

`jdupes -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리3</span>
