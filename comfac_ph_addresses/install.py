import frappe


def after_migrate():
    _ensure_ph_location_doctypes()
    _import_psgc_data()


def _ensure_ph_location_doctypes():
    required = ["Philippine Province", "Philippine City", "Philippine Barangay"]
    existing = frappe.db.get_list(
        "DocType", pluck="name", filters=[["name", "in", required]]
    )
    missing = set(required) - set(existing)
    if missing:
        frappe.log_error(
            f"comfac_ph_addresses: Missing DocTypes {missing}. "
            "Run bench migrate after installing the app."
        )


def _import_psgc_data():
    if frappe.db.count("Philippine Province") > 0:
        return

    data = _load_psgc_json()
    if not data:
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
                        "province": province_name,
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
