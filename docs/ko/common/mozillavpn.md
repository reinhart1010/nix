---
layout: page
title: common/mozillavpn (한국어)
description: "Firefox 제작사에서 제공하는 가상 사설망."
content_hash: a3270ae87e1a3571a96644a30a8e1815f3c37d18
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mozillavpn.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mozillavpn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mozillavpn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mozillavpn

Firefox 제작사에서 제공하는 가상 사설망.
같이 보기: `fastd`, `ivpn`, `mullvad`, `warp-cli`.
더 많은 정보: <https://github.com/mozilla-mobile/mozilla-vpn-client/wiki/Command-line-interface>.

- 대화형 프롬프트로 로그인:

`mozillavpn login`

- Mozilla VPN에 연결:

`mozillavpn activate`

- 연결 상태 표시:

`mozillavpn status`

- 사용 가능한 서버 목록 표시:

`mozillavpn servers`

- 특정 서버 선택:

`mozillavpn select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_이름</span>

- Mozilla VPN 연결 해제:

`mozillavpn deactivate`

- 로그아웃:

`mozillavpn logout`

- 하위 명령에 대한 도움말 표시:

`mozillavpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`
