---
layout: page
title: common/ppmtobmp (한국어)
description: "PPM 이미지를 BMP 파일로 변환."
content_hash: f105493e8c2755c31a169716827980f3490c8aca
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtobmp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtobmp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtobmp

PPM 이미지를 BMP 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtobmp.html>.

- PPM 이미지를 BMP 파일로 변환:

`ppmtobmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bmp</span>

- Windows BMP 파일 또는 OS/2 BMP 파일을 생성할지 여부를 명시적으로 지정:

`ppmtobmp -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|os2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bmp</span>

- 각 픽셀에 사용할 비트 수를 지정:

`ppmtobmp -bbp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|4|8|24</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bmp</span>
