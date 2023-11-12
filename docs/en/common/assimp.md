---
layout: page
title: common/assimp (English)
description: "Command-line client for the Open Asset Import Library."
content_hash: 2a421e907ab0736f96907d095eed75c042871ae9
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/assimp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/assimp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/assimp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/assimp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# assimp

Command-line client for the Open Asset Import Library.
Supports loading of 40+ 3D file formats, and exporting to several popular 3D formats.
More information: <https://assimp-docs.readthedocs.io/>.

- List all supported import formats:

`assimp listext`

- List all supported export formats:

`assimp listexport`

- Convert a file to one of the supported output formats, using the default parameters:

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.obj</span>

- Convert a file using custom parameters (the dox_cmd.h file in assimp's source code lists available parameters):

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.obj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameters</span>

- Display a summary of a 3D file's contents:

`assimp info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List all supported subcommands ("verbs"):

`assimp help`

- Get help on a specific subcommand (e.g. the parameters specific to it):

`assimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
