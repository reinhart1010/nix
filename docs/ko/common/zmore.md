---
layout: page
title: common/zmore (한국어)
description: "`gzip`으로 압축된 파일을 `more`로 보기."
content_hash: 10ac43861bc04ad29eca5254ff6ea00ab41f0ac9
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zmore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zmore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zmore

`gzip`으로 압축된 파일을 `more`로 보기.
더 많은 정보: <https://manned.org/zmore>.

- 압축된 파일 열기:

`zmore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt.gz</span>

- 파일의 다음 페이지 표시:

`<Space>`

- 파일에서 패턴 검색 (`n`을 눌러 다음 일치 항목으로 이동):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 종료:

`q`

- 상호작용 명령 도움말 표시:

`h`
