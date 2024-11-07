---
layout: page
title: common/rdfind (한국어)
description: "중복된 내용을 가진 파일을 찾아 제거."
content_hash: 0abd4717c655f2871e7136413d526d42556dc068
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rdfind.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rdfind.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rdfind

중복된 내용을 가진 파일을 찾아 제거.
더 많은 정보: <https://rdfind.pauldreik.se>.

- 주어진 디렉터리에서 모든 중복 파일을 식별하고 요약 출력:

`rdfind -dryrun true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 중복 파일을 하드 링크로 교체:

`rdfind -makehardlinks true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 중복 파일을 심볼릭 링크/소프트 링크로 교체:

`rdfind -makesymlinks true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 중복 파일 삭제하고 빈 파일 무시 안 함:

`rdfind -deleteduplicates true -ignoreempty false `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
