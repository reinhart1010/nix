---
layout: page
title: common/magick-mogrify (한국어)
description: "여러 이미지에 대한 크기 조정, 자르기, 뒤집기, 효과 추가와 같은 작업 수행."
content_hash: 72a9a87b53cabdf5bf82bfe497a81f4e4ad4a4ba
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/magick-mogrify.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-mogrify.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># magick mogrify

여러 이미지에 대한 크기 조정, 자르기, 뒤집기, 효과 추가와 같은 작업 수행.
변경 사항은 원본 파일에 직접 적용됩니다.
같이 보기: `magick`.
더 많은 정보: <https://imagemagick.org/script/mogrify.php>.

- 디렉토리 내 모든 JPEG 이미지를 원래 크기의 50%로 조정:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- `DSC`로 시작하는 모든 이미지를 800x600으로 조정:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DSC*</span>

- 디렉토리 내 모든 PNG를 JPEG로 변환:

`magick mogrify -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- 현재 디렉토리의 모든 이미지 파일의 채도를 절반으로 줄이기:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100,50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 현재 디렉토리의 모든 이미지 파일의 밝기를 두 배로 증가:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>
