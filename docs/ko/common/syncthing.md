---
layout: page
title: common/syncthing (한국어)
description: "지속적인 양방향 분산 폴더 동기화 도구."
content_hash: e17a8535f669aa1ff2334ec7e10cd0b50a74d5b5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/syncthing.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/syncthing.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># syncthing

지속적인 양방향 분산 폴더 동기화 도구.
더 많은 정보: <https://docs.syncthing.net/>.

- Syncthing 시작:

`syncthing`

- 웹 브라우저를 열지 않고 Syncthing 시작:

`syncthing -no-browser`

- 장치 ID 출력:

`syncthing -device-id`

- 홈 디렉토리 변경:

`syncthing -home=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 전체 색인 교환 강제 수행:

`syncthing -reset-deltas`

- 웹 인터페이스가 수신 대기할 주소 변경:

`syncthing -gui-address=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소:포트|경로/대상/socket.sock</span>

- Syncthing이 사용하는 파일 경로 표시:

`syncthing -paths`

- Syncthing 모니터 프로세스 비활성화:

`syncthing -no-restart`
