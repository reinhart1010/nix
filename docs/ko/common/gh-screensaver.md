---
layout: page
title: common/gh-screensaver (한국어)
description: "GitHub CLI용 확장 기능으로 애니메이션 터미널 화면 보호기를 실행합니다."
content_hash: 9822b53d4ee0c8b5817bb963f6de7e7378f1052b
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-screensaver.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-screensaver.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh screensaver

GitHub CLI용 확장 기능으로 애니메이션 터미널 화면 보호기를 실행합니다.
같이 보기: `gh extension`.
더 많은 정보: <https://github.com/vilmibm/gh-screensaver>.

- 무작위 화면 보호기 실행:

`gh screensaver`

- 특정 화면 보호기 실행:

`gh screensaver --saver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fireworks|life|marquee|pipes|pollock|starfield</span>

- 특정 텍스트와 폰트를 사용하여 "marquee" 화면 보호기 실행:

`gh screensaver --saver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">marquee</span>` -- --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" --font=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폰트_이름</span>

- 특정 밀도와 속도로 "starfield" 화면 보호기 실행:

`gh screensaver --saver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">starfield</span>` -- --density `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 사용 가능한 화면 보호기 목록 나열:

`gh screensaver --list`
