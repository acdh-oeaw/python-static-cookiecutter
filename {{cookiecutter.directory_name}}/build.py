import os
import glob
import jinja2
import json

templateLoader = jinja2.FileSystemLoader(searchpath=".")
templateEnv = jinja2.Environment(loader=templateLoader)

out_dir = "html"

with open("project.json", "r", encoding="utf-8") as f:
    project_data = json.load(f)

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
