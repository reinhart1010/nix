---
layout: page
title: osx/say (中文)
description: "将文本转换为语音。"
content_hash: 1e37e888cd7aa5f76ec01693b4ff258e459fa1ec
related_topics:
  - title: English version
    url: /en/osx/say.html
    icon: bi bi-globe
---
# say

将文本转换为语音。
更多信息：<https://ss64.com/osx/say.html>.

- 大声说出一个句子：

`say "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">你好，世界！</span>`"`

- 播放文本文件内容音频：

`say -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.txt</span>

- 用自定义的语音和语音速率说出一个句子：

`say -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">语音库名</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">每分钟多少词</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">你好，我可以说中文.</span>`"`

- 列出可用的语音库：

`say --voice="?"`

- 创建文本的音频文件：

`say -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.aiff</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">你好，请将录音内容输出到文件.</span>`"`
