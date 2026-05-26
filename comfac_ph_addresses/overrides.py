import json

import frappe


def address_on_update(doc, method):
    if not doc.get("custom_barangay"):
        return
    try:
        if not doc.get("custom_mail_code"):
            mail_code = frappe.db.get_value(
                "Philippine Barangay", doc.custom_barangay, "mail_code"
            )
            if mail_code:
                doc.db_set("custom_mail_code", mail_code)
    except Exception:
        frappe.log_error(
            f"address_on_update failed for {doc.name}", frappe.get_traceback()
        )


def geocode_address(doc, method):
    if not doc.custom_geolocation and doc.custom_barangay:
        geolocation = _forward_geocode(doc)
        if geolocation:
            doc.db_set("custom_geolocation", geolocation)


def _forward_geocode(doc):
    address_parts = []
    if doc.custom_barangay:
        barangay_name = frappe.db.get_value(
            "Philippine Barangay", doc.custom_barangay, "barangay_name"
        )
        if barangay_name:
            address_parts.append(barangay_name)

    if doc.city:
        city_name = frappe.db.get_value("City", doc.city, "city_name")
        if city_name:
            address_parts.append(city_name)
        elif doc.custom_city_municipality:
            city_name = frappe.db.get_value(
                "Philippine City", doc.custom_city_municipality, "city_name"
            )
            if city_name:
                address_parts.append(city_name)

    if doc.state:
        address_parts.append(doc.state)

    if not address_parts:
        return None

    query = ", ".join(address_parts)
    try:
        result = frappe.integrations.utils.make_get_request(
            "https://nominatim.openstreetmap.org/search",
            params={"q": query + ", Philippines", "format": "json", "limit": 1},
            headers={"User-Agent": "ComfacERPNext/1.0 (it@comfac-it.com)"},
        )
        if result and len(result) > 0:
            lat = result[0].get("lat")
            lon = result[0].get("lon")
            if lat and lon:
                return json.dumps(
                    {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "Point",
                            "coordinates": [float(lon), float(lat)],
                        },
                    }
                )
    except Exception:
        frappe.log_error("Geocoding failed for Address", frappe.get_traceback())

    return None
