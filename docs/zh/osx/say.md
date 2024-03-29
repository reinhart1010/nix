---
layout: page
title: osx/say (中文)
description: "将文本转换为语音。"
content_hash: 0f909f9b6b9158bfee2ace55fede192957a048f4
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/say.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/say.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/say.html
    icon: bi bi-globe
tldri18n_status: 2
---
# say

将文本转换为语音。
更多信息：<https://keith.github.io/xcode-man-pages/say.1.html>.

- 大声说出一个句子：

`say "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我喜欢骑脚踏车。</span>`"`

- 播放文本文件内容音频：

`say --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.txt</span>

- 用自定义的语音和语音速率说出一个句子：

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">语音库名</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">每分钟多少词</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">戴夫，我很抱歉，我不能让你那么干。</span>`"`

- 列出可用的语音库（不同的语音用于不同的语言）：

`say --voice="?"`

- 用波兰语说一个句子：

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zosia</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Litwo, ojczyzno moja!</span>`"`

- 创建文本的音频文件：

`say --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.aiff</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">献给疯狂的人们。</span>`"`
