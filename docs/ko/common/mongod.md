---
layout: page
title: common/mongod (한국어)
description: "MongoDB 데이터베이스 서버."
content_hash: 0641b182209b51c8fea13acedbfd7ccf2b858d6f
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/mongod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mongod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mongod.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mongod.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mongod

MongoDB 데이터베이스 서버.
더 많은 정보: <https://docs.mongodb.com/manual/reference/program/mongod>.

- 저장 디렉터리 지정 (기본값: Linux 및 macOS는 `/data/db`, Windows는 `C:\data\db`):

`mongod --dbpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 설정 파일 지정:

`mongod --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 청취할 포트 지정 (기본값: 27017):

`mongod --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 데이터베이스 프로파일링 수준 지정. 0은 꺼짐, 1은 느린 작업만, 2는 모든 작업 (기본값: 0):

`mongod --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2</span>
