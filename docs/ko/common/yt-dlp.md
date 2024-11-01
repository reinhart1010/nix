---
layout: page
title: common/yt-dlp (한국어)
description: "추가 기능과 수정이 포함된 youtube-dl 포크."
content_hash: 29546c520570a38cded24277c3ad0ddba52fba87
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yt-dlp.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/yt-dlp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yt-dlp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yt-dlp

추가 기능과 수정이 포함된 youtube-dl 포크.
YouTube 및 기타 웹사이트에서 동영상을 다운로드합니다.
같이 보기: `yt-dlp`, `ytfzf`.
더 많은 정보: <https://github.com/yt-dlp/yt-dlp>.

- 동영상 또는 재생목록 다운로드 (아래 명령의 기본 옵션 사용):

`yt-dlp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 동영상의 다운로드 가능한 형식 나열:

`yt-dlp --list-formats "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 사용 가능한 최고의 MP4 비디오로 동영상 또는 재생목록 다운로드 (기본은 "bv*+ba/b"):

`yt-dlp --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 동영상에서 오디오 추출 (ffmpeg 또는 ffprobe 필요):

`yt-dlp --extract-audio "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 추출된 오디오의 형식과 품질 지정 (0 (최고)에서 10 (최악) 사이, 기본값 = 5):

`yt-dlp --extract-audio --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` --audio-quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- YouTube 채널/사용자의 모든 재생목록을 각각의 폴더에 저장하여 다운로드:

`yt-dlp -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/user/TheLinuxFoundation/playlists</span>`"`

- Udemy 강의를 각 챕터별로 다른 폴더에 저장하여 다운로드:

`yt-dlp -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`" -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.udemy.com/java-tutorial</span>`"`
