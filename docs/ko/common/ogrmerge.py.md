---
layout: page
title: common/ogrmerge.py (한국어)
description: "여러 벡터 데이터셋을 하나로 병합."
content_hash: 3a8f4464e1c46106778afd4121c2377eff83360c
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ogrmerge.py.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ogrmerge.py

여러 벡터 데이터셋을 하나로 병합.
더 많은 정보: <https://gdal.org/programs/ogrmerge.html>.

- 각 입력 셰이프파일에 대해 레이어가 포함된 GeoPackage 생성:

`ogrmerge.py -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPKG</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.shp 경로/대상/입력2.shp ...</span>

- 각 입력 GeoJSON에 대해 레이어가 포함된 가상 데이터 소스(VRT) 생성:

`ogrmerge.py -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VRT</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.geojson 경로/대상/입력2.geojson ...</span>

- 두 벡터 데이터셋을 연결하고 속성 'source_name'에 데이터셋의 소스 이름 저장:

`ogrmerge.py -single -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GeoJSON</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.geojson</span>` -src_layer_field_name country `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.shp 경로/대상/입력2.shp ...</span>
