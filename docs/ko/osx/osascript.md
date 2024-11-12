---
layout: page
title: osx/osascript (한국어)
description: "AppleScript 또는 JavaScript for Automation (JXA) 실행."
content_hash: e01f8b8c8a2fd37f2494ed9a2ed077798de0fd76
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/osascript.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/osascript.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/osascript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/osascript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# osascript

AppleScript 또는 JavaScript for Automation (JXA) 실행.
더 많은 정보: <https://keith.github.io/xcode-man-pages/osascript.1.html>.

- AppleScript 명령 실행:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello world'</span>`"`

- 여러 AppleScript 명령 실행:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello'</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'world'</span>`"`

- 컴파일된(`*.scpt`), 번들(`*.scptd`), 또는 텍스트(`*.applescript`) 형식의 AppleScript 파일 실행:

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/apple.scpt</span>

- 애플리케이션의 번들 식별자 얻기 (`open -b`에 유용):

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`"'`

- JavaScript 명령 실행:

`osascript -l JavaScript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log('Hello world');</span>`"`

- JavaScript 파일 실행:

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/script.js</span>
