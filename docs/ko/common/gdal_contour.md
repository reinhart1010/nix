---
layout: page
title: common/gdal_contour (한국어)
description: "디지털 표고 모델에서 등고선과 다각형을 생성."
content_hash: 49fdb472b119070a673200fcb704ba8716098dbf
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gdal_contour.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gdal_contour.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gdal_contour

디지털 표고 모델에서 등고선과 다각형을 생성.
더 많은 정보: <https://gdal.org/programs/gdal_contour.html>.

- 고도 속성([a]ttributing)을 "ele"로 지정하면서 100미터 간격([i]nterval)에 걸쳐 등고선이 퍼져있는 벡터 데이터세트를 생성:

`gdal_contour -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ele</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gpkg</span>

- 100미터 간격([i]nterval)에 걸쳐 분산된 다각형([p]olygons)으로 벡터 데이터세트를 생성:

`gdal_contour -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100.0</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gpkg</span>
