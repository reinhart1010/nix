---
layout: page
title: common/nice (한국어)
description: "프로그램을 사용자 정의 스케줄링 우선순위(친화도)로 실행."
content_hash: 9ff7afecbef99b2ff824a0fe3df3a1fc41d8928b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/nice.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nice

프로그램을 사용자 정의 스케줄링 우선순위(친화도)로 실행.
친화도 값은 -20(가장 높은 우선순위)에서 19(가장 낮은 우선순위)까지 범위.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- 변경된 우선순위로 프로그램 실행:

`nice -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">친화도_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명시적 옵션으로 우선순위 정의:

`nice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--adjustment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">친화도_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
