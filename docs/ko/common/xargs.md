---
layout: page
title: common/xargs (한국어)
description: "다른 명령, 파일 등으로부터 전달된 인수를 사용하여 명령을 실행."
content_hash: 5ade0ca8a9f1477b902746275901982bd7553e98
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xargs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xargs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xargs

다른 명령, 파일 등으로부터 전달된 인수를 사용하여 명령을 실행.
입력은 하나의 텍스트 블록으로 처리되며 공백, 탭, 개행 및 파일 끝에서 별개의 조각으로 분리됩니다.
더 많은 정보: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- 입력 데이터를 인수로 사용하여 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들_소스</span>` | xargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 입력 데이터에 대해 여러 연결된 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들_소스</span>` | xargs sh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어3</span>`"`

- 여러 스레드를 활용하여 `.log` 확장자를 가진 모든 파일을 gzip으로 압축 (`-print0`는 파일 이름을 null 문자로 분리하고, `-0`은 이를 구분자로 사용):

`find . -name '*.log' -print0 | xargs -0 -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -n 1 gzip`

- 각 인수에 대해 한 번씩 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들_소스</span>` | xargs -n1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 각 입력 줄에 대해 한 번씩 명령 실행, 입력 줄로 플레이스홀더(여기서는 `_`로 표시)를 대체:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들_소스</span>` | xargs -I _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택적_추가_인수들</span>

- 한 번에 `최대-프로세스` 프로세스까지 병렬 실행; 기본값은 1입니다. `최대-프로세스`가 0인 경우, xargs는 가능한 많은 프로세스를 동시에 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들_소스</span>` | xargs -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대-프로세스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
