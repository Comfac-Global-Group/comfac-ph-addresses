frappe.ui.form.on("Address", {
    setup: function (frm) {
        frm.set_query("custom_province", function () {
            let region = frm.doc.custom_region;
            let filters = {};
            if (region) {
                filters.region_code = region;
            }
            return { filters: filters };
        });

        frm.set_query("custom_city_municipality", function () {
            let province = frm.doc.custom_province;
            let filters = {};
            if (province) {
                filters.province = province;
            }
            return { filters: filters };
        });

        frm.set_query("custom_barangay", function () {
            let city = frm.doc.custom_city_municipality;
            let filters = {};
            if (city) {
                filters.city = city;
            }
            return { filters: filters };
        });
    },

    custom_region: function (frm) {
        frm.set_value("custom_province", null);
        frm.set_value("custom_city_municipality", null);
        frm.set_value("custom_barangay", null);
    },

    custom_province: function (frm) {
        frm.set_value("custom_city_municipality", null);
        frm.set_value("custom_barangay", null);
    },

    custom_city_municipality: function (frm) {
        frm.set_value("custom_barangay", null);
    },

    geocode: function (frm) {
        if (!frm.doc.name) {
            frappe.msgprint(__("Save the address first."));
            return;
        }
        frappe.call({
            method: "comfac_ph_addresses.api.geocode_address",
            args: { address_name: frm.doc.name },
            callback: function (r) {
                if (r.message) {
                    frappe.show_alert({
                        message: __("Geocoded: {0}, {1}", [r.message.lat, r.message.lon]),
                        indicator: "green",
                    });
                    frm.refresh_field("custom_geolocation");
                }
            },
        });
    },
});
