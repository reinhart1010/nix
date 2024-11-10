---
layout: page
title: linux/pyrit (한국어)
description: "계산 능력을 활용한 WPA/WPA2 크래킹 도구."
content_hash: d4ea34aa787a9c2c6cd20cb82ba302c0f29b986d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pyrit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pyrit

계산 능력을 활용한 WPA/WPA2 크래킹 도구.
더 많은 정보: <https://github.com/JPaulMora/Pyrit>.

- 시스템 크래킹 속도 표시:

`pyrit benchmark`

- 사용 가능한 코어 나열:

`pyrit list_cores`

- [e]SSID 설정:

`pyrit -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ESSID</span>`" create_essid`

- 특정 패킷 캡처 파일 [r]읽고 분석:

`pyrit -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cap|경로/대상/파일.pcap</span>` analyze`

- 현재 데이터베이스에 비밀번호 [i]가져오기:

`pyrit -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import_unique_passwords|unique_passwords|import_passwords</span>

- 데이터베이스에서 특정 파일로 비밀번호 [o]내보내기:

`pyrit -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` export_passwords`

- Pired 마스터 키로 비밀번호 변환:

`pyrit batch`

- 캡처 파일 [r]읽고 비밀번호 크래킹:

`pyrit -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` attack_db`
