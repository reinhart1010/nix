---
layout: page
title: linux/photorec (한국어)
description: "삭제된 파일 복구 도구."
content_hash: 7e1d3f21d8eb5817f9c25f6b60df8a8a2c03f057
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/photorec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# photorec

삭제된 파일 복구 도구.
복구된 파일은 원본 디스크와 다른 디스크에 저장하는 것이 권장됩니다.
더 많은 정보: <https://www.cgsecurity.org/wiki/PhotoRec>.

- 특정 장치에서 PhotoRec 실행:

`sudo photorec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>

- 디스크 이미지(`image.dd`)에서 PhotoRec 실행:

`sudo photorec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.dd</span>
