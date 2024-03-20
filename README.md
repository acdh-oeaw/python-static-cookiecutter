# python-static-cookiecutter
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to bootstrap the development of python based static website.

## Quickstart
* Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.7.0 or higher) by running `pip install -U cookiecutter`
* To generate a new djangobaseproject-based django-project project run `cookiecutter gh:acdh-oeaw/djangobase-cookiecutter` and answer the following questions, see below:

```json
{
    "directory_name": "my-new-project",
    "project_title": "My New Project",
    "github": "https://github.com/acdh-oeaw/my-new-project",
    "redmine_id": "18716"
} 
```

* change into the new created repo, by default `$ my-new-project`
* create a virtual env
* install requierements `pip install -r requirements.txt`
* start developing