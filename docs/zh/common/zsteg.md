---
layout: page
title: common/zsteg (中文)
description: "用于 PNG 和 BMP 文件格式的隐写术检测工具。"
content_hash: f80ae7a887d9222b57db54ddd9eff0a46b30113e
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zsteg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zsteg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zsteg

用于 PNG 和 BMP 文件格式的隐写术检测工具。
它检测 LSB 隐写术、ZLIB 压缩数据、OpenStego、Camouflage 和包含 Eratosthenes 集的 LSB。
更多信息：<https://github.com/zed-0xff/zsteg>.

- 检测 PNG 文件中的嵌入数据：

`zsteg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.png</span>

- 使用所有已知方法检测 BMP 图像中的嵌入数据：

`zsteg --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.bmp</span>

- 检测 PNG 中的嵌入数据，以垂直方式遍历像素并优先使用 MSB：

`zsteg --msb --order yx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.png</span>

- 在 BMP 图像中检测嵌入数据，指定要考虑的位：

`zsteg --bits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2,3|1-3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.bmp</span>

- 检测 PNG 文件中的嵌入数据，仅提取素数像素并反转位：

`zsteg --prime --invert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.png</span>

- 检测 BMP 图像中的嵌入数据，指定要找到的字符串的最小长度和查找模式：

`zsteg --min-str-len `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first|all|longest|none</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.bmp</span>
