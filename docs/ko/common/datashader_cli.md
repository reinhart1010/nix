---
layout: page
title: common/datashader_cli (한국어)
description: "Datashader 기반의 CLI을 사용하여 대규모 데이터 세트를 빠르게 시각화."
content_hash: bd4ab39c501f9d8db3d49803a47fa0f8a75b5468
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/datashader_cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/datashader_cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># datashader_cli

Datashader 기반의 CLI을 사용하여 대규모 데이터 세트를 빠르게 시각화.
더 많은 정보: <https://github.com/wybert/datashader-cli>.

- 점의 음영처리된 산점도를 생성하고 PNG 파일로 저장한 후 배경색을 설정:

`datashader_cli points `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.parquet</span>` --x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pickup_x</span>` --y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pickup_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>` --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|white|#rrggbb</span>

- 지리공간 데이터 시각화 (Geoparquet, shapefile, geojson, geopackage 등 지원):

`datashader_cli points `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_데이터.geo.parquet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_데이터.png</span>` --geo true`

- matplotlib를 사용해 이미지 렌더링:

`datashader_cli points `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_데이터.geo.parquet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_데이터.png</span>` --geo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` --matplotlib true`
