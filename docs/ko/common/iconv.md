---
layout: page
title: common/iconv (한국어)
description: "한 인코딩에서 다른 인코딩으로 텍스트를 변환."
content_hash: 4b662935e8ae6d87ef3ab6aa41642e24dd83c07a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/iconv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iconv

한 인코딩에서 다른 인코딩으로 텍스트를 변환.
더 많은 정보: <https://manned.org/iconv>.

- 파일을 특정 인코딩으로 변환하고, `stdout`으로 출력:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_인코딩</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">특정_인코딩</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 파일을 현재 로케일의 인코딩으로 변환하고, 파일로 출력:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_인코딩</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- 지원되는 인코딩 나열:

`iconv -l`
