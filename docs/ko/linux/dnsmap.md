---
layout: page
title: linux/dnsmap (한국어)
description: "dnsmap 명령은 도메인의 일반적인 하위 도메인(e.g. smtp.domain.org)을 스캔합니다."
content_hash: 7d38c9ec3184e41a54e8827a53d0c7053347ed0b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dnsmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnsmap

dnsmap 명령은 도메인의 일반적인 하위 도메인(e.g. smtp.domain.org)을 스캔합니다.
더 많은 정보: <https://github.com/resurrecting-open-source-projects/dnsmap>.

- 내부 단어 목록을 사용하여 하위 도메인 스캔:

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 확인할 하위 도메인 목록 지정:

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>

- 결과를 CSV 파일에 저장:

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 잘못된 양성으로 인식되는 2개의 IP 무시(최대 5개 가능):

`dnsmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123.45.67.89,98.76.54.32</span>
