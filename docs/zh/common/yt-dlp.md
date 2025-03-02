---
layout: page
title: common/yt-dlp (中文)
description: "一个具有额外功能和修复的 youtube-dl 分支。"
content_hash: 7f410ca4d677bb3767d91a4682b0aae8ece4e280
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yt-dlp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yt-dlp.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/yt-dlp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yt-dlp

一个具有额外功能和修复的 youtube-dl 分支。
从 YouTube 和其他网站下载视频。
请参阅：`yt-dlp`，`ytfzf`。
更多信息：<https://github.com/yt-dlp/yt-dlp>.

- 下载视频或播放列表（使用下面命令的默认选项）：

`yt-dlp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 列出可下载的视频格式：

`yt-dlp --list-formats "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 使用最佳 MP4 视频格式下载视频或播放列表（默认为 "bv\*+ba/b"）：

`yt-dlp --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 从视频中提取音频（需要 ffmpeg 或 ffprobe）：

`yt-dlp --extract-audio "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 指定提取音频的格式和音质（0（最佳）到 10（最差），默认值为 5）：

`yt-dlp --extract-audio --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` --audio-quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- 仅下载播放列表中的第二、第四、第五、第六和最后一项（第一项为 1，而非 0）：

`yt-dlp --playlist-items 2,4:6,-1 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA</span>`"`

- 下载 YouTube 频道/用户的所有播放列表，并将每个播放列表保存在单独的目录中：

`yt-dlp -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/user/TheLinuxFoundation/playlists</span>`"`

- 下载 Udemy 课程，并将每章保存在单独的目录中：

`yt-dlp -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>`" -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.udemy.com/java-tutorial</span>`"`
