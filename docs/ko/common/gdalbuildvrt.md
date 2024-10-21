---
layout: page
title: common/gdalbuildvrt (한국어)
description: "기존 데이터세트 목록에서 가상 데이터 세트를 구축."
content_hash: 08788e2d27e16b532a80f652b0ca6ffd0216338c
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gdalbuildvrt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdalbuildvrt

기존 데이터세트 목록에서 가상 데이터 세트를 구축.
더 많은 정보: <https://gdal.org/programs/gdalbuildvrt.html>.

- 디렉토리에 포함된 모든 TIFF 파일로 가상 모자이크를 생성:

`gdalbuildvrt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_디렉토리/*.tif</span>

- 텍스트 파일에 이름이 지정된 파일로 가상 모자이크를 만듬 :

`gdalbuildvrt -input_file_list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목록.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.vrt</span>

- 3개의 단일 대역 입력 파일에서 RGB 가상 모자이크를 만듬:

`gdalbuildvrt -separate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/rgb.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빨강.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/초록.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파랑.tif</span>

- 파란색 배경색 (RGB: 0 0 255)으로 가상 모자이크 만들기:

`gdalbuildvrt -hidenodata -vrtnodata "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0 0 255</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_디렉토리/*.tif</span>
