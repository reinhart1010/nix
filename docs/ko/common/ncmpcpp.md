---
layout: page
title: common/ncmpcpp (한국어)
description: "Music Player Daemon을 위한 음악 플레이어 클라이언트."
content_hash: f86046313fae85218ccc0c79702e8fa504bf7cbc
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ncmpcpp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ncmpcpp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ncmpcpp

Music Player Daemon을 위한 음악 플레이어 클라이언트.
같이 보기: `mpd`, `mpc`, `qmmp`, `termusic`.
더 많은 정보: <https://rybczak.net/ncmpcpp>.

- 지정된 호스트와 포트의 음악 플레이어 데몬에 연결:

`ncmpcpp --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 현재 곡의 메타데이터를 콘솔에 표시:

`ncmpcpp --current-song`

- 지정된 설정 파일 사용:

`ncmpcpp --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 파일에서 다른 키 바인딩 세트 사용:

`ncmpcpp --bindings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>
