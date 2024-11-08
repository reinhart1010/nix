---
layout: page
title: common/piper (한국어)
description: "빠르고 로컬에서 동작하는 신경망 기반의 텍스트 음성 변환 시스템."
content_hash: b05f62f04b2139dbc7342a2d21637ff1d1697e59
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/piper.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/piper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# piper

빠르고 로컬에서 동작하는 신경망 기반의 텍스트 음성 변환 시스템.
<https://rhasspy.github.io/piper-samples>에서 음성 모델을 시도해보고 다운로드하세요.
더 많은 정보: <https://github.com/rhasspy/piper>.

- 텍스트 음성 변환 [m]모델을 사용하여 WAV [f]파일 출력(모델 경로에 대한 config 파일이 있을 경우):

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">말할 내용</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/모델.onnx</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력파일.wav</span>

- [m]모델과 JSON [c]설정 파일을 지정하여 WAV [f]파일 출력:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'말할 내용'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/모델.onnx</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/모델.onnx.json</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력파일.wav</span>

- 여러 명의 화자가 있는 음성에서 특정 화자를 ID 번호로 선택:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Warum?'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de_DE-thorsten_emotional-medium.onnx</span>` --speaker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">화남.wav</span>

- mpv 미디어 플레이어로 출력을 스트리밍:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Hello world'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_GB-northern_english_male-medium.onnx</span>` --output-raw -f - | mpv -`

- 두 배 빠르게 말하고 문장 사이에 큰 간격을 두기:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'두 배 속도로 말합니다. 드라마틱하게!'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.onnx</span>` --length_scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` --sentence_silence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라마.wav</span>
