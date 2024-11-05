---
layout: page
title: common/ppmtoyuvsplit (한국어)
description: "PPM 이미지를 세 개의 서브샘플링된 Abekas YUV 파일로 변환."
content_hash: f229d115119eda738277ff59c6e3569117d1371e
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtoyuvsplit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoyuvsplit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoyuvsplit

PPM 이미지를 세 개의 서브샘플링된 Abekas YUV 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoyuvsplit.html>.

- 입력 파일에서 PPM 이미지를 읽고, 이를 세 개의 서브샘플링된 Abekas YUV 이미지로 변환하여 지정된 기본 이름으로 시작하는 출력 파일들에 저장:

`ppmtoyuvsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>
