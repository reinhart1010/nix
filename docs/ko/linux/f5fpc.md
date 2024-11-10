---
layout: page
title: linux/f5fpc (한국어)
description: "BIG-IP Edge의 독점 상업용 SSL VPN 클라이언트."
content_hash: 8e79da65be74328d4726018f6655d394d995d138
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/f5fpc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# f5fpc

BIG-IP Edge의 독점 상업용 SSL VPN 클라이언트.
더 많은 정보: <https://techdocs.f5.com/kb/en-us/products/big-ip_apm/manuals/product/apm-client-configuration-11-4-0/4.html>.

- 새 VPN 연결 열기:

`sudo f5fpc --start`

- 특정 호스트에 새 VPN 연결 열기:

`sudo f5fpc --start --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host.example.com</span>

- 사용자명 지정 (암호는 사용자에게 요청됨):

`sudo f5fpc --start --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host.example.com</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>

- 현재 VPN 상태 표시:

`sudo f5fpc --info`

- VPN 연결 종료:

`sudo f5fpc --stop`
