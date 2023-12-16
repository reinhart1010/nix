---
layout: page
title: common/audacious (한국어)
description: "오픈 소스 오디오 플레이어."
content_hash: dd75ba2275373a606ec9e648043bd4040b58522f
last_modified_at: 2023-12-16
related_topics:
  - title: English version
    url: /en/common/audacious.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/audacious.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/audacious.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># audacious

오픈 소스 오디오 플레이어.
더 많은 정보: <https://audacious-media-player.org>.

- 프로그램 실행:

`audacious`

- 오디오 파일의 특정 디렉터리를 대기열에 삽입:

`audacious --enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 재생 시작 또는 중지:

`audacious --play-pause`

- 재생 목록에서 앞으로 또는 뒤로 건너뛰기:

`audacious --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fwd|rew</span>

- 재생 중지:

`audacious --stop`

- 헤드리스 버전 시작:

`audacious --headless`

- 재생이 중지되거나 재생할 내용이 없으면 즉시 종료:

`audacious --quit-after-play`
