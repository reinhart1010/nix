---
layout: page
title: common/reflex (한국어)
description: "특정 파일이 변경되면 디렉토리를 모니터링하고 명령을 다시 실행."
content_hash: 8df0238bc0aa3f67256e18773f06bb739ac8f4d0
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/reflex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reflex

특정 파일이 변경되면 디렉토리를 모니터링하고 명령을 다시 실행.
더 많은 정보: <https://github.com/cespare/reflex>.

- 파일이 변경되면 `make`로 다시 빌드:

`reflex make`

- `.go` 파일이 변경되면 Go 애플리케이션을 컴파일하고 실행:

`reflex --regex='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\.go$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go run .</span>

- 변경 사항을 모니터링할 때 디렉토리를 무시:

`reflex --inverse-regex='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^dir/</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `reflex`가 시작될 때 명령어를 실행하고 파일이 변경되면 다시 시작:

`reflex --start-service=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 변경된 파일 이름을 대체하여 출력:

`reflex -- echo {}`
