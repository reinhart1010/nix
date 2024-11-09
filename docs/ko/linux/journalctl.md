---
layout: page
title: linux/journalctl (한국어)
description: "systemd 저널을 조회합니다."
content_hash: 815937b3d5d3bc968dccfc958ac26a1cdbec8f15
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/journalctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/journalctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/journalctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/journalctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/journalctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># journalctl

systemd 저널을 조회합니다.
더 많은 정보: <https://manned.org/journalctl>.

- 현재 [b]부트에서 우선순위 레벨 3(오류)로 모든 메시지 표시:

`journalctl -b --priority=3`

- 2일 이상된 저널 로그 삭제:

`journalctl --vacuum-time=2d`

- 마지막 N줄만 표시하고 새 메시지를 [f]팔로우(전통적인 syslog의 `tail -f`처럼) 표시:

`journalctl --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` --follow`

- 특정 [u]유닛의 모든 메시지 표시:

`journalctl --unit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유닛</span>

- 마지막으로 시작된 이후 유닛의 로그 표시:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유닛</span>`)`

- 시간 범위 내의 메시지 필터링(타임스탬프 또는 "yesterday" 같은 플레이스홀더 사용 가능):

`journalctl --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">now|today|yesterday|tomorrow</span>` --until "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD HH:MM:SS</span>`"`

- 특정 프로세스의 모든 메시지 표시:

`journalctl _PID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 특정 실행 파일의 모든 메시지 표시:

`journalctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행_파일</span>
