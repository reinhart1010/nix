---
layout: page
title: common/searchsploit (한국어)
description: "Exploit Database에서 익스플로잇, 쉘코드 및/또는 논문을 검색."
content_hash: c7c46bdac60324b682fddb1c1fe6122fabb5dbf3
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/searchsploit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# searchsploit

Exploit Database에서 익스플로잇, 쉘코드 및/또는 논문을 검색.
알려진 버전 번호가 검색어로 사용되면, 해당 버전에 대한 익스플로잇뿐만 아니라 지정된 버전 범위를 포함하는 다른 익스플로잇도 표시됩니다.
더 많은 정보: <https://www.exploit-db.com/searchsploit>.

- 익스플로잇, 쉘코드 또는 논문 검색:

`searchsploit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 특정 버전을 검색, 예: sudo 버전 1.8.27:

`searchsploit sudo 1.8.27`

- 발견된 리소스의 exploit-db 링크 표시:

`searchsploit --www `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 리소스를 현재 디렉토리로 복사 ([m]irror) (익스플로잇 번호 필요):

`searchsploit --mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">익스플로잇_번호</span>

- `$PAGER` 환경 변수에 정의된 페이지 뷰어를 사용하여 리소스를 e[x]amine:

`searchsploit --examine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">익스플로잇_번호</span>

- 로컬 Exploit Database [u]업데이트:

`searchsploit --update`

- [c]ommon [v]ulnerabilities and [e]xposures (CVE) 값 검색:

`searchsploit --cve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-44228</span>

- `nmap`의 XML 출력에서 서비스 버전 (`nmap -sV -oX nmap-output.xml`)으로 알려진 익스플로잇 확인:

`searchsploit --nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/nmap-output.xml</span>
