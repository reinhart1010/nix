---
layout: page
title: common/ppmtopcx (한국어)
description: "PPM 이미지를 PCX 파일로 변환."
content_hash: 527927a27601eeed13275c340bb4b860d72ae76c
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtopcx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtopcx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtopcx

PPM 이미지를 PCX 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtopcx.html>.

- PPM 이미지를 PCX 파일로 변환:

`ppmtopcx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcx</span>

- 지정된 색상 깊이로 PCX 파일 생성:

`ppmtopcx -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8bit|24bit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcx</span>
