---
layout: page
title: common/vault (한국어)
description: "HashiCorp Vault와 상호작용."
content_hash: 2ce0071b78de53b5d87fa3df0878db4318e2ba3b
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/vault.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vault.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vault

HashiCorp Vault와 상호작용.
더 많은 정보: <https://www.vaultproject.io/docs/commands>.

- Vault 서버에 연결하고 새로운 암호화 데이터 저장소 초기화:

`vault init`

- 암호화된 데이터 저장소에 접근하기 위해 필요한 키 공유 중 하나를 제공하여 금고의 잠금 해제:

`vault unseal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_공유_x</span>

- 인증 토큰을 사용하여 Vault 서버에 대해 CLI 클라이언트 인증:

`vault auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증_토큰</span>

- "secret"이라는 일반 백엔드를 사용하여 금고에 새 비밀 저장:

`vault write secret/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello</span>` value=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">world</span>

- "secret"이라는 일반 백엔드를 사용하여 금고에서 값 읽기:

`vault read secret/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello</span>

- 값에서 특정 필드 읽기:

`vault read -field=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드_이름</span>` secret/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello</span>

- 데이터 저장소의 암호화 키를 메모리에서 제거하여 Vault 서버 잠금:

`vault seal`
