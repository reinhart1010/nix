---
layout: page
title: common/pbmtomacp (한국어)
description: "PBM 이미지를 MacPaint 파일로 변환."
content_hash: 5cf6c28d8ff60d63166230ec42e2f90791f2775d
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtomacp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtomacp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtomacp

PBM 이미지를 MacPaint 파일로 변환.
같이 보기: `macptopbm`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtomacp.html>.

- PBM 이미지를 MACP 파일로 변환:

`pbmtomacp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.macp</span>

- 출력 파일을 압축하지 않음:

`pbmtomacp -norle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.macp</span>
