---
layout: page
title: common/flutter-pub (한국어)
description: "Flutter 패키지 매니저."
content_hash: 82ec7d64e7863dd6c961c037ddae8098e9046b4e
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/flutter-pub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flutter pub

Flutter 패키지 매니저.
참고: 패키지는 <https://pub.dev>에서 사용 가능. 참조: `flutter`.
더 많은 정보: <https://docs.flutter.dev/packages-and-plugins/using-packages>.

- `pubspec.yaml`에 지정된 모든 패키지를 다운로드/업데이트:

`flutter pub get`

- 앱에 패키지 종속성을 추가:

`flutter pub add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 앱에 패키지 종속성을 제거:

`flutter pub remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- `pubspec.yaml`에서 허용하는 가장 높은 버전의 패키지로 업그레이드:

`flutter pub upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
