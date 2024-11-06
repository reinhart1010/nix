---
layout: page
title: common/ogr2ogr (한국어)
description: "지리공간 벡터 데이터를 파일 형식 간에 변환."
content_hash: 6bf5867022a48b4ff08ea99a5f1704ddb55dded4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ogr2ogr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ogr2ogr

지리공간 벡터 데이터를 파일 형식 간에 변환.
더 많은 정보: <https://gdal.org/programs/ogr2ogr.html>.

- 쉐이프파일을 지오패키지로 변환:

`ogr2ogr -f GPKG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.shp</span>

- 조건에 맞는 특징만 포함하도록 GeoJSON 축소:

`ogr2ogr -where '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myProperty > 42</span>`' -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GeoJSON</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.geojson</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.geojson</span>

- 지오패키지의 좌표 참조 시스템을 `EPSG:4326`에서 `EPSG:3857`로 변경:

`ogr2ogr -s_srs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EPSG:4326</span>` -t_srs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EPSG:3857</span>` -f GPKG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>

- CSV 파일을 지오패키지로 변환하며 좌표 열의 이름을 지정하고 좌표 참조 시스템 할당:

`ogr2ogr -f GPKG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.csv</span>` -oo X_POSSIBLE_NAMES=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경도</span>` -oo Y_POSSIBLE_NAMES=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위도</span>` -a_srs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EPSG:4326</span>

- 지오패키지를 PostGIS 데이터베이스로 로드:

`ogr2ogr -f PostgreSQL PG:dbname="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>

- 주어진 경계 상자로 지오패키지 파일의 레이어를 자르기:

`ogr2ogr -spat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최소_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최소_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_y</span>` -f GPKG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.gpkg</span>
