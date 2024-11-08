---
layout: page
title: common/mp4box (한국어)
description: "MPEG-4 시스템 도구: 스트림을 MP4 컨테이너에 멀티플렉싱."
content_hash: fa2faf2aaa38058dd5afd6862c4bafeffe7654ea
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mp4box.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mp4box

MPEG-4 시스템 도구: 스트림을 MP4 컨테이너에 멀티플렉싱.
더 많은 정보: <https://gpac.wp.imt.fr/mp4box>.

- 기존 MP4 파일에 대한 정보 표시:

`mp4box -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- MP4 파일에 SRT 자막 파일 추가:

`mp4box -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_자막.srt</span>`:lang=eng -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mp4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.mp4</span>

- 한 파일에서 오디오와 다른 파일에서 비디오 결합:

`mp4box -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력1.mp4</span>`#audio -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력2.mp4</span>`#video `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.mp4</span>
