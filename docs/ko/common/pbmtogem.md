---
layout: page
title: common/pbmtogem (한국어)
description: "PBM 이미지를 입력으로 받아 압축된 GEM .img 파일로 출력."
content_hash: c53ffba7d7b3828ba5a249e39004790c25f6575c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtogem.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtogem.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtogem

PBM 이미지를 입력으로 받아 압축된 GEM .img 파일로 출력.
`pbmtogem`은 반복된 행을 압축할 수 없습니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtogem.html>.

- PBM 이미지를 GEM .img 파일로 변환:

`pbmtogem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.img</span>

- 모든 정보 메시지 억제:

`pbmtogem -quiet`

- 버전 표시:

`pbmtogem -version`
