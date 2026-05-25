import json

import frappe


@frappe.whitelist()
def get_provinces(region_code=None):
    filters = {}
    if region_code:
        filters["region_code"] = region_code
    return frappe.get_all(
        "Philippine Province",
        fields=["name", "province_name", "region_code"],
        filters=filters,
        order_by="province_name",
    )


@frappe.whitelist()
def get_cities(province=None):
    filters = {}
    if province:
        filters["province"] = province
    return frappe.get_all(
        "Philippine City",
        fields=["name", "city_name", "province", "city_type", "display_name"],
        filters=filters,
        order_by="city_name",
    )


@frappe.whitelist()
def get_barangays(city=None):
    filters = {}
    if city:
        filters["city"] = city
    return frappe.get_all(
        "Philippine Barangay",
        fields=["name", "barangay_name", "city", "display_name", "mail_code"],
        filters=filters,
        order_by="barangay_name",
    )


@frappe.whitelist()
def geocode_address(address_name):
    doc = frappe.get_doc("Address", address_name)
    address_parts = []
    if doc.custom_barangay:
        barangay_name = frappe.db.get_value(
            "Philippine Barangay", doc.custom_barangay, "barangay_name"
        )
        if barangay_name:
            address_parts.append(barangay_name)

    if doc.city:
        address_parts.append(doc.city)
    if doc.state:
        address_parts.append(doc.state)

    if not address_parts:
        frappe.throw("No location data to geocode")

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
                geolocation = json.dumps(
                    {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "Point",
                            "coordinates": [float(lon), float(lat)],
                        },
                    }
                )
                doc.db_set("custom_geolocation", geolocation)
                return {"lat": float(lat), "lon": float(lon)}
    except Exception:
        frappe.log_error("Geocoding failed", frappe.get_traceback())
        frappe.throw("Geocoding failed. Please try again.")
