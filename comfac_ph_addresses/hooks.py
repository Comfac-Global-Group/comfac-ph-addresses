app_name = "comfac_ph_addresses"
app_title = "Comfac PH Addresses"
app_publisher = "Comfac Global Group"
app_description = (
    "Philippine address/location data — PSGC import, cascading dropdowns, geolocation"
)
app_email = "it@comfac-it.com"
app_license = "mit"

required_apps = ["erpnext"]

after_migrate = "comfac_ph_addresses.install.after_migrate"

doc_events = {
    "Address": {
        "on_update": "comfac_ph_addresses.overrides.address_on_update",
    },
}

doctype_js = {
    "Address": "public/js/address.js",
}

fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Comfac PH Addresses"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Comfac PH Addresses"]]},
]
