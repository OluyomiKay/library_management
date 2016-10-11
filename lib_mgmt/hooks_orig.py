# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lib_mgmt"
app_title = "Library Management"
app_publisher = "Yomi"
app_description = "Test App to manage Users, Memberships, Articles and Transactions for Libraries"
app_icon = "octicon octicon-file-directory"
app_color = "teal"
app_email = "testuser@ia-group.com.au"
app_license = "GNU Genenral Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lib_mgmt/css/lib_mgmt.css"
# app_include_js = "/assets/lib_mgmt/js/lib_mgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/lib_mgmt/css/lib_mgmt.css"
# web_include_js = "/assets/lib_mgmt/js/lib_mgmt.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lib_mgmt.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lib_mgmt.install.before_install"
# after_install = "lib_mgmt.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lib_mgmt.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lib_mgmt.tasks.all"
# 	],
# 	"daily": [
# 		"lib_mgmt.tasks.daily"
# 	],
# 	"hourly": [
# 		"lib_mgmt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lib_mgmt.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lib_mgmt.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lib_mgmt.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lib_mgmt.event.get_events"
# }

