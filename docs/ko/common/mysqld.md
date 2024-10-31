---
layout: page
title: common/mysqld (한국어)
description: "MySQL 데이터베이스 서버 시작."
content_hash: 12ab9d47e34d874b7b6137255d9f818a5ee9d60d
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/mysqld.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mysqld.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mysqld

MySQL 데이터베이스 서버 시작.
더 많은 정보: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

- MySQL 데이터베이스 서버 시작:

`mysqld`

- 서버 시작 및 오류 메시지를 콘솔에 출력:

`mysqld --console`

- 서버 시작 및 로그 출력을 사용자 지정 로그 파일에 저장:

`mysqld --log=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.log</span>

- 기본 인자와 그 값을 출력하고 종료:

`mysqld --print-defaults`

- 파일에서 인자와 값을 읽어 서버 시작:

`mysqld --defaults-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자 지정 포트에서 서버 시작:

`mysqld --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 도움말 표시:

`mysqld --verbose --help`
