---
layout: page
title: common/cs-complete-dep (한국어)
description: "웹에서 직접 검색하지 않고도 라이브러리를 검색할 수 있음."
content_hash: 3be08e454c181da1ad2ed9eda3bfee68a8ab3dad
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/cs-complete-dep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cs complete dep

웹에서 직접 검색하지 않고도 라이브러리를 검색할 수 있음.
더 많은 정보: <https://get-coursier.io/docs/cli-complete>.

- 특정 Maven 그룹 식별자로 게시된 아티팩트를 출력:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>

- 특정 Maven 그룹 식별자 및 아티팩트 식별자로 게시된 라이브러리 버전을 나열:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_아이디</span>

- ivy2local에서 검색하여 특정 Maven 그룹 ID 아래에 게시된 아티팩트를 출력:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>` --repository ivy2local`

- 특정 저장소 및 자격 증명에서 검색하는 Maven 그룹 식별자 아래에 게시된 아티팩트를 나열:

`cs complete-dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_아이디</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>` --credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
