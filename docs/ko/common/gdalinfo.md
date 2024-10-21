---
layout: page
title: common/gdalinfo (한국어)
description: "GDAL 지원 래스터 데이터세트에 대한 다양한 정보를 나열."
content_hash: c206be9833b39602bda52aa689825f43e9e96d46
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gdalinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdalinfo

GDAL 지원 래스터 데이터세트에 대한 다양한 정보를 나열.
더 많은 정보: <https://gdal.org/programs/gdalinfo.html>.

- 지원하는 래스터 포맷 나열:

`gdalinfo --formats`

- 특정 래스터 데이터세트에 대한 정보 나열:

`gdalinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>

- 특정 래스터 데이터세트에 대한 정보를 JSON 형식으로 나열:

`gdalinfo -json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>

- 특정 래스터 데이터세트의 히스토그램 값 표시:

`gdalinfo -hist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>

- 웹 맵 서비스(WMS)에 대한 정보를 나열:

`gdalinfo WMS:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://services.meggsimum.de/geoserver/ows</span>

- 웹 맵 서비스(WMS)의 특정 데이터세트에 대한 정보를 나열:

`gdalinfo WMS:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://services.meggsimum.de/geoserver/ows</span>` -sd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
