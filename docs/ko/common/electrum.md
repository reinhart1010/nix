---
layout: page
title: common/electrum (한국어)
description: "인체공학적 Bitcoin 지갑 및 개인 키 관리."
content_hash: a88ab68a7c7341aaf2758920ab442e9892d896e8
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/electrum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/electrum.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/electrum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># electrum

인체공학적 Bitcoin 지갑 및 개인 키 관리.
더 많은 정보: <https://electrum.org>.

- 새로운 지갑 생성:

`electrum -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_wallet.dat</span>` create`

- 오프라인 시드에서 기존 지갑 복원:

`electrum -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recovery_wallet.dat</span>` restore -o`

- 오프라인으로 서명된 거래 생성:

`electrum mktx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amount</span>` -f 0.0000001 -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from</span>` -o`

- 모든 지갑 수신 주소 표시:

`electrum listaddresses -a`

- 메시지에 설명:

`electrum signmessage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- 메시지 확인:

`electrum verifymessage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- 특정 일렉트럼 서버 인스턴스에만 연결:

`electrum -p socks5:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>`:9050 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">56ckl5obj37gypcu.onion</span>`:50001:t -1`
