---
layout: page
title: common/waifu2x-ncnn-vulkan (English)
description: "Image upscaler for manga/anime-style images using NCNN neural network framework."
content_hash: 0c4e1a28987285e142af2be722495f7778edee7c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# waifu2x-ncnn-vulkan

Image upscaler for manga/anime-style images using NCNN neural network framework.
More information: <https://github.com/nihui/waifu2x-ncnn-vulkan>.

- Upscale an image:

`waifu2x-ncnn-vulkan -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Upscale an image by a custom scale factor and denoise it:

`waifu2x-ncnn-vulkan -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|4|8|16|32</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|0|1|2|3</span>

- Save the upscaled image in a specific format:

`waifu2x-ncnn-vulkan -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jpg|png|webp</span>
