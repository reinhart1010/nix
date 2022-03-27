---
layout: page
title: osx/sips (中文)
description: "苹果的处理文件脚本系统。"
content_hash: ca3df8e43b7a0c30ade226b21e884c9fb7a987d8
related_topics:
  - title: English version
    url: /en/osx/sips.html
    icon: bi bi-globe
---
# sips

苹果的处理文件脚本系统。
光栅 / 查询图像 和 颜色同步 ICC 配置文件。

- S 指定一个输出目录，这样原始文件就不会被修改：

`sips --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标 / 文件夹 / 输出文件夹</span>

- 以指定的大小对图像重新采样，图像纵横比可能会更改：

`sips -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图片文件。扩展名</span>

- 对图像重新取样，使高度和宽度不大于指定的大小（注意大写 Z）：

`sips -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图片文件。扩展名</span>

- 对目录中的所有图像重新取样，以适应 960px 的宽度（保持纵横比）：

`sips --resampleWidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">960</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标 / 文件夹 / 所有图片文件</span>

- 将图像从 CMYK 转换为 RGB：

`sips --matchTo '/System/Library/ColorSync/Profiles/Generic RGB Profile.icc' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标 / 文件夹 / 图片。扩展</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标 / 文件夹 / 输出文件夹</span>

- 从图像中删除 ColorSync ICC 配置：

`sips -d profile --deleteColorManagementProperties `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标 / 文件夹 / 图片。扩展</span>
