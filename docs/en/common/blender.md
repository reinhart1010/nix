---
layout: page
title: common/blender (English)
description: "Command-line interface to the Blender 3D computer graphics application."
content_hash: b9f56f48bc24c41df2c7d13de7efab738656d0c9
last_modified_at: 2022-12-06
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
More information: <https://manned.org/blender>.

- Render all frames of an animation in the background, without loading the UI (output is saved to `/tmp`):

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.blend --render-anim`

- Render an animation using a specific image naming pattern, in a path relative (`//`) to the .blend file:

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.blend --render-output //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">render/frame_###.png</span>` --render-anim`

- Render the 10th frame of an animation as a single image, saved to an existing directory (absolute path):

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.blend --render-output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/output_directory</span>` --render-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Render the second last frame in an animation as a JPEG image, saved to an existing directory (relative path):

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.blend --render-output //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_directory</span>` --render-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JPEG</span>` --render-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-2</span>

- Render the animation of a specific scene, starting at frame 10 and ending at frame 500:

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.blend --scene `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scene_name</span>` --frame-start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` --render-anim`

- Render an animation at a specific resolution, by passing a Python expression:

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.blend --python-expr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import bpy; bpy.data.scenes[0].render.resolution_percentage = 25</span>`' --render-anim`

- Start an interactive Blender session in the terminal with a python console (do `import bpy` after starting):

`blender --background --python-console`
