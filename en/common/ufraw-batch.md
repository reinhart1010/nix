---
layout: page
title: common/ufraw-batch (English)
description: "Convert RAW files from cameras into standard image files."
content_hash: 72cc9564851650a8438748bcad83bca372af027e
---
# ufraw-batch

Convert RAW files from cameras into standard image files.
More information: <https://manned.org/ufraw-batch>.

- Simply convert RAW files to JPG:

`ufraw-batch --out-type=jpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>

- Simply convert RAW files to PNG:

`ufraw-batch --out-type=png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>

- Extract the preview image from the raw file:

`ufraw-batch --embedded-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>

- Save the file with size up to the given maximums MAX1 and MAX2:

`ufraw-batch --size=MAX1,MAX2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>
