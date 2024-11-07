---
layout: page
title: common/react-native-start (한국어)
description: "React Native 서버를 시작하는 명령줄 도구."
content_hash: ea8c124cb42e406f3268028b1d664e9b83e2a94b
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/react-native-start.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/react-native-start.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># react-native start

React Native 서버를 시작하는 명령줄 도구.
더 많은 정보: <https://github.com/react-native-community/cli/blob/master/docs/commands.md#start>.

- 연결된 기기와 통신하는 서버 시작:

`react-native start`

- 캐시를 초기화하여 메트로 번들러 시작:

`react-native start --reset-cache`

- 사용자 지정 포트(기본값은 8081)로 서버 시작:

`react-native start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3000</span>

- 자세한 모드로 서버 시작:

`react-native start --verbose`

- 파일 변환 작업을 위한 최대 작업자 수 지정(기본값은 CPU 코어 수):

`react-native start --max-workers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>

- 대화형 모드 비활성화:

`react-native start --no-interactive`
