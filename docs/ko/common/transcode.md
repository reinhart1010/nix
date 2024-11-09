---
layout: page
title: common/transcode (한국어)
description: "비디오 및 오디오 코덱을 변환하고 미디어 형식을 변환하는 도구."
content_hash: c361f054d36e74dde5d5ed394eca64014af89d4e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/transcode.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transcode.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transcode

비디오 및 오디오 코덱을 변환하고 미디어 형식을 변환하는 도구.
더 많은 정보: <https://manned.org/transcode>.

- 카메라 흔들림 제거를 위한 안정화 파일 생성:

`transcode -J stabilize -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 안정화 파일 생성 후 카메라 흔들림 제거, XviD를 사용하여 비디오 변환:

`transcode -J transform -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` -y xvid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- 비디오 크기를 640x480 픽셀로 조정하고 XviD를 사용하여 MPEG4 코덱으로 변환:

`transcode -Z 640x480 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` -y xvid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>
