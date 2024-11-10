---
layout: page
title: common/ss-local (한국어)
description: "Shadowsocks 클라이언트를 SOCKS5 프록시로 실행."
content_hash: f441a5a61c69c756dc6903317f143c51cb19bf4c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/ss-local.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ss-local

Shadowsocks 클라이언트를 SOCKS5 프록시로 실행.
더 많은 정보: <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>.

- 호스트, 서버 포트, 로컬 포트, 비밀번호 및 암호화 방법을 지정하여 Shadowsocks 프록시 실행:

`ss-local -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_포트</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호화_방법</span>

- 구성 파일을 지정하여 Shadowsocks 프록시 실행:

`ss-local -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정/파일.json</span>

- 플러그인을 사용하여 프록시 클라이언트 실행:

`ss-local --plugin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>` --plugin-opts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_옵션</span>

- TCP 패스트 오픈 활성화:

`ss-local --fast-open`
