---
layout: page
title: linux/torsocks (한국어)
description: "모든 애플리케이션의 트래픽을 Tor 네트워크를 통해 라우팅합니다."
content_hash: b3bc7fcdd1aaaff7e3c3df54433f13a6330781ee
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/torsocks.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/torsocks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/torsocks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># torsocks

모든 애플리케이션의 트래픽을 Tor 네트워크를 통해 라우팅합니다.
참고: `torsocks`는 Tor 데몬의 기본값인 127.0.0.1:9050에서 실행 중인 Tor SOCKS 프록시에 연결해야 한다고 가정합니다.
더 많은 정보: <https://gitlab.torproject.org/tpo/core/torsocks/>.

- Tor를 사용하여 명령 실행:

`torsocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 이 셸에서 Tor 활성화 또는 비활성화:

`. torsocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Tor가 활성화된 새로운 셸 생성:

`torsocks --shell`

- 현재 셸이 Tor가 활성화되었는지 확인 (`LD_PRELOAD` 값이 비어 있으면 비활성화됨):

`torsocks show`

- 다른 Tor 회로를 통해 트래픽을 [i]솔레이트하여 익명성 향상:

`torsocks --isolate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">curl https://check.torproject.org/api/ip</span>

- 특정 [a]주소 및 [P]포트에서 실행 중인 Tor 프록시에 연결:

`torsocks --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
