---
layout: page
title: linux/grub-mkconfig (中文)
description: "生成GRUB配置文件。"
content_hash: 5c1b43f6146991cbb43015e3c30f2ccdbd9b5624
related_topics:
  - title: English version
    url: /en/linux/grub-mkconfig.html
    icon: bi bi-globe
---
# grub-mkconfig

生成GRUB配置文件。
更多信息：<https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- 模拟运行并打印配置到标准输出：

`sudo grub-mkconfig`

- 生成配置文件：

`sudo grub-mkconfig --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub/grub.cfg</span>

- 打印帮助页面：

`grub-mkconfig --help`
