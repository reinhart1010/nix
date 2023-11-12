---
layout: page
title: linux/v4l2-ctl (English)
description: "Control video devices."
content_hash: 87e8f4a34f943bb76720fc44e7f1c9c1952d3d0f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# v4l2-ctl

Control video devices.
More information: <https://manned.org/v4l2-ctl>.

- List all video devices:

`v4l2-ctl --list-devices`

- List supported video formats and resolutions of default video device `/dev/video0`:

`v4l2-ctl --list-formats-ext`

- List supported video formats and resolutions of a specific video device:

`v4l2-ctl --list-formats-ext --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video_device</span>

- Get all details of a video device:

`v4l2-ctl --all --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video_device</span>

- Capture a JPEG photo with a specific resolution from video device:

`v4l2-ctl --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video_device</span>` --set-fmt-video=width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`,height=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>`,pixelformat=MJPG --stream-mmap --stream-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.jpg</span>` --stream-count=1`

- Capture a raw video stream from video device:

`v4l2-ctl --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video_device</span>` --set-fmt-video=width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`,height=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>`,pixelformat=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` --stream-mmap --stream-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>` --stream-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_frames_to_capture</span>

- List all video device's controls and their values:

`v4l2-ctl --list-ctrls --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video_device</span>

- Set the value of a video device control:

`v4l2-ctl --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video_device</span>` --set-ctrl=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">control_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
