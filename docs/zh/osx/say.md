---
layout: page
title: osx/say (中文)
description: "将文本转换为语音。"
content_hash: 201080fd7364ff5a9549c7d2b1be5b26b6fbf9bf
last_modified_at: 2023-06-13
related_topics:
  - title: English version
    url: /en/osx/say.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/say.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/say.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># say

将文本转换为语音。
更多信息：<https://ss64.com/osx/say.html>.

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
