---
layout: page
title: common/gdaldem (한국어)
description: "디지털 표고 모델 (DEM)을 분석하고 시각화."
content_hash: 153ff68692016a87f4e3ed70013cb5823b781850
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gdaldem.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gdaldem.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gdaldem

디지털 표고 모델 (DEM)을 분석하고 시각화.
더 많은 정보: <https://gdal.org/programs/gdaldem.html>.

- DEM의 음영기복도를 계산:

`gdaldem hillshade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.tif</span>

- DEM의 기울기를 계산:

`gdaldem slope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.tif</span>

- DEM의 측면을 계산:

`gdaldem aspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.tif</span>
