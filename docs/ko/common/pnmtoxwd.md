---
layout: page
title: common/pnmtoxwd (한국어)
description: "PNM 파일을 X11 윈도우 덤프 파일로 변환."
content_hash: 93075b601637fe6c43c93142e0b2cf1105974be1
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pnmtoxwd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmtoxwd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmtoxwd

PNM 파일을 X11 윈도우 덤프 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtoxwd.html>.

- PNM 이미지 파일을 XWD로 변환:

`pnmtoxwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xwd</span>

- DirectColor 형식으로 출력 생성:

`pnmtoxwd -directcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xwd</span>

- 출력의 색상 깊이를 b 비트로 설정:

`pnmtoxwd -pseudodepth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xwd</span>
