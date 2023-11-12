---
layout: page
title: linux/cam (English)
description: "Frontend tool for `libcamera`."
content_hash: 879bc612e833daffa4c5c28cdff454590f4639f4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cam

Frontend tool for `libcamera`.
More information: <https://libcamera.org/docs.html>.

- List available cameras:

`cam --list`

- List controls of a camera:

`cam --camera `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camera_index</span>` --list-controls`

- Write frames to a folder:

`cam --camera `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camera_index</span>` --capture=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frames_to_capture</span>` --file`

- Display camera feed in a window:

`cam --camera `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camera_index</span>` --capture --sdl`
