---
layout: page
title: linux/usbip (한국어)
description: "원격으로 USB 장치를 사용합니다."
content_hash: 6e04ab1bf54170f38c1f5711a1e9dd1bb437b0f3
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/usbip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# usbip

원격으로 USB 장치를 사용합니다.
더 많은 정보: <https://usbip.sourceforge.net>.

- 모든 로컬 USB 장치와 해당 버스 ID 나열:

`usbip list --local`

- 서버에서 `usbip` 데몬 시작:

`systemctl start usbipd`

- 서버에서 USB 장치를 `usbip`에 바인드:

`sudo usbip bind --busid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스_ID</span>

- 클라이언트에서 `usbip`에 필요한 커널 모듈 로드:

`sudo modprobe vhci-hcd`

- 클라이언트에서 `usbip` 장치에 연결(버스 ID는 서버와 동일합니다):

`sudo usbip attach -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>` --busid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스_ID</span>

- 연결된 장치 나열:

`usbip port`

- 장치에서 분리:

`sudo usbip detach --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 장치의 바인드 해제:

`usbip unbind --busid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스_ID</span>
