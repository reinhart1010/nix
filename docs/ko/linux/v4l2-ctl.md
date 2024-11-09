---
layout: page
title: linux/v4l2-ctl (한국어)
description: "비디오 장치 제어."
content_hash: ceb95eebf724fc27bf70a1fc73cf895a5f6dea6d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/v4l2-ctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/v4l2-ctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># v4l2-ctl

비디오 장치 제어.
더 많은 정보: <https://manned.org/v4l2-ctl>.

- 모든 비디오 장치 나열:

`v4l2-ctl --list-devices`

- 기본 비디오 장치 `/dev/video0`의 지원 비디오 포맷과 해상도 나열:

`v4l2-ctl --list-formats-ext`

- 특정 비디오 장치의 지원 비디오 포맷과 해상도 나열:

`v4l2-ctl --list-formats-ext --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오_장치</span>

- 비디오 장치의 모든 세부 정보 가져오기:

`v4l2-ctl --all --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오_장치</span>

- 특정 해상도로 비디오 장치에서 JPEG 사진 캡처:

`v4l2-ctl --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오_장치</span>` --set-fmt-video=width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`,height=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>`,pixelformat=MJPG --stream-mmap --stream-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.jpg</span>` --stream-count=1`

- 비디오 장치에서 원시 비디오 스트림 캡처:

`v4l2-ctl --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오_장치</span>` --set-fmt-video=width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`,height=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>`,pixelformat=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포맷</span>` --stream-mmap --stream-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>` --stream-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">캡처할_프레임_수</span>

- 모든 비디오 장치의 컨트롤과 그 값 나열:

`v4l2-ctl --list-ctrls --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오_장치</span>

- 비디오 장치 컨트롤 값 설정:

`v4l2-ctl --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오_장치</span>` --set-ctrl=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨트롤_이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
