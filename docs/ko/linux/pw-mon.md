---
layout: page
title: linux/pw-mon (한국어)
description: "PipeWire 인스턴스의 객체를 모니터링."
content_hash: 7713666d1fd5043d8b57651965ec8a7bf9967202
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-mon.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-mon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-mon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-mon

PipeWire 인스턴스의 객체를 모니터링.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-mon_1.html>.

- 기본 PipeWire 인스턴스 모니터링:

`pw-mon`

- 특정 원격 인스턴스 모니터링:

`pw-mon --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 색상 설정을 지정하여 기본 인스턴스 모니터링:

`pw-mon --color=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">never|always|auto</span>

- 도움말 표시:

`pw-mon --help`
