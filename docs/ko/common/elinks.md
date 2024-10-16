---
layout: page
title: common/elinks (한국어)
description: "`lynx`와 유사한 텍스트 기반 브라우저."
content_hash: 61c44a465c93a1b5120e1b7f41f77551c4177645
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/elinks.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/elinks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/elinks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># elinks

`lynx`와 유사한 텍스트 기반 브라우저.
더 많은 정보: <http://elinks.or.cz>.

- ELink 시작:

`elinks`

- elinks 종료:

`<Ctrl> + C`

- 웹페이지 출력을 콘솔에 덤프하고, ANSI 제어 코드로 텍스트 색상을 지정:

`elinks -dump -dump-color-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
