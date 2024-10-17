---
layout: page
title: common/fastlane (한국어)
description: "모바일 애플리케이션 구축 및 출시."
content_hash: 37b5ed9cae5eed054418c723717f484874d341aa
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/fastlane.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastlane

모바일 애플리케이션 구축 및 출시.
더 많은 정보: <https://docs.fastlane.tools/actions/>.

- 현재 디렉터리에서 iOS 애플리케이션을 빌드하고 서명:

`fastlane run build_app`

- 현재 디렉터리의 프로젝트에 대해 `pod install`을 실행:

`fastlane run cocoapods`

- Xcode에서 파생된 데이터 삭제:

`fastlane run clear_derived_data`

- pod의 캐시 제거:

`fastlane run clean_cocoapods_cache`
