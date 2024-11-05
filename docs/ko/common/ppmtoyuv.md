---
layout: page
title: common/ppmtoyuv (한국어)
description: "PPM 이미지를 Abekas YUV 파일로 변환."
content_hash: ffd74dd070f30770aee445ae216b48c2a6c81adc
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtoyuv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoyuv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoyuv

PPM 이미지를 Abekas YUV 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoyuv.html>.

- 입력 파일에서 PPM 이미지를 읽고, Abekas YUV 이미지로 변환하여 지정된 출력 파일에 저장:

`ppmtoyuv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.yuv</span>
