---
layout: page
title: common/nmap (한국어)
description: "네트워크 탐색 도구 및 보안/포트 스캐너."
content_hash: 7faec66637bbc2238b20433d4ed0b6729b50bc49
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/nmap.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nmap.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nmap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmap

네트워크 탐색 도구 및 보안/포트 스캐너.
일부 기능(예: SYN 스캔)은 `nmap`을 루트 권한으로 실행할 때만 활성화됩니다.
더 많은 정보: <https://nmap.org/book/man.html>.

- 원격 호스트의 상위 1000개 포트를 다양한 [v]erbosity 수준으로 스캔:

`nmap -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소_또는_호스트명</span>

- 매우 공격적으로 전체 서브넷 또는 개별 호스트에 핑 스위프 실행:

`nmap -T5 -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24|IP_주소_또는_호스트명1,IP_주소_또는_호스트명2,...</span>

- 파일에 있는 호스트에 대해 OS 감지, 버전 감지, 스크립트 스캔 및 트레이서우트 활성화:

`sudo nmap -A -iL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 특정 포트 목록 스캔 (1부터 65535까지 모든 포트를 스캔하려면 `-p-` 사용):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트1,포트2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소_또는_호스트명1,IP_주소_또는_호스트명2,...</span>

- 기본 NSE 스크립트를 사용하여 상위 1000개 포트의 서비스 및 버전 감지 수행 후 결과를 (`-oA`) 출력 파일에 저장:

`nmap -sC -sV -oA `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top-1000-ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소_또는_호스트명1,IP_주소_또는_호스트명2,...</span>

- `기본 및 안전` NSE 스크립트를 사용하여 대상 신중하게 스캔:

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소_또는_호스트명1,IP_주소_또는_호스트명2,...</span>

- 표준 포트 80과 443에서 실행 중인 웹 서버를 모든 사용 가능한 `http-*` NSE 스크립트를 사용하여 스캔:

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소_또는_호스트명1,IP_주소_또는_호스트명2,...</span>` -p 80,443`

- 매우 느린 스캔 (`-T0`), 디코이 소스 주소 (`-D`), [f]ragmented 패킷, 랜덤 데이터 및 기타 방법을 사용하여 IDS/IPS 감지를 피하려고 시도:

`sudo nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디코이_IP1,디코이_IP2,...</span>` --source-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">53</span>` -f --data-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -Pn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소_또는_호스트명</span>
