---
layout: page
title: common/exiv2 (한국어)
description: "이미지 메타데이터 도구."
content_hash: 3454e0abcf1e04b164c50d67cab9c0458fbab9e3
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/exiv2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exiv2

이미지 메타데이터 도구.
더 많은 정보: <https://www.exiv2.org/manpage.html>.

- 이미지 Exif 메타데이터 요약을 출력:

`exiv2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 해석된 값으로 모든 메타데이터 (Exif, IPTC, XMP)를 출력:

`exiv2 -P kt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 윈시 값으로 모든 메타데이터를 출력:

`exiv2 -P kv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이미지에서 모든 메타데이터를 삭제:

`exiv2 -d a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 타임스탬프를 유지하면서, 모든 메타데이터를 삭제:

`exiv2 -d a -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 메타데이터(파일 타임스탬프가 아님)의 날짜와 시간을 앞에 추가하여 파일 이름을 변경:

`exiv2 -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'%Y%m%d_%H%M%S_:basename:'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
