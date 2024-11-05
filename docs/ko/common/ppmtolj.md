---
layout: page
title: common/ppmtolj (한국어)
description: "PPM 파일을 HP LaserJet PCL 5 Color 파일로 변환."
content_hash: 99cf8b1f3c455c96dde53dfd51628b7fbbd8d737
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtolj.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtolj.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtolj

PPM 파일을 HP LaserJet PCL 5 Color 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtolj.html>.

- PPM 파일을 HP LaserJet PCL 5 Color 파일로 변환:

`ppmtolj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.lj</span>

- 지정된 감마 값을 사용하여 감마 보정 적용:

`ppmtolj -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">감마</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.lj</span>

- 필요한 해상도 지정:

`ppmtolj -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75|100|150|300|600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.lj</span>
