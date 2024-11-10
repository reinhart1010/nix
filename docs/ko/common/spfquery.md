---
layout: page
title: common/spfquery (한국어)
description: "전송자 정책 프레임워크(SPF) 레코드를 조회하여 이메일 발신자를 검증합니다."
content_hash: e3c30b975d77a52791226c8abd7f3898c7cefb41
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/spfquery.html
    icon: bi bi-globe
tldri18n_status: 2
---
# spfquery

전송자 정책 프레임워크(SPF) 레코드를 조회하여 이메일 발신자를 검증합니다.
더 많은 정보: <https://manned.org/spfquery>.

- 특정 IP 주소가 지정된 이메일 주소에서 이메일을 보낼 수 있는지 확인:

`spfquery -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` -sender `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">보낸이@example.com</span>

- 디버깅 출력을 활성화:

`spfquery -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` -sender `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">보낸이@example.com</span>` --debug`
