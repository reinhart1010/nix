---
layout: page
title: common/kcadm.sh (한국어)
description: "관리 작업 수행."
content_hash: b2a578bc07fc849ef62ccbad5d150503c014d5ea
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kcadm.sh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kcadm.sh

관리 작업 수행.
더 많은 정보: <https://www.keycloak.org/docs/latest/server_admin/#admin-cli>.

- 인증된 세션 시작:

`kcadm.sh config credentials --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --realm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">영역_이름</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 사용자 생성:

`kcadm.sh create users -s username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">영역_이름</span>

- 모든 영역 나열:

`kcadm.sh get realms`

- JSON 구성으로 영역 업데이트:

`kcadm.sh update realms/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">영역_이름</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>
