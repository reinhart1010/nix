---
layout: page
title: common/ppmflash (한국어)
description: "PPM 이미지 파일을 밝게 조정."
content_hash: 0984b9d1c3a53e2de1d0953512d0a79acc63a762
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmflash.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmflash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmflash

PPM 이미지 파일을 밝게 조정.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmflash.html>.

- 입력 PPM 이미지보다 `flashfactor` 배 밝은 출력 PPM 이미지 생성:

`ppmflash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">flashfactor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- 버전 표시:

`ppmflash -version`
