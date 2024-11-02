---
layout: page
title: common/pbmtoxbm (한국어)
description: "PBM 이미지를 X11 또는 X10 비트맵으로 변환."
content_hash: 495c75eb9dd36a4290e4ea938dbe4b6b03d04e81
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtoxbm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pbmtoxbm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtoxbm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtoxbm

PBM 이미지를 X11 또는 X10 비트맵으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoxbm.html>.

- PBM 이미지를 X11 XBM 파일로 변환:

`pbmtoxbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xbm</span>

- X11 또는 X10 비트맵을 생성할지 명시적으로 지정:

`pbmtoxbm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11|x10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xbm</span>
