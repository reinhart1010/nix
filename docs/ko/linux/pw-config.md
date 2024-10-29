---
layout: page
title: linux/pw-config (한국어)
description: "PipeWire 서버와 클라이언트에서 사용될 설정 경로와 섹션 나열."
content_hash: 750455eb8e55efbd09ef649b497f45d8a4f6a4ec
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pw-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-config

PipeWire 서버와 클라이언트에서 사용될 설정 경로와 섹션 나열.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- 사용될 모든 설정 파일 나열:

`pw-config`

- PipeWire PulseAudio 서버에서 사용될 모든 설정 파일 나열:

`pw-config --name pipewire-pulse.conf`

- PipeWire PulseAudio 서버에서 사용되는 모든 설정 섹션 나열:

`pw-config --name pipewire-pulse.conf list`

- JACK 클라이언트에서 사용되는 `context.properties` 조각 나열:

`pw-config --name jack.conf list context.properties`

- JACK 클라이언트에서 사용되는 병합된 `context.properties` 나열:

`pw-config --name jack.conf merge context.properties`

- PipeWire 서버에서 사용되는 병합된 `context.modules` 나열 및 [r]eformat:

`pw-config --name pipewire.conf --recurse merge context.modules`

- 도움말 표시:

`pw-config --help`
