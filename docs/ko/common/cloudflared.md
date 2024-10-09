---
layout: page
title: common/cloudflared (한국어)
description: "Cloudflare 네트워크에 대한 지속적인 연결을 생성."
content_hash: 7c8d0e2f0696265f535776f063afc347c050aa8e
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/common/cloudflared.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cloudflared

Cloudflare 네트워크에 대한 지속적인 연결을 생성.
더 많은 정보: <https://developers.cloudflare.com/argo-tunnel/>.

- Cloudflare 계정의 도메인에 대한 연결을 인증하고 연결:

`cloudflared tunnel login`

- 특정 이름의 터널을 생성:

`cloudflared tunnel create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 로컬 서버에서 Cloudflare의 호스트로 터널을 설정:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- 로컬 서버의 인증서를 확인하지 않고, 로컬 서버에서 Cloudflare의 호스트로 터널을 설정:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>` --no-tls-verify`

- 로그를 파일에 저장:

`cloudflared tunnel --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` http://localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>` --loglevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">panic|fatal|error|warn|info|debug</span>` --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- cloudflared를 시스템 서비스로 설치:

`cloudflared service install`
