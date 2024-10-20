---
layout: page
title: common/ganache-cli (한국어)
description: "이더리움 개발을 위한 개인 블록체인 Ganache의 명령줄 버전."
content_hash: 39240375697b12a1e2669910eb4d9356bcb2e2ac
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/ganache-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ganache-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ganache-cli

이더리움 개발을 위한 개인 블록체인 Ganache의 명령줄 버전.
더 많은 정보: <https://www.trufflesuite.com/ganache>.

- Ganache 실행:

`ganache-cli`

- 특정 수의 계정으로 Ganache를 실행:

`ganache-cli --accounts=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_의_수</span>

- Ganache를 실행하고 기본적으로 사용 가능한 계정을 잠금:

`ganache-cli --secure`

- Ganache 서버를 실행하고 특정 계정을 잠금 해제:

`ganache-cli --secure --unlock "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_개인_키1</span>`" --unlock "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_개인_키2</span>`"`

- 특정 계정과 잔액으로 Ganache을 실행:

`ganache-cli --account="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_개인_키</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_잔액</span>`"`

- 기본 잔액이 있는 계정으로 Ganache를 실행:

`ganache-cli --defaultBalanceEther=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본_잔액</span>

- Ganache를 실행하고 모든 요청을 `stdout`에 기록:

`ganache-cli --verbose`
