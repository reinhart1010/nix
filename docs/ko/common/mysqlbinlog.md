---
layout: page
title: common/mysqlbinlog (한국어)
description: "MySQL 바이너리 로그 파일을 처리하는 도구."
content_hash: 5415f37b182c93293135ffbcb2cd65c1167291b6
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/mysqlbinlog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mysqlbinlog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mysqlbinlog

MySQL 바이너리 로그 파일을 처리하는 도구.
더 많은 정보: <https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html>.

- 특정 바이너리 로그 파일에서 이벤트 표시:

`mysqlbinlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바인로그</span>

- 특정 데이터베이스에 대한 바이너리 로그의 항목 표시:

`mysqlbinlog --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바인로그</span>

- 특정 날짜 사이의 바이너리 로그에서 이벤트 표시:

`mysqlbinlog --start-datetime='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2022-01-01 01:00:00</span>`' --stop-datetime='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2022-02-01 01:00:00</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바인로그</span>

- 특정 위치 사이의 바이너리 로그에서 이벤트 표시:

`mysqlbinlog --start-position=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --stop-position=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바인로그</span>

- 지정된 호스트의 MySQL 서버에서 바이너리 로그 표시:

`mysqlbinlog --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바인로그</span>
