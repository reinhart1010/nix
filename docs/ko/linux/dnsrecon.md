---
layout: page
title: linux/dnsrecon (한국어)
description: "DNS 열거 도구."
content_hash: 8d61b6cfd96cf1408319717d19a2adbb6fcf5ee1
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dnsrecon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnsrecon

DNS 열거 도구.
더 많은 정보: <https://github.com/darkoperator/dnsrecon>.

- 도메인을 스캔하고 결과를 SQLite 데이터베이스에 저장:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스.sqlite</span>

- 도메인을 스캔하며 네임서버를 지정하고 존 전송 수행:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --name_server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nameserver.example.com</span>` --type axfr`

- 도메인을 스캔하며 서브도메인 및 호스트명의 사전으로 무차별 공격 수행:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --dictionary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사전.txt</span>` --type brt`

- 도메인을 스캔하며 SPF 레코드에서 IP 범위의 역방향 조회를 수행하고 JSON 파일에 결과 저장:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -s --json`

- 도메인을 스캔하며 Google 열거를 수행하고 CSV 파일에 결과 저장:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -g --csv`

- 도메인을 스캔하며 DNS 캐시 스누핑 수행:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --type snoop --name_server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nameserver.example.com</span>` --dictionary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사전.txt</span>

- 도메인을 스캔하며 존 워킹 수행:

`dnsrecon --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --type zonewalk`
