---
layout: page
title: common/godot (English)
description: "An open source 2D and 3D game engine."
content_hash: 4095a8fd750e3dc719522a88336af0ce32fc4cd7
---
# godot

An open source 2D and 3D game engine.
More information: <https://godotengine.org/>.

- Run a project if the current directory contains a `project.godot` file, otherwise open the project manager:

`godot`

- Edit a project (the current directory must contain a `project.godot` file):

`godot -e`

- Open the project manager even if the current directory contains a `project.godot` file:

`godot -p`

- Export a project for a given export preset (the preset must be defined in the project):

`godot --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">preset</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_path</span>

- Execute a standalone GDScript file (the script must inherit from `SceneTree` or `MainLoop`):

`godot -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.gd</span>
