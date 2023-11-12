---
layout: page
title: linux/beep (中文)
description: "让电脑扬声器发出哔哔声的实用程序。"
content_hash: f6216c9ecc0c52840f255aec37b00a58d5f9383d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/beep.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/beep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/beep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/beep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# beep

让电脑扬声器发出哔哔声的实用程序。
更多信息：<https://github.com/spkr-beep/beep>.

- 播放哔哔声：

`beep`

- 重复播放哔哔声：

`beep -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">重复次数</span>

- 指定频率（Hz）和持续时间（毫秒）播放哔哔声：

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">频率</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">持续时间</span>

- 将每个新的频率和持续时间作为单独的哔哔声播放：

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">频率</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">持续时间</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">频率</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">持续时间</span>

- 播放 C 大调：

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">262</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">294</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">330</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">349</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">392</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">440</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">494</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">523</span>
