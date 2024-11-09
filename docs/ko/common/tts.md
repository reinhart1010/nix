---
layout: page
title: common/tts (한국어)
description: "음성을 합성합니다."
content_hash: 6ca474307d959c41ea7cf9b29da4140d72ceb6aa
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tts.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tts.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tts

음성을 합성합니다.
더 많은 정보: <https://github.com/coqui-ai/TTS#command-line-tts>.

- 기본 모델로 텍스트를 음성으로 변환하고 출력을 "tts_output.wav"에 저장:

`tts --text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`"`

- 제공된 모델 나열:

`tts --list_models`

- 인덱스로 모델 정보 조회:

`tts --model_info_by_idx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델_타입/모델_조회_인덱스</span>

- 이름으로 모델 정보 조회:

`tts --model_info_by_name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델_타입/언어/데이터셋/모델_이름</span>

- 기본 보코더 모델로 텍스트를 음성으로 변환:

`tts --text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`" --model_name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델_타입/언어/데이터셋/모델_이름</span>

- 사용자 정의 텍스트 음성 변환 모델 실행 (Griffin-Lim 보코더 사용):

`tts --text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`" --model_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/모델.pth</span>` --config_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정.json</span>` --out_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>
