---
layout: page
title: linux/binwalk (中文)
description: "固件分析工具。"
content_hash: 0f0b9a4e867827146e53bf3ba2e5667cec34019e
related_topics:
  - title: English version
    url: /en/linux/binwalk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/binwalk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/binwalk.html
    icon: bi bi-globe
---
# binwalk

固件分析工具。
更多信息：<https://github.com/ReFirmLabs/binwalk>.

- 扫描一个二进制文件：

`binwalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 解压一个二进制文件并指定输出目录：

`binwalk --extract --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 递归解压一个二进制文件并限制递归深度为 2:

`binwalk --extract --matryoshka --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 解压一个二进制文件并指定文件签名：

`binwalk --dd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png image:png</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 分析一个二进制文件的熵，用与文件相同的名字和 `.png` 后缀保存绘图：

`binwalk --entropy --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 在单条命令中组合熵、签名和操作码分析：

`binwalk --entropy --signature --opcodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>
