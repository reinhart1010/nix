---
layout: page
title: common/sox (한국어)
description: "Sound eXchange: 오디오 파일을 재생, 녹음 및 변환하는 도구."
content_hash: 36d0c56c82ebe962471c0dae0ba339f15c633c19
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sox.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sox.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sox

Sound eXchange: 오디오 파일을 재생, 녹음 및 변환하는 도구.
오디오 형식은 확장자로 식별됩니다.
더 많은 정보: <https://sox.sourceforge.net>.

- 두 오디오 파일을 하나로 병합:

`sox -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_오디오1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_오디오2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_오디오</span>

- 오디오 파일을 지정된 시간으로 잘라내기:

`sox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_오디오</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_오디오</span>` trim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지속시간</span>

- 오디오 파일을 정규화 (클리핑 없이 최대 피크 수준으로 볼륨 조정):

`sox --norm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_오디오</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_오디오</span>

- 오디오 파일을 반전하여 저장:

`sox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_오디오</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_오디오</span>` reverse`

- 오디오 파일의 통계 데이터 출력:

`sox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_오디오</span>` -n stat`

- 오디오 파일의 볼륨을 2배로 증가:

`sox -v 2.0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_오디오</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_오디오</span>
