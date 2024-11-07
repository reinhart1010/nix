---
layout: page
title: common/readlink (한국어)
description: "심볼릭 링크를 따라가고 심볼릭 링크 정보를 가져옵니다."
content_hash: 4311a0bbbccecdfe8d04396fcc54c3d9f4a1992b
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/readlink.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/readlink.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/readlink.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/readlink.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># readlink

심볼릭 링크를 따라가고 심볼릭 링크 정보를 가져옵니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/readlink>.

- 심볼릭 링크가 가리키는 실제 파일을 가져오기:

`readlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 절대 경로 가져오기:

`readlink -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
