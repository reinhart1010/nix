---
layout: page
title: common/pueue-add (한국어)
description: "실행할 작업을 대기열에 추가."
content_hash: 7733721380e1be3e8968f3d599e5d3780f9e3478
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue add

실행할 작업을 대기열에 추가.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 대기열에 임의의 명령 추가:

`pueue add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 플래그 또는 인수를 명령에 전달하여 대기열에 추가:

`pueue add -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 --인수 -f</span>

- 대기열에서 첫 번째인 경우 시작하지 않도록 명령 추가:

`pueue add --stashed -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsync --archive --compress /local/directory /remote/directory</span>

- 그룹에 명령 추가 및 즉시 시작, 그룹 관리에 대해서는 `pueue group` 참고:

`pueue add --immediate --group "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CPU_집중</span>`" -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ffmpeg -i input.mp4 frame_%d.png</span>

- 명령 추가 및 9번과 12번 명령이 성공적으로 완료된 후 시작:

`pueue add --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` --group "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트</span>`" -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transmission-cli torrent_file.torrent</span>

- 일정 시간 후 레이블을 붙여 명령 추가, 유효한 날짜 형식에 대해서는 `pueue enqueue` 참고:

`pueue add --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큰 파일 압축</span>`" --delay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수요일 10:30pm</span>`" -- "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7z a compressed_file.7z large_file.xml</span>`"`
