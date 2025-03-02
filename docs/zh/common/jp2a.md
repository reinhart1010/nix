---
layout: page
title: common/jp2a (中文)
description: "将 JPEG 图像转换为 ASCII。"
content_hash: aa7e7c9bf5be60fc786a8a494871ffd318542b86
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jp2a.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jp2a.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jp2a

将 JPEG 图像转换为 ASCII。
更多信息：<https://csl.name/jp2a/>.

- 从文件中读取 JPEG 图像并以 ASCII 显示：

`jp2a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.jpeg</span>

- 从 URL 中读取 JPEG 图像并以 ASCII 显示：

`jp2a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/image.jpeg</span>

- 对 ASCII 输出进行着色：

`jp2a --colors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.jpeg</span>

- 指定用于 ASCII 输出的字符：

`jp2a --chars='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">..-ooxx@@</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.jpeg</span>

- 将 ASCII 输出写入一个文件：

`jp2a --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/output_file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.jpeg</span>

- 以 HTML 文件格式写入 ASCII 输出，适合在网页浏览器中查看：

`jp2a --html --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/output_file.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/image.jpeg</span>
