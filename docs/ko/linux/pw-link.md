---
layout: page
title: linux/pw-link (한국어)
description: "PipeWire에서 포트 간의 링크를 관리."
content_hash: 3f2f46bc5a191ed521381b5a085acd101b253baa
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-link.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-link.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-link.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-link.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-link

PipeWire에서 포트 간의 링크를 관리.
더 많은 정보: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- 모든 오디오 출력 및 입력 포트와 해당 ID 나열:

`pw-link --output --input --ids`

- 출력 포트와 입력 포트 간 링크 생성:

`pw-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_포트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_포트_이름</span>

- 두 포트 간 연결 해제:

`pw-link --disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_포트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_포트_이름</span>

- 모든 링크와 해당 ID 나열:

`pw-link --links --ids`

- 도움말 표시:

`pw-link -h`
