---
layout: page
title: linux/protonvpn (한국어)
description: "비공식 서드파티 ProtonVPN 클라이언트."
content_hash: f7323c94198fdf750fe92db9124d1ace49f9671f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/protonvpn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/protonvpn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># protonvpn

비공식 서드파티 ProtonVPN 클라이언트.
같이 보기: `protonvpn-connect`.
더 많은 정보: <https://github.com/Rafficer/linux-cli-community>.

- ProtonVPN 프로필 초기화:

`protonvpn init`

- ProtonVPN에 대화형으로 연결:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>

- 연결 상태 표시:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|status</span>

- ProtonVPN 연결 해제:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|disconnect</span>

- 마지막으로 사용한 서버에 다시 연결 또는 연결:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|reconnect</span>

- OpenVPN 구성 및 서버 데이터 새로고침:

`protonvpn refresh`

- 하위 명령의 도움말 표시:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`
