---
layout: page
title: linux/aplay (中文)
description: "ALSA 声卡驱动程序的命令行声音播放器。"
content_hash: 70285c1aa9771cd499c66b2b3c34bc6438278cfc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/aplay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aplay.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aplay

ALSA 声卡驱动程序的命令行声音播放器。
更多信息：<https://manned.org/aplay>.

- 播放一个文件（会自动根据文件格式确定采样率、位深等）：

`aplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 以 2500 Hz 播放指定文件的前 10 秒：

`aplay --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 以 22050 Hz，mono，8-bit，Mu-Law 和 `.au` 格式来播放指定原始文件：

`aplay --channels=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --file-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22050</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mu_law</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>
