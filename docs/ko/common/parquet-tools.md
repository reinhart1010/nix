---
layout: page
title: common/parquet-tools (한국어)
description: "Parquet 파일을 표시하고 검사하며 조작."
content_hash: 46a4dc677e89983d4e5358d13b19c70c636ffe4c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/parquet-tools.html
    icon: bi bi-globe
tldri18n_status: 2
---
# parquet-tools

Parquet 파일을 표시하고 검사하며 조작.
더 많은 정보: <https://github.com/apache/parquet-mr>.

- Parquet 파일 내용 표시:

`parquet-tools cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet</span>

- Parquet 파일의 처음 몇 줄 표시:

`parquet-tools head `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet</span>

- Parquet 파일의 스키마 출력:

`parquet-tools schema `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet</span>

- Parquet 파일의 메타데이터 출력:

`parquet-tools meta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet</span>

- Parquet 파일의 내용과 메타데이터 출력:

`parquet-tools dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet</span>

- 여러 Parquet 파일을 하나의 대상 파일로 병합:

`parquet-tools merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_parquet</span>

- Parquet 파일의 행 수 출력:

`parquet-tools rowcount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet</span>

- Parquet 파일의 열 및 오프셋 색인 출력:

`parquet-tools column-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/parquet</span>
