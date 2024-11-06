---
layout: page
title: common/osmium (한국어)
description: "OpenStreetMap (OSM) 파일을 처리하는 다목적 도구."
content_hash: fc6c4e8c5d3376d2725099052cfb8991fe423fd1
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/osmium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# osmium

OpenStreetMap (OSM) 파일을 처리하는 다목적 도구.
더 많은 정보: <https://osmcode.org/osmium-tool/manual>.

- 파일 정보 표시:

`osmium fileinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.osm</span>

- 내용 표시:

`osmium show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.osm</span>

- 파일 형식을 PBF에서 XML로 변환:

`osmium cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.osm.pbf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.osm</span>

- 주어진 경계 상자에 의해 지리적 영역 추출:

`osmium extract -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최소_경도</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최소_위도</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_경도</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_위도</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbf</span>

- GeoJSON 파일에 의해 지리적 영역 추출:

`osmium extract -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다각형.geojson</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbf</span>

- "restaurant"으로 태그된 모든 객체 필터링:

`osmium tags-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbf</span>` amenity=restaurant -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbf</span>

- "highway"로 태그된 "way" 객체 필터링:

`osmium tags-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbf</span>` w/highway -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbf</span>

- "building"으로 태그된 "way" 및 "relation" 객체 필터링:

`osmium tags-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pbf</span>` wr/building -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbf</span>
