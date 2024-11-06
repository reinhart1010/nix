---
layout: page
title: common/odps-auth (한국어)
description: "ODPS (Open Data Processing Service)에서 사용자 권한 관리."
content_hash: 9c1edd385a99fcafe12aa6e869b721f92669807c
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/odps-auth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# odps auth

ODPS (Open Data Processing Service)에서 사용자 권한 관리.
같이 보기: `odps`.
더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 프로젝트에 사용자 추가:

`add user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`;`

- 사용자에게 권한 집합 부여:

`grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_목록</span>` on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_이름</span>` to user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`;`

- 사용자의 권한 보기:

`show grants for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`;`

- 사용자 역할 생성:

`create role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>`;`

- 역할에 권한 집합 부여:

`grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_목록</span>` on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_이름</span>` to role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>`;`

- 역할의 권한 설명:

`desc role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>`;`

- 사용자에게 역할 부여:

`grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`;`
