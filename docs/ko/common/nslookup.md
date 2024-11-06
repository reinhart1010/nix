---
layout: page
title: common/nslookup (한국어)
description: "다양한 도메인 레코드에 대해 네임 서버에 질의."
content_hash: a7f58ce330c333ceb3d17d9c21a03698a720cfb8
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nslookup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nslookup

다양한 도메인 레코드에 대해 네임 서버에 질의.
더 많은 정보: <https://manned.org/nslookup>.

- 시스템의 기본 네임 서버에 도메인의 IP 주소 (A 레코드) 질의:

`nslookup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 주어진 네임 서버에 도메인의 NS 레코드 질의:

`nslookup -type=NS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- IP 주소의 역방향 조회 (PTR 레코드) 질의:

`nslookup -type=PTR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">54.240.162.118</span>

- TCP 프로토콜을 사용하여 모든 사용 가능한 레코드 질의:

`nslookup -vc -type=ANY `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 주어진 네임 서버에 도메인의 전체 존 파일 (존 전송)을 TCP 프로토콜을 사용하여 질의:

`nslookup -vc -type=AXFR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임_서버</span>

- 도메인의 메일 서버 (MX 레코드) 질의, 트랜잭션 세부사항 표시:

`nslookup -type=MX -debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 포트 번호로 주어진 네임 서버에 도메인의 TXT 레코드 질의:

`nslookup -port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>` -type=TXT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임_서버</span>
