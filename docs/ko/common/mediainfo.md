---
layout: page
title: common/mediainfo (한국어)
description: "비디오 및 오디오 파일의 메타데이터 표시."
content_hash: 0408b37a1c2fe6e072b235f0b9e91b55f9929a28
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mediainfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mediainfo

비디오 및 오디오 파일의 메타데이터 표시.
더 많은 정보: <https://mediaarea.net/MediaInfo>.

- 주어진 파일의 메타데이터를 콘솔에 표시:

`mediainfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 콘솔에 표시하면서 출력 결과를 주어진 파일에 저장:

`mediainfo --Logfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 추출할 수 있는 메타데이터 속성 나열:

`mediainfo --Info-Parameters`
