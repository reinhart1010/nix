---
layout: page
title: common/fdupes (한국어)
description: "일련의 디렉터리에서 중복 파일을 찾음."
content_hash: a01e019575bd0b78188b4bd99d7a668c1671db85
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fdupes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fdupes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fdupes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fdupes

일련의 디렉터리에서 중복 파일을 찾음.
더 많은 정보: <https://github.com/adrianlopezroche/fdupes>.

- 단일 디렉터리 검색:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 여러 디렉터리 검색:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리2</span>

- 재귀적으로 디렉터리를 검색:

`fdupes -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 여러 디렉터리를 하나의 재귀적으로 검색:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리1</span>` -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉터리2</span>

- 하드링크를 중복으로 간주하여 재귀적으로 검색:

`fdupes -rH `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 반복적으로 중복 항목을 검색하고 유지할 항목을 선택하고, 나머지 항목을 삭제하는 것:

`fdupes -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 메시지를 표시하지 않고 반복적으로 검색하고 중복 항목을 삭제:

`fdupes -rdN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
