---
layout: page
title: common/ogrinfo (한국어)
description: "OGR 지원 데이터 소스에 대한 정보를 나열합니다."
content_hash: 42d9867eba4eb15e5b3bbcc9b6330f2b63072f0e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ogrinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ogrinfo

OGR 지원 데이터 소스에 대한 정보를 나열합니다.
더 많은 정보: <https://gdal.org/programs/ogrinfo.html>.

- 지원되는 형식 나열:

`ogrinfo --formats`

- 데이터 소스의 레이어 나열:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>

- 데이터 소스의 특정 레이어에 대한 자세한 정보 얻기:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이어_이름</span>

- 데이터 소스의 특정 레이어에 대한 요약 정보 표시:

`ogrinfo -so `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이어_이름</span>

- 데이터 소스의 모든 레이어 요약 정보 표시:

`ogrinfo -so -al `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>

- 조건에 맞는 피처의 자세한 정보 표시:

`ogrinfo -where '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름 > 42</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이어_이름</span>

- SQL을 사용하여 데이터 소스의 레이어 업데이트:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.geojson</span>` -dialect SQLite -sql "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UPDATE input SET attribute_name = 'foo'</span>`"`
