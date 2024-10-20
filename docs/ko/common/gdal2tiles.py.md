---
layout: page
title: common/gdal2tiles.py (한국어)
description: "래스터 데이터세트를 위한 TMS 또는 XYZ 타일을 생성."
content_hash: 16868bd2380c05f726baea2173472d6471937a12
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gdal2tiles.py.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gdal2tiles.py.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gdal2tiles.py

래스터 데이터세트를 위한 TMS 또는 XYZ 타일을 생성.
더 많은 정보: <https://gdal.org/programs/gdal2tiles.html>.

- 래스터 데이터세트의 확대/축소 수준 2~5에 대한 TMS 타일을 생성:

`gdal2tiles.py --zoom 2-5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_디렉토리</span>

- 래스터 데이터세트의 확대/축소 수준 2~5에 대한 XYZ 타일을 생성:

`gdal2tiles.py --zoom 2-5 --xyz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_디렉토리</span>
