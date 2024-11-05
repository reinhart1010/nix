---
layout: page
title: common/pamixer (한국어)
description: "PulseAudio를 위한 간단한 커맨드라인 믹서."
content_hash: c9047c4eb31c888e07b56120731d00c534f29240
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamixer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamixer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamixer

PulseAudio를 위한 간단한 커맨드라인 믹서.
더 많은 정보: <https://github.com/cdemoulins/pamixer>.

- 모든 싱크 및 소스를 해당 ID와 함께 나열:

`pamixer --list-sinks --list-sources`

- 기본 싱크의 볼륨을 75%로 설정:

`pamixer --set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>

- 기본이 아닌 싱크 음소거 전환:

`pamixer --toggle-mute --sink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>

- 기본 싱크의 볼륨을 5% 증가:

`pamixer --increase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 소스의 볼륨을 5% 감소:

`pamixer --decrease `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>

- 100% 이상으로 볼륨을 증가, 감소 또는 설정하기 위해 부스트 허용 옵션 사용:

`pamixer --set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">105</span>` --allow-boost`

- 기본 싱크 음소거 (`--unmute`를 사용하여 음소거 해제 가능):

`pamixer --mute`
