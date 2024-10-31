---
layout: page
title: common/handbrakecli (한국어)
description: "HandBrake 비디오 변환 및 DVD 리핑 도구에 대한 명령줄 인터페이스."
content_hash: 77a99671460b2a74368e308394ff24e44e4a8095
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/handbrakecli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# handbrakecli

HandBrake 비디오 변환 및 DVD 리핑 도구에 대한 명령줄 인터페이스.
더 많은 정보: <https://handbrake.fr/>.

- 비디오 파일을 MKV(AAC 160kbit 오디오 및 x264 CRF20 비디오)로 변환:

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.avi</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.mkv</span>` --encoder x264 --quality 20 --ab 160`

- 비디오 파일 크기를 320x240으로 조정:

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mp4</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.mp4</span>` --width 320 --height 240`

- 사용 가능한 사전 설정 목록:

`handbrakecli --preset-list`

- Android 사전 설정을 사용하여 AVI 비디오를 MP4로 변환:

`handbrakecli --preset="Android" --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.ext</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.mp4</span>

- DVD 내용을 출력하고 그 과정에서 CSS 키를 가져옴:

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sr0</span>` --title 0`

- 지정된 장치에서 DVD의 첫 번째 트랙을 추출. 오디오트랙과 자막 언어는 목록으로 지정됨:

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sr0</span>` --title 1 --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.mkv</span>` --format av_mkv --encoder x264 --subtitle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,5</span>` --audio `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2</span>` --aencoder copy --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">23</span>
