---
layout: page
title: common/vinmap (한국어)
description: "IP 범위를 청크로 나누고 병렬 스캔을 수행하며 XML 또는 JSON 결과를 병합하는 멀티스레드 Nmap 스캐너."
content_hash: 91a29a78d8dcea9abdd780f634fce120d9787243
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vinmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vinmap

IP 범위를 청크로 나누고 병렬 스캔을 수행하며 XML 또는 JSON 결과를 병합하는 멀티스레드 Nmap 스캐너.
더 많은 정보: <https://pypi.org/project/vinmap>.

- 서브넷에 대한 기본 스캔 수행:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.0/24</span>

- 버전 및 OS 감지로 도메인을 스캔하고 결과를 특정 파일에 저장:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -s "-sV -O" -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/scan_results.xml</span>

- IP 범위를 10개의 청크와 20개의 동시 스레드를 사용하여 스캔, 지정하지 않으면 시스템 CPU 코어의 절반 사용:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1-10.0.0.255</span>` -n 10 -t 20`

- JSON 형식으로 스캔 결과 출력:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1-192.168.1.100</span>` -f json`

- 기본 설정으로 여러 IP 스캔하고 병합된 XML 출력 저장:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1,192.168.1.2,...</span>
