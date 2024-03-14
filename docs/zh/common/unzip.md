---
layout: page
title: common/unzip (中文)
description: "从 Zip 压缩包中提取文件或目录。"
content_hash: 252c9b5d4412153b4e4bb44634b53f19442def1e
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/unzip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unzip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unzip

从 Zip 压缩包中提取文件或目录。
参见：`zip`.
更多信息：<https://manned.org/unzip>.

- 将指定压缩包中的所有文件和目录提取到当前目录下：

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件1.zip 路径/到/压缩文件2.zip ...</span>

- 将压缩包中的所有文件和目录提取到指定目录下：

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件1.zip 路径/到/压缩文件2.zip ...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出目录</span>

- 将压缩包中的文件和目录提取到 `stdout`（标准输出）中：

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件1.zip 路径/到/压缩文件2.zip ...</span>

- 提取文件内容及文件名到 `stdout`（标准输出）中：

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件1.zip 路径/到/压缩文件2.zip ...</span>

- 在不进行解压缩的情况下，列出指定压缩包中的内容：

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件.zip</span>

- 从指定压缩包中提取特定文件：

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>
