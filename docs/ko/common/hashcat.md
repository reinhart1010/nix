---
layout: page
title: common/hashcat (한국어)
description: "빠른 고급 비밀번호 복구 도구."
content_hash: 11e14f8a0ef07458748c14a840327ed55683e747
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/hashcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/hashcat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hashcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hashcat

빠른 고급 비밀번호 복구 도구.
더 많은 정보: <https://hashcat.net/wiki/doku.php?id=hashcat>.

- 기본 hashcat 마스크를 사용하여 무차별 대입 공격(모드 3)을 수행:

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_타입_아이디</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_값</span>

- 알려진 4자리 패턴으로 무차별 대입 공격(모드 3)을 수행:

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_타입_아이디</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_값</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">?d?d?d?d</span>`"`

- 인쇄 가능한 모든 ASCII 문자 중 최대 8개를 사용하여 무차별 대입 공격(모드 3)을 수행:

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_타입_아이디</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --increment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_값</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">?a?a?a?a?a?a?a?a</span>`"`

- Kali Linux 상자의 단어 목록을 사용하여 사전 공격(모드 0)을 수행:

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_타입_아이디</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/wordlists/rockyou.txt</span>

- 일반적인 비밀번호 변형으로 변형된 RockYou 단어 목록을 사용하여 규칙 기반 사전 공격(모드 0)을 수행:

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_타입_아이디</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --rules-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/hashcat/rules/best64.rule</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/wordlists/rockyou.txt</span>

- 두 가지 다른 사용자 정의 사전의 단어 연결을 사용하여 조합 공격(모드 1)을 수행:

`hashcat --hash-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_타입_아이디</span>` --attack-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/사전1.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/사전2.txt</span>

- 이미 크랙된 해시의 결과를 표시:

`hashcat --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_값</span>

- 모든 예시 해시 표시:

`hashcat --example-hashes`
