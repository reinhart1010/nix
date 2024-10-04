---
layout: page
title: common/choose (한국어)
description: "cut 및 (때떄로) awk에 대한 사람 친화적이고 빠른 대안."
content_hash: 254fb94b90d28eb0b0c622afb8c97bd812a9458d
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/choose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choose

cut 및 (때떄로) awk에 대한 사람 친화적이고 빠른 대안.
더 많은 정보: <https://github.com/theryangeary/choose>.

- 한 줄에서 5번째 항목을 출력 (0부터 시작):

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 공백 대신 ':'으로 항목을 구분하는 줄의 첫 번째, 세 번째, 다섯 번째 항목을 출력:

`choose --field-separator '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 5번째 항목을 포함하여, 줄의 2번째 항목부터 5번째 항목까지 모든 항목을 출력:

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 5번째 항목을 제외하고, 줄의 2번째 항목부터 5번째 항목까지 모든 항목을 출력:

`choose --exclusive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 줄의 시작 부분을 세 번째 항목에 출력:

`choose :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 줄의 처음부터 세번쨰(제외) 항목까지 모든 항목을 출력:

`choose --exclusive :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 3번쨰부터 줄 끝까지의 모든 항목을 출력:

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:`

- 줄의 마지막 항목을 출력:

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>
