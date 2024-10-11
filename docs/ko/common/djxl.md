---
layout: page
title: common/djxl (한국어)
description: "JPEG XL 이미지의 압축을 해제."
content_hash: 3a71d6ca8327178996a3519f3cacc36e9cd3b468
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/djxl.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/djxl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/djxl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># djxl

JPEG XL 이미지의 압축을 해제.
허용되는 출력 확장자는 PNG, APNG, JPEG, EXR, PGM, PPM, PNM, PFM, PAM, EXIF, XMP 및 JUMBF.
더 많은 정보: <https://github.com/libjxl/libjxl>.

- JPEG XL 이미지를 다른 형식으로 압축 해제:

`djxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jxl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ext</span>

- 매우 상세한 도움말 페이지를 표시:

`djxl --help --verbose --verbose --verbose --verbose`
