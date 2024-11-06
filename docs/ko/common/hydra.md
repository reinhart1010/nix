---
layout: page
title: common/hydra (한국어)
description: "온라인 비밀번호 추측 도구."
content_hash: 59314142dc6fa969f6eff73109682c1a600e02cf
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hydra.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hydra

온라인 비밀번호 추측 도구.
지원되는 프로토콜에는 FTP, HTTP(S), SMTP, SNMP, XMPP, SSH 등이 포함됨.
더 많은 정보: <https://github.com/vanhauser-thc/thc-hydra>.

- Hydra의 마법사를 시작:

`hydra-wizard`

- 주어진 사용자 이름과 비밀번호 목록을 사용하여 SSH 자격 증명을 추측:

`hydra -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- 두 개의 특정 사용자명 및 비밀번호 목록을 사용하여 HTTPS 웹 양식 자격 증명을 추측 ("https_post_request"는 "사용자명=^USER^&password=^PASS^"와 유사할 수 있음):

`hydra -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명.txt</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https-post-form</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_없는_url</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https_post_요청</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그인_실패_문자열</span>`"`

- 사용자명과 비밀번호 목록을 사용하여 FTP 자격 증명을 추측하고, 스레드 수를 지정:

`hydra -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명.txt</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_tasks</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp</span>

- 사용자명과 비밀번호 목록을 사용하여 MySQL 자격 증명을 추측하고, 사용자명/비밀번호 쌍이 발견되면 종료됨:

`hydra -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>

- 각 시도를 보여주는 사용자명과 비밀번호 목록을 사용하여, RDP 자격 증명을 추측:

`hydra -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rdp://호스트_ip</span>

- 콜론으로 구분된 사용자명/비밀번호 쌍 목록을 사용하여, 다양한 호스트의 IMAP 자격 증명을 추측:

`hydra -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명_비밀번호_쌍.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imap://[호스트_범위_cidr]</span>

- 사용자명과 비밀번호 목록을 사용하여 호스트 목록에서 POP3 자격 증명을 추측하고, 사용자명/비밀번호 쌍이 발견되면 종료됨:

`hydra -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명.txt</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/호스트.txt</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pop3</span>
