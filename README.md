

Presentation
================================
Epyk-studio is a module on top of Epyk-ui in order to facilitate the use of the various features available.
As Epyk-ui is the transpiler to Javascript and web artifacts on few (around 200) components are available.

Epyk-studio will facilitate the use of components by using pre defined styles according to the type of websites.
Epyk-studio will provide some helpers and shortcut to design:

- blog pages
- event pages
- shops
- ad for app
- picture / video gallery


Those pages will generate proper HYML pages which can then be hosted in any company.
There is no need to buy something specific to use Epyk and also to publish your work.


Quickstart
================================

As Epyk-studio is still only available as a Python package to use it you would need to follow the below steps

Install Epyk

> pip install epyk_studio

Create a web page

```py
from epyk_studio.core.Page import Report#

page = Report()
page.headers.dev()

page.ui.title("Print messages")

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

page.ui.title("Dataset")

t1 = page.studio.dashboard.table(dataset.to_dict('records'))
```
Transpile your reports

> python epyk_studio transpile

Usage
======

The idea of this module is to never leave Python until the end of the product.
By using this module there is no need to move to Javascript or even worst to start learning TypeScript to create safe and modern webpages.

This will allow you to make the bridge between Python and Javascript and then to reuse both rich ecosystems.
Everything which is close to Javascript will be using the Javascript naming conventions.

Epyk studio can be used for any kind of project from personal ones to professional ones when dashboards are needed.
Thanks to this module and its design it will be easy to change layouts and to switch the display according to your audience (without changing code or technology).

<b><i>
In the below examples, assets are coming from existing websites. This is only to illustrate some features available in the 
package.
</i>
</b>

For example Epyk Studio can be used in the below cases:

To generate **dashboards** (for time management, data monitoring, machine learning algorithms...)

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-studio/blob/master/static/dashboards.PNG?raw=true">
</div>
<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-studio/blob/master/static/tracking.PNG?raw=true">
</div>

Examples:

[management.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/management.py)
[news.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/news.py)
[tracking.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/tracking.py)


To generate **modern website** (for restaurant, hotel or a specific private event)

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-studio/blob/master/static/foods.PNG?raw=true">
</div>

Examples:

[travel.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/travel.py)
[management.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/hotel.py)
[wedding.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/wedding.py)


To generate **shopping websites** (for e-commerce websites)

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-studio/blob/master/static/shops.PNG?raw=true">
</div>

Examples:

[shop.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/shop.py)
[vitrin.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/vitrin.py)


To generate **slides** (for dynamic and rich presentations)

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-studio/blob/master/static/slides.PNG?raw=true">
</div>

Examples:

[europython](https://github.com/epykure/epyk-templates/blob/master/slides/20200725_sprint_europython.py)
[blog.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/blog.py)
[gallery.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/gallery.py)

To teach Python

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-studio/blob/master/static/teaching.PNG?raw=true">
</div>

Examples:

[learning.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/learning.py)
[image_processing.py](https://github.com/epykure/epyk-templates/blob/master/locals/studio/image_processing.py)


<h2 style="text-align:center">
A simple and afficient way to prototype and share your work !
</h2>

This can also work with Jupyter and JupyterLab more details [here](https://github.com/epykure/epyk-templates-notebooks)

Next features
==================

The Epyk Studio team will be working on 

1. building a online portal to start prototyping directly from the browser.
2. integrating of Native application features for the migration to apps
3. building the community
3. creating of tutorials and examples

As this is a collaborative project, do not hesitate to let us know about your interest and also to share your feedback.

You can also have a look at the main templates and examples repository [here](https://github.com/epykure/epyk-templates)
