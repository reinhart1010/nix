---
layout: page
title: linux/wodim (한국어)
description: "CD 또는 DVD에 데이터를 기록하는 명령어(일부 시스템에서는 `cdrecord`로 별칭됨)."
content_hash: f5229418b75523d466e70a807f9d8d709b457765
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wodim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wodim

CD 또는 DVD에 데이터를 기록하는 명령어(일부 시스템에서는 `cdrecord`로 별칭됨).
wodim의 일부 사용은 디스크의 모든 데이터를 지우는 등의 파괴적 작업을 수행할 수 있습니다.
더 많은 정보: <https://manned.org/wodim>.

- `wodim`에서 사용할 수 있는 광학 드라이브 표시:

`wodim --devices`

- 오디오 전용 디스크 기록(굽기):

`wodim dev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/optical_drive</span>` -audio `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">track*.cdaudio</span>

- 파일을 디스크에 굽고 완료 시 디스크 배출(일부 레코더는 이 작업이 필요함):

`wodim -eject dev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/optical_drive</span>` -data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.iso</span>

- 광학 드라이브에 파일을 굽고, 연속적으로 여러 디스크에 기록할 수 있음:

`wodim -tao dev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/optical_drive</span>` -data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.iso</span>
