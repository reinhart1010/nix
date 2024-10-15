---
layout: page
title: common/magick-compare (한국어)
description: "두 이미지 간의 차이를 시각적으로 주석 처리하기 위한 비교 이미지를 생성."
content_hash: 9d87939d6096e6df770adaed0e3e5669f038a9fc
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/common/magick-compare.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-compare.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/magick-compare.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/magick-compare.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-compare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick compare

두 이미지 간의 차이를 시각적으로 주석 처리하기 위한 비교 이미지를 생성.
같이 보기: `magick`.
더 많은 정보: <https://imagemagick.org/script/compare.php>.

- 두 이미지 비교:

`magick compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/diff.png</span>

- 지정된 측정 기준을 사용하여 두 이미지 비교:

`magick compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/diff.png</span>
