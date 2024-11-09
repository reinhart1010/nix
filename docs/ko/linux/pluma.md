---
layout: page
title: linux/pluma (한국어)
description: "MATE 데스크탑 환경에서 파일 편집."
content_hash: ba5d9bcc75ca3bfd7f3c063f773413d18816ee0e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pluma.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pluma.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pluma

MATE 데스크탑 환경에서 파일 편집.
더 많은 정보: <https://manned.org/pluma>.

- 편집기 시작:

`pluma`

- 특정 문서 열기:

`pluma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 인코딩을 사용하여 문서 열기:

`pluma --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">WINDOWS-1252</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 지원되는 모든 인코딩 출력:

`pluma --list-encodings`

- 특정 줄로 이동하여 문서 열기:

`pluma +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
