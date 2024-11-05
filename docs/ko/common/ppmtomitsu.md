---
layout: page
title: common/ppmtomitsu (한국어)
description: "PPM 이미지를 Mitsubishi S340-10 파일로 변환."
content_hash: 2953231217b21f7b2e9134d1be40db751978453d
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtomitsu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtomitsu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtomitsu

PPM 이미지를 Mitsubishi S340-10 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtomitsu.html>.

- PPM 이미지를 MITSU 파일로 변환:

`ppmtomitsu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mitsu</span>

- 이미지를 지정된 배율로 확대하고, 지정된 선명도를 사용하여 `n`개의 복사본 생성:

`ppmtomitsu -enlarge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` -sharpness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|4</span>` -copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mitsu</span>

- 인쇄 과정에 주어진 매체 사용:

`ppmtomitsu -media `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|A4|AS|A4S</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mitsu</span>
