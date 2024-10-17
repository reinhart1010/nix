---
layout: page
title: common/exiftool (한국어)
description: "파일의 메타 정보를 읽고 쓰기."
content_hash: 67d3bcd0465dc204abc659facb2968f7a18a298e
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/exiftool.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exiftool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exiftool

파일의 메타 정보를 읽고 쓰기.
더 많은 정보: <https://exiftool.org>.

- 특정 파일에 대한 EXIF 메타데이터를 출력 :

`exiftool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 파일에서 모든 EXIF 메타데이터를 제거 :

`exiftool -All= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 지정된 이미지 파일에서 GPS EXIF 메타데이터를 제거:

`exiftool "-gps*=" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1 경로/대상/이미지2 ...</span>

- 지정된 이미지 파일에서 모든 EXIF 메타데이터를 제거한 다음, 색상 및 방향에 대한 메타데이터를 다시 추가:

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1 경로/대상/이미지2 ...</span>

- 디렉터리의 모든 사진을 찍은 날짜를 1시간 앞으로 이동:

`exiftool "-AllDates+=0:0:0 1:0:0" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 현재 디렉토리의 모든 JPEG 사진을 촬영한 날짜를 1일 2시간 뒤로 이동:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- 백업을 유지하지 않고, `DateTimeOriginal` 필드에서 1.5 시간을 뺀 값만 변경:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- `DateTimeOriginal` 필드를 기반으로 디렉토리에 있는 모든 JPEG 사진의 이름을 반복적으로 변경:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` -r -ext jpg`
