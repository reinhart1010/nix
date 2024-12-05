---
layout: page
title: linux/swaybg (한국어)
description: "Wayland 합성기용 배경화면 도구."
content_hash: fd17d5b376ebea0980333306ba3a625fefdc2169
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/linux/swaybg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swaybg

Wayland 합성기용 배경화면 도구.
더 많은 정보: <https://github.com/swaywm/swaybg/blob/master/swaybg.1.scd>.

- 배경화면을 [i]이미지로 설정:

`swaybg --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 배경화면 [m]모드 설정:

`swaybg --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stretch|fit|fill|center|tile|solid_color</span>

- 배경화면을 고정된 [c]색상으로 설정:

`swaybg --color "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#rrggbb</span>`"`
