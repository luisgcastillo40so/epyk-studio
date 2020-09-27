
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar

# Create a basic report object
page = Report()

nav_bar(page, "Project")

c = page.ui.title("Create new report")
c.style.standard()

s_new = page.ui.input(htmlCode="name")
s_new.style.css.text_align = "left"
s_new.style.css.padding_left = 5
s_new.style.standard()

pills = page.ui.panels.pills(htmlCode="category")
pills.style.css.padding_bottom = 5
pills.style.css.padding_top = 5
pills.style.standard()

pills.add_panel("Page", None, selected=True)
pills.add_panel("Blog", None)
pills.add_panel("Gallery", None)
pills.add_panel("Dashboard", None)

b_new = page.ui.buttons.large("New Report", align="center")

wa = page.ui.title("Get web artifacts", align="center")
wa.style.standard()
wp = page.ui.texts.text('''
Produce rich HTML pages from your Python code
''', align="center")
wp.style.standard()
wp.style.css.margin_bottom = 10
b_transpile = page.ui.buttons.large("Transpile", align="center")

s = page.ui.title("Attach a server", align="center")
s.style.standard()
b_server = page.ui.buttons.large("Server", align="center")

t = page.ui.title("Scan external packages")
t.style.standard()
pr = page.ui.texts.paragraph('''
Find an existing report in the project
''')
pr.style.standard()

inp_pr = page.ui.input(htmlCode="reports")
inp_pr.style.css.text_align = "left"
inp_pr.style.css.padding_left = 5
inp_pr.style.standard()

add_code(page)


def add_inputs(inputs):
  nav.title._vals = inputs.get('name', '')
  b_new.click([
    page.js.post("/projects_page_add", {'project': inputs.get('name', '')}, components=[s_new, pills])
  ])

  b_transpile.click([
    page.js.post("/projects_transpile", {'project': inputs.get('name', '')})
  ])

  b_server.click([
    page.js.post("/projects_add_server", {'project': inputs.get('name', '')})
  ])