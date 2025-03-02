---
layout: page
title: common/jpegoptim (中文)
description: "优化 JPEG 图像。"
content_hash: 3a4b31fd2f08c134f9d8872e21839441fcf4c5ae
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jpegoptim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jpegoptim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jpegoptim

优化 JPEG 图像。
更多信息：<https://github.com/tjko/jpegoptim>.

- 优化一组 JPEG 图像，保留所有相关数据：

`jpegoptim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像N.jpeg</span>

- 优化 JPEG 图像，剥离所有非必要数据：

`jpegoptim --strip-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像N.jpeg</span>

- 强制输出图像为渐进式：

`jpegoptim --all-progressive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像N.jpeg</span>

- 强制输出图像具有固定的最大文件大小：

`jpegoptim --size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">250k</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像1.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像2.jpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像N.jpeg</span>
