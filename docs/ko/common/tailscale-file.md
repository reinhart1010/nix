---
layout: page
title: common/tailscale-file (한국어)
description: "Tailscale 네트워크에서 연결된 장치 간에 파일을 전송."
content_hash: 1f92873daa7ef19ccc4f3dc4ab2d444016ebd307
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tailscale-file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tailscale file

Tailscale 네트워크에서 연결된 장치 간에 파일을 전송.
현재 동일한 Tailscale 네트워크 내에서도 다른 사용자가 소유한 장치로 파일을 보내는 것은 지원하지 않습니다.
더 많은 정보: <https://tailscale.com/kb/1106/taildrop/>.

- 특정 노드로 파일 전송:

`sudo tailscale file cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명|IP</span>`:`

- 현재 노드로 전송된 파일을 특정 디렉토리에 저장:

`sudo tailscale file get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
