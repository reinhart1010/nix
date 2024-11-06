---
layout: page
title: common/npm-star (한국어)
description: "패키지를 즐겨찾기로 표시."
content_hash: 45a12b4aa814730ddfcea46918dc98f5fe0af210
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/npm-star.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm star

패키지를 즐겨찾기로 표시.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-star>.

- 기본 레지스트리에서 공개 패키지 즐겨찾기:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 특정 스코프 내의 패키지 즐겨찾기:

`npm star @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스코프</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 특정 레지스트리에서 패키지 즐겨찾기:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_URL</span>

- 인증이 필요한 비공개 패키지 즐겨찾기:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --auth-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacy|oauth|web|saml</span>

- 2단계 인증을 위한 OTP를 제공하여 패키지 즐겨찾기:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --otp=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">OTP</span>

- 자세한 로그와 함께 패키지 즐겨찾기:

`npm star `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` --loglevel=verbose`

- 즐겨찾기한 모든 패키지 나열:

`npm star --list`

- 특정 레지스트리에서 즐겨찾기한 패키지 나열:

`npm star --list --registry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_URL</span>
