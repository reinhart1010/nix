---
layout: page
title: common/pbmmask (한국어)
description: "일반 비트맵에서 마스크 비트맵 생성."
content_hash: 7fc0ec3e178ba6282574d636c16a1301666c10ae
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmmask.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmmask.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmmask

일반 비트맵에서 마스크 비트맵 생성.
같이 보기: `pambackground`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmmask.html>.

- 배경과 전경을 분리하여 마스크 비트맵 생성:

`pbmmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 생성된 마스크를 한 픽셀 확장:

`pbmmask -expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
