---
layout: page
title: common/cotton (한국어)
description: "마크다운 테스트 사양 러너."
content_hash: c92f5e69f72a663e69c4db4c98c02daac56e7e03
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cotton.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cotton

마크다운 테스트 사양 러너.
더 많은 정보: <https://github.com/chonla/cotton>.

- 특정 기본 URL 사용하기:

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>`.md`

- 인증서 확인 비활성화(비 보안 모드):

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본_url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>`.md`

- 테스트 실패시 실행 중지:

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본_url</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>`.md`
