---
layout: page
title: common/safe (한국어)
description: "HashiCorp Vault와 상호작용."
content_hash: b26698e0cfac155ec78530caf065dd5af3efa80d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/safe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/safe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># safe

HashiCorp Vault와 상호작용.
더 많은 정보: <https://github.com/starkandwayne/safe>.

- 안전한 타겟 추가:

`safe target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>

- 인증 토큰을 사용하여 Vault 서버에 CLI 클라이언트 인증:

`safe auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증_토큰</span>

- 현재 타겟을 설명하는 환경 변수 출력:

`safe env`

- 주어진 경로에 대한 모든 접근 가능한 키의 트리 계층 구조 표시:

`safe tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>

- 비밀을 한 경로에서 다른 경로로 이동:

`safe move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기존/경로/대상/비밀</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운/경로/대상/비밀</span>

- 새로운 2048비트 SSH 키 쌍 생성 및 저장:

`safe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀</span>

- 비민감 키를 비밀에 설정:

`safe set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 자동 생성된 비밀번호를 비밀에 설정:

`safe gen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>
