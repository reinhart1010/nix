---
layout: page
title: linux/wol (한국어)
description: "Wake-on-LAN 매직 패킷을 보내는 클라이언트."
content_hash: 37beef4d5aa81485f8755078a00942a8013dbdf7
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wol.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wol

Wake-on-LAN 매직 패킷을 보내는 클라이언트.
더 많은 정보: <https://sourceforge.net/projects/wake-on-lan/>.

- 장치에 WoL 패킷 전송:

`wol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MAC_주소</span>

- 다른 서브넷의 IP를 기반으로 장치에 WoL 패킷 전송:

`wol --ipaddr=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MAC_주소</span>

- 다른 서브넷의 호스트명을 기반으로 장치에 WoL 패킷 전송:

`wol --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MAC_주소</span>

- 특정 포트의 호스트에 WoL 패킷 전송:

`wol --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MAC_주소</span>

- [하]드웨어 주소, IP 주소/호스트명, 선택적 포트 및 SecureON 비밀번호를 [f]파일에서 읽기:

`wol --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- [v]자세히 출력 켜기:

`wol --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MAC_주소</span>
