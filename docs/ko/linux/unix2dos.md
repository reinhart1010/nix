---
layout: page
title: linux/unix2dos (한국어)
description: "Unix 스타일 줄 끝을 DOS 스타일로 변경."
content_hash: 36358f314b6d9fe02d8d8ada7adac57c5cf36cc0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/unix2dos.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/unix2dos.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/unix2dos.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2dos

Unix 스타일 줄 끝을 DOS 스타일로 변경.
LF를 CRLF로 대체.
같이 보기: `unix2mac`, `dos2unix`, `mac2unix`.
더 많은 정보: <https://manned.org/unix2dos>.

- 파일의 줄 끝 변경:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- DOS 스타일 줄 끝으로 복사본 생성:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_파일</span>

- 파일 정보 표시:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 바이트 순서 표시(Byte Order Mark) 유지/추가/제거:

`unix2dos --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
