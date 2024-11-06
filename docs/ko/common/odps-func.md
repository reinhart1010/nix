---
layout: page
title: common/odps-func (한국어)
description: "ODPS (Open Data Processing Service)에서 함수 관리."
content_hash: 0d4baf45e034757aed28d405dd3c4ae1714083f2
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/odps-func.html
    icon: bi bi-globe
tldri18n_status: 2
---
# odps func

ODPS (Open Data Processing Service)에서 함수 관리.
같이 보기: `odps`.
더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 프로젝트의 함수 표시:

`list functions;`

- `.jar` 리소스를 사용하여 Java 함수 생성:

`create function `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_이름</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로.대상.패키지.Func</span>` using '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지.jar</span>`';`

- `.py` 리소스를 사용하여 Python 함수 생성:

`create function `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_이름</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.Func</span>` using '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.py</span>`';`

- 함수 삭제:

`drop function `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_이름</span>`;`
