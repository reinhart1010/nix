---
layout: page
title: common/npm-unstar (한국어)
description: "패키지에서 즐겨찾기/별표 표시를 제거."
content_hash: 40aa6044fff0d7c48aa66d31ae0884d15bfbd637
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/npm-unstar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm unstar

패키지에서 즐겨찾기/별표 표시를 제거.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-unstar>.

- 기본 레지스트리에서 공개 패키지의 별표 제거:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 특정 범위 내의 패키지의 별표 제거:

`npm unstar @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">범위</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 특정 레지스트리에서 패키지의 별표 제거:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_URL</span>

- 인증이 필요한 비공개 패키지의 별표 제거:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --auth-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacy|oauth|web|saml</span>

- 이중 인증을 위한 OTP를 제공하여 패키지의 별표 제거:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --otp=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">OTP</span>

- 특정 로깅 수준으로 패키지의 별표 제거:

`npm unstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --loglevel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">silent|error|warn|notice|http|timing|info|verbose|silly</span>
