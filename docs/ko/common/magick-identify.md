---
layout: page
title: common/magick-identify (한국어)
description: "이미지 파일의 형식과 특성을 설명합니다."
content_hash: 2b5a33fb09ca94e5c118d7f81cba396110ca343b
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/magick-identify.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-identify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick identify

이미지 파일의 형식과 특성을 설명합니다.
같이 보기: `magick`.
더 많은 정보: <https://imagemagick.org/script/identify.php>.

- 이미지의 형식과 기본 특성 설명:

`magick identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 이미지의 형식과 자세한 특성 설명:

`magick identify -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 현재 디렉토리의 모든 JPEG 파일의 크기를 수집하여 CSV 파일에 저장:

`magick identify -format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%f,%w,%h\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일목록.csv</span>
