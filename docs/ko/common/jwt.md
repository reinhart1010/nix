---
layout: page
title: common/jwt (한국어)
description: "JSON Web Token(JWT) 처리."
content_hash: fd7a45923079e460b320843b2ba9bd284bfe649f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jwt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/jwt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jwt

JSON Web Token(JWT) 처리.
사용할 수 있는 암호화 알고리즘: HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384.
더 많은 정보: <https://github.com/mike-engel/jwt-cli>.

- JWT 디코드:

`jwt decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt_문자열</span>

- JWT를 JSON 문자열로 디코드:

`jwt decode -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt_문자열</span>

- JSON 문자열을 JWT로 인코드:

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json_문자열</span>`'`

- 키-값 쌍 페이로드를 JWT로 인코드:

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키=값</span>
