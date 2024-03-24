import os
import glob
import json
import jinja2
import requests

templateLoader = jinja2.FileSystemLoader(searchpath=".")
templateEnv = jinja2.Environment(loader=templateLoader)

out_dir = "html"

with open("project.json", "r", encoding="utf-8") as f:
    project_data = json.load(f)

redmine_id = project_data["redmine_id"]
imprint_url = f"https://imprint.acdh.oeaw.ac.at/{redmine_id}?locale=de"
print(imprint_url)
try:
    r = requests.get(imprint_url)
    project_data["imprint"] = r.content.decode("utf-8")
except Exception as e:
    project_data["imprint"] = e

os.makedirs(out_dir, exist_ok=True)
for x in glob.glob(f"{out_dir}/*.html"):
    os.unlink(x)

files = glob.glob("./templates/static/*.j2")

print("building static content")
for x in files:
    print(x)
    template = templateEnv.get_template(x)
    _, tail = os.path.split(x)
    print(f"rendering {tail}")
    output_path = os.path.join("html", tail.replace(".j2", ".html"))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template.render({"project_data": project_data}))
