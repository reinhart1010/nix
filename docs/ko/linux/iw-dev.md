---
layout: page
title: linux/iw-dev (한국어)
description: "무선 장치를 표시하고 조작합니다."
content_hash: 151dbdce4f5437cc5107c5622a0ca9129cdfb49f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/iw-dev.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iw dev

무선 장치를 표시하고 조작합니다.
채널, 주파수 및 규제 정보 목록은 <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>.
더 많은 정보: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- 장치를 모니터 모드로 설정(인터페이스는 먼저 종료되어야 합니다. `ip link`도 참조):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set type monitor`

- 장치를 관리 모드로 설정(인터페이스는 먼저 종료되어야 합니다):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set type managed`

- 장치의 WiFi 채널 설정(장치는 먼저 인터페이스가 활성화된 상태에서 모니터 모드여야 합니다):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널_번호</span>

- 장치의 WiFi 주파수 설정(Mhz 단위)(장치는 먼저 인터페이스가 활성화된 상태에서 모니터 모드여야 합니다):

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` set freq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주파수_단위_메가헤르츠</span>

- 모든 알려진 스테이션 정보 표시:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` station dump`

- 특정 MAC 주소로 모니터 모드의 가상 인터페이스 생성:

`sudo iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` interface add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_인터페이스_이름</span>`" type monitor addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12:34:56:aa:bb:cc</span>

- 가상 인터페이스 삭제:

`sudo iw dev "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_인터페이스_이름</span>`" del`
