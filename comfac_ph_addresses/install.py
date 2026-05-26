import frappe


def after_migrate():
    _create_ph_location_doctypes()
    _import_psgc_data()


# ─── DocType Field Definitions ──────────────────────────────────────────────

_PROVINCE_FIELDS = [
    {
        "fieldname": "province_name",
        "label": "Province Name",
        "fieldtype": "Data",
        "reqd": 1,
        "in_list_view": 1,
        "in_standard_filter": 1,
    },
    {
        "fieldname": "region_code",
        "label": "Region Code",
        "fieldtype": "Data",
        "in_list_view": 1,
        "in_standard_filter": 1,
    },
    {"fieldname": "region_name", "label": "Region Name", "fieldtype": "Data"},
]

_CITY_FIELDS = [
    {
        "fieldname": "city_name",
        "label": "City/Municipality Name",
        "fieldtype": "Data",
        "reqd": 1,
        "in_list_view": 1,
        "in_standard_filter": 1,
    },
    {
        "fieldname": "province",
        "label": "Province",
        "fieldtype": "Link",
        "options": "Philippine Province",
        "reqd": 1,
        "in_list_view": 1,
    },
    {
        "fieldname": "city_type",
        "label": "Type",
        "fieldtype": "Select",
        "options": "City\nMunicipality",
        "in_list_view": 1,
    },
    {
        "fieldname": "display_name",
        "label": "Display Name",
        "fieldtype": "Data",
        "in_list_view": 1,
    },
]

_BARANGAY_FIELDS = [
    {
        "fieldname": "barangay_name",
        "label": "Barangay Name",
        "fieldtype": "Data",
        "reqd": 1,
        "in_list_view": 1,
        "in_standard_filter": 1,
    },
    {
        "fieldname": "city",
        "label": "City/Municipality",
        "fieldtype": "Link",
        "options": "Philippine City",
        "reqd": 1,
        "in_list_view": 1,
    },
    {
        "fieldname": "display_name",
        "label": "Display Name",
        "fieldtype": "Data",
        "in_list_view": 1,
    },
    {"fieldname": "mail_code", "label": "Mail Code", "fieldtype": "Data"},
]


def _create_ph_location_doctypes():
    existing = frappe.db.get_list(
        "DocType",
        pluck="name",
        filters=[
            [
                "name",
                "in",
                ["Philippine Province", "Philippine City", "Philippine Barangay"],
            ]
        ],
    )

    doctype_defs = [
        {
            "name": "Philippine Province",
            "module": "Setup",
            "custom": 1,
            "autoname": "field:province_name",
            "fields": _PROVINCE_FIELDS,
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1,
                }
            ],
        },
        {
            "name": "Philippine City",
            "module": "Setup",
            "custom": 1,
            "autoname": "format:{city_name}-{province}",
            "fields": _CITY_FIELDS,
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1,
                }
            ],
        },
        {
            "name": "Philippine Barangay",
            "module": "Setup",
            "custom": 1,
            "autoname": "hash",
            "fields": _BARANGAY_FIELDS,
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1,
                }
            ],
        },
    ]

    for dt in doctype_defs:
        if dt["name"] not in existing:
            doc = frappe.get_doc({"doctype": "DocType", **dt})
            doc.flags.ignore_permissions = True
            doc.flags.ignore_mandatory = True
            doc.insert()
            frappe.db.commit()


def _import_psgc_data():
    data = _load_psgc_json()
    if not data:
        return

    if frappe.db.count("Philippine Province") > 0:
        frappe.log_error(
            "comfac_ph_addresses: PSGC data already imported (provinces > 0). Skipping."
        )
        return

    for region_code, region_data in data.items():
        region_name = region_data.get("region_name", "")
        province_list = region_data.get("province_list", {})

        for province_name, province_data in province_list.items():
            province_doc = frappe.get_doc(
                {
                    "doctype": "Philippine Province",
                    "province_name": province_name,
                    "region_code": region_code,
                    "region_name": region_name,
                }
            )
            province_doc.flags.ignore_permissions = True
            province_doc.flags.ignore_mandatory = True
            province_doc.insert(ignore_if_duplicate=True)

            municipality_list = province_data.get("municipality_list", {})
            for city_name, city_data in municipality_list.items():
                city_doc = frappe.get_doc(
                    {
                        "doctype": "Philippine City",
                        "city_name": city_name,
                        "province": province_doc.name,
                        "city_type": city_data.get("city_type", "Municipality"),
                    }
                )
                city_doc.flags.ignore_permissions = True
                city_doc.flags.ignore_mandatory = True
                city_doc.insert(ignore_if_duplicate=True)

                barangay_list = city_data.get("barangay_list", [])
                for barangay_name in barangay_list:
                    brgy_doc = frappe.get_doc(
                        {
                            "doctype": "Philippine Barangay",
                            "barangay_name": barangay_name,
                            "city": city_doc.name,
                        }
                    )
                    brgy_doc.flags.ignore_permissions = True
                    brgy_doc.flags.ignore_mandatory = True
                    brgy_doc.insert(ignore_if_duplicate=True)

            frappe.db.commit()


def _load_psgc_json():
    import os

    json_path = frappe.get_app_path(
        "comfac_ph_addresses", "data", "ph_locations_2019v2.json"
    )
    if not os.path.exists(json_path):
        frappe.log_error(
            "comfac_ph_addresses: PSGC data file not found at "
            f"{json_path}. Skipping import."
        )
        return None
    with open(json_path) as f:
        return frappe.parse_json(f.read())
