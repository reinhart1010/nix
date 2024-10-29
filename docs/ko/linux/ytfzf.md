---
layout: page
title: linux/ytfzf (한국어)
description: "비디오 및 음악을 찾고 다운로드. POSIX 셸로 작성되었습니다."
content_hash: b8445d50c4c06704079d72979acc177175a88e6a
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/ytfzf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ytfzf

비디오 및 음악을 찾고 다운로드. POSIX 셸로 작성되었습니다.
같이 보기: `youtube-dl`, `yt-dlp`, `instaloader`.
더 많은 정보: <https://github.com/pystardust/ytfzf>.

- YouTube에서 썸네일 미리보기로 비디오 검색:

`ytfzf --show-thumbnails `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- 첫 번째 항목의 오디오만 반복 재생:

`ytfzf --audio-only --auto-select --loop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- 기록에서 비디오 다운로드:

`ytfzf --download --choose-from-history`

- 검색에서 찾은 모든 음악 재생:

`ytfzf --audio-only --select-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- 외부 메뉴에서 인기 비디오 보기:

`ytfzf --trending --ext-menu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- YouTube 대신 PeerTube에서 검색:

`ytfzf --peertube `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>
