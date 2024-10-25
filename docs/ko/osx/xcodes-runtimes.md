---
layout: page
title: osx/xcodes-runtimes (한국어)
description: "Xcode 시뮬레이터 런타임 관리."
content_hash: 22dedfb0e0231757b368adeb79c313a41b988dc0
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes-runtimes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcodes runtimes

Xcode 시뮬레이터 런타임 관리.
더 많은 정보: <https://github.com/xcodesorg/xcodes>.

- 사용 가능한 모든 시뮬레이터 런타임 표시:

`xcodes runtimes --include-betas`

- 시뮬레이터 런타임 다운로드:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_이름</span>

- 시뮬레이터 런타임 다운로드 및 설치:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_이름</span>

- 특정 iOS/watchOS/tvOS/visionOS 버전의 시뮬레이터 런타임 다운로드/설치 (대소문자 구분하여 작성해야 함):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iOS|watchOS|tvOS|visionOS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_버전</span>`"`

- 런타임 아카이브를 처음 다운로드할 위치 설정 (기본값은 `~/Downloads`):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_이름</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 시뮬레이터가 성공적으로 설치된 후에도 다운로드한 아카이브 삭제하지 않기:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임_이름</span>` --keep-archive`
