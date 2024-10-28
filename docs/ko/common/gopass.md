---
layout: page
title: common/gopass (한국어)
description: "팀을 위한 표준 Unix 비밀번호 관리자. Go 언어로 작성됨."
content_hash: 114aa0d0f1e34c2f4e16df355ba169aad8b9276b
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/gopass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gopass

팀을 위한 표준 Unix 비밀번호 관리자. Go 언어로 작성됨.
더 많은 정보: <https://www.gopass.pw>.

- 구성 설정을 초기화:

`gopass init`

- 새로운 항목 생성:

`gopass new`

- 모든 저장소 보기:

`gopass mounts`

- 공유 Git 저장소 마운트:

`gopass mounts add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_레포지토리_주소</span>

- 키워드를 사용해 대화형으로 검색:

`gopass show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 키워드를 사용해 검색:

`gopass find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 마운트된 모든 저장소 동기화:

`gopass sync`

- 특정 비밀번호 항목을 표시:

`gopass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름|경로/대상/디렉터리|이메일@email.com</span>
