---
layout: page
title: common/zsteg (한국어)
description: "PNG 및 BMP 파일 형식을 위한 스테가노그래피 탐지 도구."
content_hash: ae21c38390c4faa8c91c472fd92c236051d24c20
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zsteg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zsteg

PNG 및 BMP 파일 형식을 위한 스테가노그래피 탐지 도구.
LSB 스테가노그래피, ZLIB 압축 데이터, OpenStego, Camouflage 및 에라토스테네스 집합의 LSB를 탐지합니다.
더 많은 정보: <https://github.com/zed-0xff/zsteg>.

- PNG에서 포함된 데이터 탐지:

`zsteg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- BMP 이미지에서 알려진 모든 방법을 사용하여 포함된 데이터 탐지:

`zsteg --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.bmp</span>

- PNG에서 포함된 데이터 탐지, 픽셀을 수직으로 반복하고 MSB 우선 사용:

`zsteg --msb --order yx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- BMP 이미지에서 포함된 데이터 탐지, 고려할 비트 지정:

`zsteg --bits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2,3|1-3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.bmp</span>

- PNG에서 포함된 데이터 탐지, 소수 픽셀만 추출하고 비트 반전:

`zsteg --prime --invert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- BMP 이미지에서 포함된 데이터 탐지, 찾을 문자열의 최소 길이와 찾기 모드 지정:

`zsteg --min-str-len `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first|all|longest|none</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.bmp</span>
