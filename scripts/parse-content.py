from babel import Locale
from babel.core import UnknownLocaleError
from datetime import datetime
from filehash.filehash import FileHash
import frontmatter
import json
from os import error, mkdir, path, walk
import requests
from requests.exceptions import HTTPError
from yaml.parser import ParserError
from yaml.scanner import ScannerError

# Open the i18n-data first
i18n = json.load(open("i18n-data/data.json", "r"))
indexnow_queue = []

def get_tldr_page_directory(lang: str):
  if lang == "en":
    return "pages"
  return "pages." + lang

def get_locale(lang: str):
  try:
    return Locale.parse(lang).display_name
  except UnknownLocaleError:
    return lang

def get_translations(lang: str, page: str):
  global i18n
  hierarchy = page[:-3].split(sep="/")
  try:
    translations = list(i18n["entries"][hierarchy[0]]["pages"][hierarchy[1]]["status"])
    if lang in translations:
      translations.remove(lang)
    return translations
  except KeyError:
    return []
  
def extract_page(lang: str, page: str):
  global i18n
  global indexnow_queue
  hierarchy = page[:-3].split(sep="/")
  folder_name = get_tldr_page_directory(lang)
  source_file = "source/" + folder_name + "/" + page
  target_file = "docs/" + lang + "/" + page
  source = open(source_file, "r")
  target = open(target_file, "w+")
  current_locale = get_locale(lang)
  title = page[:-3] + " (" + current_locale + ")"
  translations = get_translations(lang, page)
  
  content = source.readlines()
  source.close()

  # Generate frontmatters
  front_matter = "---\n"
  front_matter += "layout: page\n"
  front_matter += "title: " + title + "\n"
  front_matter += "description: \"" + content[2][2:-1].replace("\"", "\\\"") + "\"\n"
  print(content[2][2:-1])
  front_matter += "content_hash: " + FileHash("sha1").hash_file(source_file) + "\n"
  front_matter += "last_modified_at: " + datetime.today().strftime("%Y-%m-%d") + "\n"

  if len(translations) > 0:
    front_matter += "related_topics:\n"
    for translation in translations:
      locale = get_locale(translation)
      front_matter += "  - title: " + locale + " version\n"
      front_matter += "    url: /" + translation + "/" + page[:-3] + ".html\n"
      front_matter += "    icon: bi bi-globe\n"
      
  front_matter += "---\n"

  try:
    isOutdated = i18n["entries"][hierarchy[0]]["pages"][hierarchy[1]]["status"][lang]
    if isOutdated == 1:
      front_matter += "\n"
      front_matter += "### Outdated Translation\n"
      front_matter += "This entry is currently considered outdated and its contents may not be up-to-date with other translations.\n"
      front_matter += "\n"
      front_matter += "Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.\n"
      front_matter += "\n"
      front_matter += "<a class=\"btn btn-primary\" href=\"{{ site.url }}/en/" + page[:-3] + ".html\">View original (English) version</a>"
      front_matter += "\n"
      front_matter += "<a class=\"btn\" href=\"https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md\">Contributing Guidelines</a>\n"
      front_matter += "\n<hr>"
  except KeyError:
    front_matter += "\n"
    front_matter += "This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.\n"
    front_matter += "\n<hr>"

  target.write(front_matter)
  target.write("".join(content).replace("{{", "`<span class=\"tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold\">").replace("}}}", "}</span>`").replace("}}", "</span>`").replace("``", "").replace("\n> ", "\n"))

  target.close()

  indexnow_queue.append(lang + "/" + page)
  print("Finished generating page for " + lang + "/" + page)

for lang in i18n["languages"]:
  if not path.exists("docs/" + lang):
    mkdir("docs/" + lang)
  
  for category in i18n["entries"]:
    if not path.exists("docs/" + lang + "/" + category):
      mkdir("docs/" + lang + "/" + category)

  
  folder_name = get_tldr_page_directory(lang)
  for page in [path.join(dp.split(sep="/")[2], f) for dp, dn, fn in walk(path.expanduser("source/" + folder_name)) for f in fn]:
    source_file = "source/" + folder_name + "/" + page
    target_file = "docs/" + lang + "/" + page

    if not path.isfile(target_file):
      extract_page(lang, page)
    else:
      try:
        current_page = frontmatter.load(target_file)
        content_hash = FileHash("sha1").hash_file(source_file)

        if "content_hash" not in current_page.metadata.keys() or current_page.metadata["content_hash"] != content_hash:
          print(content_hash + " does not match with current " + current_page.metadata["content_hash"])
          extract_page(lang, page)
      except AttributeError:
        extract_page(lang, page)
      except KeyError:
        extract_page(lang, page)
      except ParserError:
        extract_page(lang, page)
      except ScannerError:
        extract_page(lang, page)

indexnow_queue_current_batch = []

def append_base_url(path):
  # Remove the ".md" part of the query
  return "https://nix.reinhart1010.id/" + path[:-3]

while len(indexnow_queue) > 0:
  indexnow_queue_current_batch.append(indexnow_queue.pop())
  if len(indexnow_queue_current_batch) >= 10000 or len(indexnow_queue) == 0:
    try:
      print("Sending an IndexNow request to Bing with %d URLs" % (len(indexnow_queue_current_batch)))
      response = requests.post("https://www.bing.com/indexnow", json={
        "host": "nix.reinhart1010.id",
        "key": "33ef9535d59348be8b8f2b95dfdbe629",
        "urlList": list(map(append_base_url, indexnow_queue_current_batch))
      })
      print("Status code: ", response.status_code)
    except HTTPError as http_err:
        print("HTTP error occurred: %s" % (http_err))  # Python 3.6
    except Exception as err:
        print("Other error occurred: %s" % (err))  # Python 3.6
    else:
        print('Success!')
