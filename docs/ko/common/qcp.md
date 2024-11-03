---
layout: page
title: common/qcp (한국어)
description: "기본 텍스트 편집기를 사용하여 파일 이름을 정의하면서 파일을 복사."
content_hash: 1ff4f765c0a86e020977ed5daf07f12250baa033
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/qcp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qcp

기본 텍스트 편집기를 사용하여 파일 이름을 정의하면서 파일을 복사.
더 많은 정보: <https://www.nongnu.org/renameutils/>.

- 단일 파일 복사 (편집기에서 왼쪽에 소스 파일 이름, 오른쪽에 대상 파일 이름이 나타남):

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일</span>

- 여러 JPEG 파일 복사:

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- 파일 복사 시 편집기에서 소스와 대상 파일 이름의 위치를 바꿈:

`qcp --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>
