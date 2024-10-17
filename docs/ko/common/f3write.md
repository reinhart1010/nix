---
layout: page
title: common/f3write (한국어)
description: "실제 용량을 테스트하려면, 드라이브를 .h2w 파일로 채우기."
content_hash: 1fd1c2ee36433f2cf3a6e21f7441fc552853fceb
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/f3write.html
    icon: bi bi-globe
tldri18n_status: 2
---
# f3write

실제 용량을 테스트하려면, 드라이브를 .h2w 파일로 채우기.
참고: `f3read`, `f3probe`, `f3fix`.
더 많은 정보: <https://oss.digirati.com.br/f3/>.

- 지정된 디렉터리에 테스트 파일을 작성하여 드라이브를 채움:

`f3write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 쓰기 속도 제한을 둠:

`f3write --max-write-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초당_kb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>
