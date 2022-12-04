---
layout: page
title: common/exiftool (English)
description: "Read and write meta information in files."
content_hash: 746ebbae240325ab36740384f2dc175edcf41a78
last_modified_at: 2022-12-04
related_topics:
  - title: italiano version
    url: /it/common/exiftool.html
    icon: bi bi-globe
---
# exiftool

Read and write meta information in files.
More information: <https://exiftool.org>.

- Print the EXIF metadata for a given file:

`exiftool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove all EXIF metadata from the given files:

`exiftool -All= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Remove GPS EXIF metadata from given image files:

`exiftool "-gps*=" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1 path/to/image2 ...</span>

- Remove all EXIF metadata from the given image files, then re-add metadata for color and orientation:

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1 image2 ...</span>

- Move the date at which all photos in a directory were taken 1 hour forward:

`exiftool "-AllDates+=0:0:0 1:0:0" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Move the date at which all JPEG photos in the current directory were taken 1 day and 2 hours backward:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Only change the `DateTimeOriginal` field subtracting 1.5 hours, without keeping backups:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Recursively rename all JPEG photos in a directory based on the `DateTimeOriginal` field:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -r -ext jpg`
