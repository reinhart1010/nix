---
layout: page
title: linux/burpsuite (한국어)
description: "주로 웹 애플리케이션 침투 테스트에 사용되는 GUI 기반 애플리케이션."
content_hash: a8ca402be4c9b994747fc6372753cd86d72303ab
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/burpsuite.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/burpsuite.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># burpsuite

주로 웹 애플리케이션 침투 테스트에 사용되는 GUI 기반 애플리케이션.
더 많은 정보: <https://portswigger.net/burp/documentation/desktop/troubleshooting/launch-from-command-line>.

- Burp Suite 시작:

`burpsuite`

- 기본 설정을 사용하여 Burp Suite 시작:

`burpsuite --use-defaults`

- 특정 프로젝트 파일 열기:

`burpsuite --project-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 구성 파일 로드:

`burpsuite --config-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 확장 기능 없이 시작:

`burpsuite --disable-extensions`
