---
layout: page
title: linux/xwinwrap (한국어)
description: "플레이어나 프로그램을 데스크탑 배경으로 실행."
content_hash: d90bc19ba884800aadb35051f362b619694fbb7d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/xwinwrap.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/xwinwrap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xwinwrap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xwinwrap

플레이어나 프로그램을 데스크탑 배경으로 실행.
더 많은 정보: <https://github.com/ujjwal96/xwinwrap>.

- mpv를 사용하여 비디오 실행:

`xwinwrap -b -nf -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오.mp4</span>

- mpv를 사용하여 전체 화면으로 비디오 실행:

`xwinwrap -b -nf -fs -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오.mp4</span>

- mpv를 사용하여 80% 투명도로 비디오 실행:

`xwinwrap -b -nf -ov -o 0.8 --- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오.mp4</span>

- mpv를 사용하여 두 번째 모니터에 1600x900 크기로 X축 1920 오프셋으로 비디오 실행:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오.mkv</span>
