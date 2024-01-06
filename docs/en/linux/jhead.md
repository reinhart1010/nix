---
layout: page
title: linux/jhead (English)
description: "Image timestamp and EXIF data manipulation."
content_hash: 075b8b4827de4ea5bb520bf216245ac11b273e5d
last_modified_at: 2024-01-06
related_topics:
  - title: Deutsch version
    url: /de/linux/jhead.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jhead

Image timestamp and EXIF data manipulation.
More information: <https://www.sentex.net/~mwandel/jhead/usage.html>.

- Show all EXIF data:

`jhead `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Set the file's date and time to the EXIF create date (file creation date will be changed):

`jhead -ft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Set the EXIF time to the file's date and time (EXIF data will be changed):

`jhead -dsft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Rename all JPEG files based on the EXIF create date to `YYYY_MM_DD-HH_MM_SS.jpg`:

`jhead -n%Y_%m_%d-%H_%M_%S *.jpg`

- Rotate losslessly all JPEG images by 90, 180 or 270 based on the EXIF orientation tag:

`jhead -autorot *.jpg`

- Update all EXIF timestamps (Format: +- hour:minute:seconds) (example: forgot to change the camera's time zone - removing 1 hour from timestamps):

`jhead -ta-1:00:00 *.jpg`

- Remove all EXIF data (including thumbnails):

`jhead -purejpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>
