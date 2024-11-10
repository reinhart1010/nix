---
layout: page
title: linux/unix2mac (한국어)
description: "Unix 스타일의 줄 끝을 macOS 스타일로 변경."
content_hash: 553109c7b24e2f385c169f8ebb1da0eb28ad5992
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/unix2mac.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/unix2mac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/unix2mac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2mac

Unix 스타일의 줄 끝을 macOS 스타일로 변경.
LF를 CR로 대체.
같이 보기: `unix2dos`, `dos2unix`, `mac2unix`.
더 많은 정보: <https://manned.org/unix2mac>.

- 파일의 줄 끝을 변경:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- macOS 스타일의 줄 끝을 가진 복사본 생성:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_파일</span>

- 파일 정보 표시:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 바이트 순서 표식 유지/추가/제거:

`unix2mac --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
