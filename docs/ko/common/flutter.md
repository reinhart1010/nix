---
layout: page
title: common/flutter (한국어)
description: "Google의 무료 오픈 소스 크로스 플랫폼 모바일 앱 SDK."
content_hash: f80495c4e126583a78ddc3bd13fca034845a54aa
last_modified_at: 2024-10-20
related_topics:
  - title: Deutsch version
    url: /de/common/flutter.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/flutter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/flutter.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/flutter.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flutter

Google의 무료 오픈 소스 크로스 플랫폼 모바일 앱 SDK.
`pub`과 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
더 많은 정보: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- 동일한 이름의 디렉터리에서 새로운 Flutter 프로젝트를 초기화:

`flutter create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 모든 외부 도구가 올바르게 설치되었는지 확인:

`flutter doctor`

- Flutter 채널 나열 또는 변경:

`flutter channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|beta|dev|master</span>

- 시작된 모든 에뮬레이터와 연결된 장치에서 Flutter를 실행:

`flutter run -d all`

- 프로젝트 루트의 터미널에서 테스트를 실행:

`flutter test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test/예시_테스트.dart</span>

- 대부분의 최신 스마트폰을 대상으로 하는 출시 APK를 구축:

`flutter build apk --target-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm64</span>

- 특정 명령에 대한 도움말을 표시:

`flutter help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
