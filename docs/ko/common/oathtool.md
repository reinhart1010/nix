---
layout: page
title: common/oathtool (한국어)
description: "OATH 일회성 비밀번호 도구."
content_hash: 75db10fd6e08dd2dc4db51a0e2d9f4b066ec882e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/oathtool.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/oathtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# oathtool

OATH 일회성 비밀번호 도구.
더 많은 정보: <https://www.nongnu.org/oath-toolkit/oathtool.1.html>.

- TOTP 토큰 생성 (Google Authenticator처럼 동작):

`oathtool --totp --base32 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀</span>`"`

- 특정 시간에 대한 TOTP 토큰 생성:

`oathtool --totp --now "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2004-02-29 16:21:42</span>`" --base32 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀</span>`"`

- TOTP 토큰 검증:

`oathtool --totp --base32 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>`"`
