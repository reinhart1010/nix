---
layout: page
title: common/binwalk (中文)
description: "固件分析工具。"
content_hash: 74439acbb4253bf3cf8a3b262906df957c98a4bf
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/binwalk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/binwalk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/binwalk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# binwalk

固件分析工具。
更多信息：<https://github.com/ReFirmLabs/binwalk>.

- 扫描一个二进制文件：

`binwalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 解压一个二进制文件并指定输出目录：

`binwalk --extract --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 递归解压一个二进制文件并限制递归深度为 2：

`binwalk --extract --matryoshka --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 解压一个二进制文件并指定文件签名：

`binwalk --dd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png image:png</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 分析一个二进制文件的熵，用与文件相同的名字和 `.png` 后缀保存绘图：

`binwalk --entropy --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>

- 在单条命令中组合熵、签名和操作码分析：

`binwalk --entropy --signature --opcodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">二进制文件</span>
