---
layout: page
title: common/magick-convert (한국어)
description: "이미지 형식 간 변환, 크기 조정, 병합, 생성 등을 수행."
content_hash: 920adbfac6b64f4cc737bff7f85574364a00c5bc
last_modified_at: 2024-10-14
related_topics:
  - title: Deutsch version
    url: /de/common/magick-convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/magick-convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/magick-convert.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/magick-convert.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># magick convert

이미지 형식 간 변환, 크기 조정, 병합, 생성 등을 수행.
참고: 이 도구는 이전의 `convert`로, ImageMagick 7+에서 `magick`으로 대체되었습니다.
더 많은 정보: <https://imagemagick.org/script/convert.php>.

- 이미지를 JPEG에서 PNG로 변환:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.png</span>

- 이미지를 원래 크기의 50%로 조정:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.png</span>

- 이미지의 원본 비율을 유지하며 최대 크기가 640x480이 되도록 축소:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.png</span>

- 지정된 파일 크기를 가지도록 이미지 크기 조정:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.png</span>` -define jpeg:extent=512kb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.jpg</span>

- 이미지를 수직/수평으로 결합:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.png 경로/대상/이미지2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-append|+append</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.png</span>

- 100ms 간격의 이미지 시리즈로 GIF 생성:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.png 경로/대상/이미지2.png ...</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/애니메이션.gif</span>

- 단색 빨간색 배경만 있는 이미지 생성:

`magick convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- 여러 크기의 이미지를 사용하여 파비콘 생성:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.png 경로/대상/이미지2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/favicon.ico</span>
