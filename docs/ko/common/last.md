---
layout: page
title: common/last (한국어)
description: "마지막으로 로그인한 사용자 보기."
content_hash: fe8f4bef20aea193c348b9fe5a796da9c3dbc915
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/last.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/last.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/last.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># last

마지막으로 로그인한 사용자 보기.
더 많은 정보: <https://manned.org/last>.

- `/var/log/wtmp`에서 읽어들인 마지막 로그인, 지속 시간 및 기타 정보 보기:

`last`

- 표시할 마지막 로그인 수 지정:

`last -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그인_수</span>

- 항목의 전체 날짜와 시간을 출력하고 호스트 이름 열이 잘리지 않도록 마지막에 표시:

`last -F -a`

- 특정 사용자의 모든 로그인 보기 및 호스트 이름 대신 IP 주소 표시:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -i`

- 모든 기록된 재부팅 보기 (즉, 가상 사용자 "reboot"의 마지막 로그인):

`last reboot`

- 모든 기록된 종료 보기 (즉, 가상 사용자 "shutdown"의 마지막 로그인):

`last shutdown`
