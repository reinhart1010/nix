---
layout: page
title: common/npm-adduser (한국어)
description: "레지스트리 사용자 계정 추가."
content_hash: d3a184db88aa4e71f1984842f3a7587da4d798ba
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/npm-adduser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm adduser

레지스트리 사용자 계정 추가.
더 많은 정보: <https://docs.npmjs.com/cli/npm-adduser>.

- 지정된 레지스트리에 새 사용자 생성하고 자격 증명을 `.npmrc`에 저장:

`npm adduser --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_주소</span>

- 특정 범위로 개인 레지스트리에 로그인:

`npm login --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@조직</span>` --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://registry.mycorp.com</span>

- 특정 범위에서 로그아웃하고 인증 토큰 제거:

`npm logout --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@조직</span>

- 초기화 중 범위가 지정된 패키지 생성:

`npm init --scope=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--yes</span>
