---
layout: page
title: common/crane-append (English)
description: "Push an image based on an (optional) base image."
content_hash: 62f51364ec1fb8256574c695254fb1ab23b23247
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane append

Push an image based on an (optional) base image.
Appends layers containing the contents of the provided tarballs.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>.

- Push image based on a base image:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Push image with appended layer from tarball:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--new_layer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_name1 layer_name2 ...</span>

- Push image with appended layer with new tag:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--new_tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Push resulting image to new tarball:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tarball</span>

- Use empty base image of type OCI media instead of Docker:

`crane append --oci-empty-base`

- Annotate resulting image as being based on the base image:

`crane append --set-base-image-annotations`

- Display help:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
