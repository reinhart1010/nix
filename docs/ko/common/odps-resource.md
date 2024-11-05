---
layout: page
title: common/odps-resource (한국어)
description: "ODPS(Open Data Processing Service)에서 리소스를 관리."
content_hash: 8f553f8da0508d0ddbc698ae8bcd139c5415e474
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/odps-resource.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/odps-resource.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># odps resource

ODPS(Open Data Processing Service)에서 리소스를 관리.
같이 보기: `odps`.
더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 프로젝트의 리소스 표시:

`list resources;`

- 파일 리소스 추가:

`add file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭</span>`;`

- 아카이브 리소스 추가:

`add archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.gz</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭</span>`;`

- .jar 리소스 추가:

`add jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지.jar</span>`;`

- .py 리소스 추가:

`add py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.py</span>`;`

- 리소스 삭제:

`drop resource `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_이름</span>`;`
