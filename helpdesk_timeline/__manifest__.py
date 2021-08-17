# Copyright 2016-2017 Tecnativa - Pedro M. Baeza
# Copyright 2017 Tecnativa - Carlos Dauden
# Copyright 2021 Open Source Integrators - Daniel Reis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk timeline",
    "summary": "Timeline view for helpdesk",
    "version": "14.0.1.1.0",
    "category": "Project Management",
    "website": "https://github.com/OCA/project",
    "author": "Tecnativa, Onestein, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["project", "web_timeline"],
    "data": [
        "templates/assets.xml",
        "views/helpdesk_project_view.xml",
        "views/helpdesk_task_view.xml",
    ],
    "demo": ["demo/project_project_demo.xml", "demo/project_task_demo.xml"],
    "post_init_hook": "populate_date_start",
}
