app_name = "comfac_ph_addresses"
app_title = "Comfac PH Addresses"
app_publisher = "Comfac Global Group"
app_description = "Philippine address/location data — PSGC import, cascading dropdowns, geolocation"
app_email = "it@comfac-it.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/comfac_ph_addresses/css/comfac_ph_addresses.css"
# app_include_js = "/assets/comfac_ph_addresses/js/comfac_ph_addresses.js"

# include js, css files in header of web template
# web_include_css = "/assets/comfac_ph_addresses/css/comfac_ph_addresses.css"
# web_include_js = "/assets/comfac_ph_addresses/js/comfac_ph_addresses.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "comfac_ph_addresses/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "comfac_ph_addresses/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "comfac_ph_addresses.utils.jinja_methods",
# 	"filters": "comfac_ph_addresses.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "comfac_ph_addresses.install.before_install"
# after_install = "comfac_ph_addresses.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "comfac_ph_addresses.uninstall.before_uninstall"
# after_uninstall = "comfac_ph_addresses.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "comfac_ph_addresses.utils.before_app_install"
# after_app_install = "comfac_ph_addresses.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "comfac_ph_addresses.utils.before_app_uninstall"
# after_app_uninstall = "comfac_ph_addresses.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "comfac_ph_addresses.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"comfac_ph_addresses.tasks.all"
# 	],
# 	"daily": [
# 		"comfac_ph_addresses.tasks.daily"
# 	],
# 	"hourly": [
# 		"comfac_ph_addresses.tasks.hourly"
# 	],
# 	"weekly": [
# 		"comfac_ph_addresses.tasks.weekly"
# 	],
# 	"monthly": [
# 		"comfac_ph_addresses.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "comfac_ph_addresses.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "comfac_ph_addresses.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "comfac_ph_addresses.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["comfac_ph_addresses.utils.before_request"]
# after_request = ["comfac_ph_addresses.utils.after_request"]

# Job Events
# ----------
# before_job = ["comfac_ph_addresses.utils.before_job"]
# after_job = ["comfac_ph_addresses.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"comfac_ph_addresses.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

