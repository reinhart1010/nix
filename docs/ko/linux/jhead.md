---
layout: page
title: linux/jhead (한국어)
description: "이미지 타임스탬프 및 EXIF 데이터 조작."
content_hash: e7e85df09537603950282e96af418cda9e87ab2e
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/linux/jhead.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/jhead.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jhead

이미지 타임스탬프 및 EXIF 데이터 조작.
더 많은 정보: <https://www.sentex.net/~mwandel/jhead/usage.html>.

- 모든 EXIF 데이터 표시:

`jhead `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- 파일의 날짜 및 시간을 EXIF 생성 날짜로 설정 (파일 생성 날짜가 변경됨):

`jhead -ft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- EXIF 시간을 파일의 날짜 및 시간으로 설정 (EXIF 데이터가 변경됨):

`jhead -dsft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- 모든 JPEG 파일을 EXIF 생성 날짜에 따라 `YYYY_MM_DD-HH_MM_SS.jpg`로 이름 변경:

`jhead -n%Y_%m_%d-%H_%M_%S *.jpg`

- 모든 JPEG 이미지를 EXIF 방향 태그에 따라 90도, 180도 또는 270도로 무손실 회전:

`jhead -autorot *.jpg`

- 모든 EXIF 타임스탬프 업데이트 (형식: +- 시간:분:초) (예: 카메라의 시간대를 변경하는 것을 잊었을 때 - 타임스탬프에서 1시간 제거):

`jhead -ta-1:00:00 *.jpg`

- 모든 EXIF 데이터 제거 (썸네일 포함):

`jhead -purejpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>
