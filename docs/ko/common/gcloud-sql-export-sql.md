---
layout: page
title: common/gcloud-sql-export-sql (한국어)
description: "Cloud SQL 인스턴스에서 Google Cloud Storage의 SQL 파일로 데이터를 내보내기."
content_hash: 781a386b4d90d43abaa0354e5e021ec6aed385c2
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gcloud-sql-export-sql.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-sql-export-sql.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud sql export sql

Cloud SQL 인스턴스에서 Google Cloud Storage의 SQL 파일로 데이터를 내보내기.
백업 생성이나 데이터 마이그레이션에 유용합니다. 같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/sql/export/sql>.

- 특정 Cloud SQL 인스턴스에서 Google Cloud Storage 버킷으로 데이터를 SQL 덤프 파일로 내보내기:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>

- 비동기적으로 데이터를 내보내고, 작업 완료를 기다리지 않고 즉시 반환:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>` --async`

- Cloud SQL 인스턴스 내 특정 데이터베이스에서 데이터 내보내기:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>` --database=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스1,데이터베이스2,...</span>

- Cloud SQL 인스턴스 내의 지정된 데이터베이스에서 특정 테이블 내보내기:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>` --database=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>` --table=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블1,테이블2,...</span>

- 소스 인스턴스의 부담을 줄이기 위해 임시 인스턴스로 작업을 오프로드하여 데이터 내보내기:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>` --offload`

- 데이터를 내보내고 출력을 `gzip`으로 압축:

`gcloud sql export sql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>`.gz`
