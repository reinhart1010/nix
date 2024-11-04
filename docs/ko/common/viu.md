---
layout: page
title: common/viu (한국어)
description: "터미널에서 이미지를 보기."
content_hash: 6155b13b8ff77f52c77180fc8b31188b8d042c74
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/viu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# viu

터미널에서 이미지를 보기.
더 많은 정보: <https://github.com/atanunq/viu>.

- 이미지 또는 애니메이션 GIF 렌더링:

`viu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `curl`을 사용하여 인터넷에서 이미지 또는 GIF 렌더링:

`curl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/image.png</span>` | viu -`

- 투명한 배경의 이미지 렌더링:

`viu -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 픽셀 너비와 높이로 이미지 렌더링:

`viu -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이미지 또는 GIF를 렌더링하고 파일 이름 표시:

`viu -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
