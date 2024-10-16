---
layout: page
title: common/espeak (한국어)
description: "텍스트 음성 변환을 사용하여, 기본 사운드 장치를 통해 이야기."
content_hash: aafe6b6aaa7a8ec8ce51e35eddc8b45d03000efe
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/espeak.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/espeak.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/espeak.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># espeak

텍스트 음성 변환을 사용하여, 기본 사운드 장치를 통해 이야기.
더 많은 정보: <https://espeak.sourceforge.net>.

- 문구를 큰 소리로 이야기:

`espeak "I like to ride my bike."`

- 파일을 소리내어 말하기:

`espeak -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 출력을 직접 말하지 않고, WAV 오디오 파일로 저장:

`espeak -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.wav</span>` "It's GNU plus Linux"`

- 다른 목소리를 사용:

`espeak -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">음성</span>
