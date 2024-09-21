---
layout: page
title: common/bq (한국어)
description: "Google Cloud의 완전 관리형 서버리스 엔터프라이즈 데이터 웨어하우스인 BigQuery용 Python 기반 도구."
content_hash: 8f0cd96e68c32787ed9d05fff7eecc8e1f1d0e76
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bq

Google Cloud의 완전 관리형 서버리스 엔터프라이즈 데이터 웨어하우스인 BigQuery용 Python 기반 도구.
더 많은 정보: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- 표준 SQL을 사용하여 BigQuery 테이블에 대해 쿼리를 실행하고, `--dry_run` 플래그를 추가해 쿼리에서 읽은 바이트 수를 추정:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터셋_이름</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>`'`

- 매개변수화된 쿼리 실행:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- 미국 위치에 새 데이터 세트 또는 테이블을 만듬:

`bq mk --location=US `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dataset_name</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>

- 프로젝트의 모든 데이터세트를 나열:

`bq ls --filter labels.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` --max_results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정수</span>` --format=prettyjson --project_id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_아이디</span>

- CSV, JSON, Parquet, Avro 등의 형식으로 특정 파일의 데이터를 테이블에 일괄 로드:

`bq load --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치</span>` --source_format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CSV|JSON|PARQUET|AVRO</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터셋</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로_대상_소스</span>

- 한 테이블을 다른 테이블에 복사:

`bq cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터셋</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오래된_테이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터셋</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_테이블</span>

- 버전 정보 표시:

`bq help`
