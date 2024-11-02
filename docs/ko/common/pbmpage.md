---
layout: page
title: common/pbmpage (한국어)
description: "인쇄를 위한 테스트 패턴 생성."
content_hash: 7b2db3360409d06580fa47b6365ffd867ed5dc9f
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmpage.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmpage.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmpage

인쇄를 위한 테스트 패턴 생성.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmpage.html>.

- US 표준 용지에 인쇄할 테스트 패턴 생성:

`pbmpage > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pbm</span>

- A4 용지에 인쇄할 테스트 패턴 생성:

`pbmpage -a4 > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pbm</span>

- 사용할 패턴 지정:

`pbmpage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pbm</span>
