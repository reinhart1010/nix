---
layout: page
title: common/vgmstream_cli (한국어)
description: "다양한 비디오 게임 오디오 포맷을 재생하고 `wav`로 변환."
content_hash: 9dc7edab567427b7190a3cfebf2de63de444bcd5
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/vgmstream_cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vgmstream_cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vgmstream_cli

다양한 비디오 게임 오디오 포맷을 재생하고 `wav`로 변환.
더 많은 정보: <https://github.com/vgmstream/vgmstream/blob/master/doc/USAGE.md>.

- `adc` 파일을 `wav`로 디코딩 (기본 출력 이름은 `input.wav`):

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.adc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.wav</span>

- 오디오를 디코딩하지 않고 메타데이터 출력:

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.adc</span>` -m`

- 루프 없이 오디오 파일 디코딩:

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.adc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.wav</span>` -i`

- 세 번의 루프로 디코딩한 후 3초 지연 및 5초 페이드아웃 추가:

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.adc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.wav</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.0</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5.0</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.0</span>

- 여러 파일을 `bgm_(원래 이름).wav`로 변환 (기본 `-o` 패턴은 `?f.wav`):

`vgmstream_cli -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bgm_?f.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.adc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.adc</span>

- 파일을 무한 반복으로 재생 (`channels`와 `rate`는 메타데이터와 일치해야 함):

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.adc</span>` -pec | aplay --format cd --channels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">44100</span>
