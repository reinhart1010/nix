---
layout: page
title: common/ppmtoterm (한국어)
description: "PPM 이미지를 ANSI ISO 6429 ASCII 이미지로 변환."
content_hash: 78ff8b1eaa9d14535ef93801aabe794ec548f5ab
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtoterm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoterm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoterm

PPM 이미지를 ANSI ISO 6429 ASCII 이미지로 변환.
같이 보기: `ppmtoascii`, `pbmtoascii`, `pbmto4425`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoterm.html>.

- 각 픽셀을 개별 문자에 매핑하여 PPM 이미지를 ANSI ISO 6429 ASCII 이미지로 변환:

`ppmtoterm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.txt</span>
