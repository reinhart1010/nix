---
layout: page
title: common/tbl (한국어)
description: "groff (GNU Troff) 문서 형식 시스템을 위한 테이블 전처리기."
content_hash: 2d92b66be357f04e8b60610ea275047345a37528
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tbl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tbl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tbl

groff (GNU Troff) 문서 형식 시스템을 위한 테이블 전처리기.
같이 보기: `groff`, `troff`.
더 많은 정보: <https://manned.org/tbl>.

- 입력에 포함된 테이블을 처리하여, 후에 groff로 PostScript 형식으로 조판할 수 있도록 출력 저장:

`tbl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.roff</span>

- [me] 매크로 패키지를 사용하여 테이블이 있는 입력을 PDF로 조판:

`tbl -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tbl</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>
