---
layout: page
title: common/lmms (한국어)
description: "무료, 오픈 소스, 크로스 플랫폼 디지털 오디오 워크스테이션."
content_hash: 5bce859b7c132144c3ca363a3672781ae5abab79
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lmms.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lmms.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lmms

무료, 오픈 소스, 크로스 플랫폼 디지털 오디오 워크스테이션.
`.mmp` 또는 `.mmpz` 프로젝트 파일을 렌더링하거나, `.mmpz`를 XML로 덤프하거나, GUI를 시작할 수 있습니다.
같이 보기: `mixxx`.
더 많은 정보: <https://lmms.io>.

- GUI 시작:

`lmms`

- GUI 시작 및 외부 구성 파일 로드:

`lmms --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.xml</span>

- GUI 시작 및 MIDI 또는 Hydrogen 파일 가져오기:

`lmms --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/midi/또는/hydrogen/파일</span>

- 지정된 창 크기로 GUI 시작:

`lmms --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_크기</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_크기</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_오프셋</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_오프셋</span>

- `.mmpz` 파일 덤프:

`lmms dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/mmpz/파일.mmpz</span>

- 프로젝트 파일 렌더링:

`lmms render `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/mmpz_또는_mmp/파일</span>

- 프로젝트 파일의 개별 트랙 렌더링:

`lmms rendertracks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/mmpz_또는_mmp/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/덤프/폴더</span>

- 사용자 지정 샘플레이트, 포맷으로 루프 렌더링:

`lmms render --samplerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">88200</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ogg</span>` --loop --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력/파일.ogg</span>
