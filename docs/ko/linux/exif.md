---
layout: page
title: linux/exif (한국어)
description: "JPEG 파일의 EXIF 정보를 표시하고 변경."
content_hash: cbff64c9d220fef0cf969e04e892311885b2c002
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/exif.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/exif.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exif

JPEG 파일의 EXIF 정보를 표시하고 변경.
더 많은 정보: <https://github.com/libexif/exif/>.

- 이미지에서 인식된 모든 EXIF 정보 표시:

`exif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>

- 이미지에 존재하는지 여부와 함께 알려진 EXIF 태그 목록을 표로 표시:

`exif --list-tags --no-fixup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.jpg</span>

- 이미지 썸네일을 `thumbnail.jpg` 파일로 추출:

`exif --extract-thumbnail --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thumbnail.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.jpg</span>

- 주어진 이미지에서 "Model" 태그의 원시 내용 표시:

`exif --ifd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --tag=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Model</span>` --machine-readable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.jpg</span>

- "Artist" 태그의 값을 John Smith로 변경하고 `new.jpg`로 저장:

`exif --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new.jpg</span>` --ifd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --tag="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Artist</span>`" --set-value="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">John Smith</span>`" --no-fixup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.jpg</span>
