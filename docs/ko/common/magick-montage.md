---
layout: page
title: common/magick-montage (한국어)
description: "이미지를 사용자 지정 가능한 그리드로 배열."
content_hash: 8855d2290483a756898e79739420b9eba0faca20
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/magick-montage.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-montage.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/magick-montage.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># magick montage

이미지를 사용자 지정 가능한 그리드로 배열.
같이 보기: `magick`.
더 많은 정보: <https://imagemagick.org/script/montage.php>.

- 이미지를 그리드로 배열하고, 그리드 셀 크기보다 큰 이미지를 자동으로 크기 조정:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/몽타주.jpg</span>

- 가장 큰 이미지로부터 그리드 셀 크기를 자동 계산하여 이미지를 그리드로 배열:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/몽타주.jpg</span>

- 그리드 셀 크기를 지정하고, 타일링 전에 이미지를 해당 크기에 맞게 조정:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/몽타주.jpg</span>

- 그리드의 행과 열 수를 제한하여 입력 이미지가 여러 출력 몽타주로 넘치도록 설정:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` -tile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2x3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">몽타주_%d.jpg</span>

- 타일링 전에 이미지를 그리드 셀에 맞게 크기 조정 및 자르기:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480^</span>` -gravity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">center</span>` -crop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/몽타주.jpg</span>
