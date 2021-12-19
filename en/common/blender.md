---
layout: page
title: common/blender (English)
description: "Command-line interface to the Blender 3D computer graphics application."
content_hash: 08b5f8cceb62c27cb7de9802a0633e2110e7f8a4
related_topics:
  - title: italiano version
    url: /it/common/blender.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/blender.html
    icon: bi bi-globe
---
# blender

Command-line interface to the Blender 3D computer graphics application.
Arguments are executed in the order they are given.
More information: <https://docs.blender.org/manual/en/latest/advanced/command_line/>.

- Render all frames of an animation in the background, without loading the UI (output is saved to `/tmp`):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.blend -a`

- Render an animation using a specific image naming pattern, in a path relative (`//`) to the .blend file:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.blend -o //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">render/frame_###.png</span>` -a`

- Render the 10th frame of an animation as a single image, saved to an existing directory (absolute path):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.blend -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/output_directory</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Render the second last frame in an animation as a JPEG image, saved to an existing directory (relative path):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.blend -o //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_directory</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JPEG</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-2</span>

- Render the animation of a specific scene, starting at frame 10 and ending at frame 500:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.blend -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scene_name</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -a`

- Render an animation at a specific resolution, by passing a Python expression:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.blend --python-expr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import bpy; bpy.data.scenes[0].render.resolution_percentage = 25</span>`' -a`

- Start an interactive Blender session in the terminal with a python console (do `import bpy` after starting):

`blender -b --python-console`
