---
layout: page
title: common/odps-inst (한국어)
description: "ODPS(오픈 데이터 프로세싱 서비스)에서 인스턴스를 관리합니다."
content_hash: 97e871fa9874f82cad9d5688e14e91297e8b4a5d
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/odps-inst.html
    icon: bi bi-globe
tldri18n_status: 2
---
# odps inst

ODPS(오픈 데이터 프로세싱 서비스)에서 인스턴스를 관리합니다.
같이 보기: `odps`.
더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 현재 사용자가 생성한 인스턴스 보기:

`show instances;`

- 인스턴스의 세부 정보 설명:

`desc instance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_ID</span>`;`

- 인스턴스 상태 확인:

`status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_ID</span>`;`

- 인스턴스 종료를 대기하며 로그 및 진행 정보를 출력:

`wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_ID</span>`;`

- 인스턴스 종료:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_ID</span>`;`
