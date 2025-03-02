---
layout: page
title: common/yuvsplittoppm (中文)
description: "将三个抽样的 Abekas YUV 文件转换为一个 PPM 图像。"
content_hash: 32b287c41603922334a167784efe2a1bbcd1b408
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yuvsplittoppm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yuvsplittoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yuvsplittoppm

将三个抽样的 Abekas YUV 文件转换为一个 PPM 图像。
更多信息：<https://netpbm.sourceforge.net/doc/yuvsplittoppm.html>.

- 从以基名开始的三个文件中读取 Akebas YUV 字节，将它们合并为一个单一的 PPM 图像，并将其存储到指定的输出文件中：

`yuvsplittoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">基名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">宽度</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">高度</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出_文件.ppm</span>
