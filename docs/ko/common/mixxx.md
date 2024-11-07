---
layout: page
title: common/mixxx (한국어)
description: "무료 및 오픈 소스 크로스 플랫폼 DJ 소프트웨어."
content_hash: 4505a82ee1e3001a5db28c9d9a2b7e9b19cd8ca5
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mixxx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mixxx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mixxx

무료 및 오픈 소스 크로스 플랫폼 DJ 소프트웨어.
같이 보기: `lmms`.
더 많은 정보: <https://mixxx.org/manual/latest/chapters/appendix.html#command-line-options>.

- Mixxx GUI를 전체 화면으로 시작:

`mixxx --fullScreen`

- 안전한 개발자 모드에서 시작하여 충돌 디버그:

`mixxx --developer --safeMode`

- 오작동 디버그:

`mixxx --debugAssertBreak --developer --loglevel trace`

- 지정된 설정 파일을 사용하여 Mixxx 시작:

`mixxx --resourcePath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mixxx/res/controllers</span>` --settingsPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정-파일</span>

- 사용자 정의 컨트롤러 매핑 디버그:

`mixxx --controllerDebug --resourcePath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매핑-폴더</span>

- 도움말 표시:

`mixxx --help`
