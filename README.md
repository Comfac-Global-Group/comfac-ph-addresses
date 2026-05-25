# comfac-ph-addresses

**Philippine Address/Location App for ERPNext**

PSGC import, cascading dropdowns, and geolocation feedback loop for Comfac ERPNext instances.

## Architecture

Custom Frappe app containing:
- **DocTypes**: Philippine Province, City/Municipality, Barangay (in file)
- **Custom Fields**: Address form fields (region, province, city, barangay, mail_code, geolocation)
- **Client Script**: Cascading dropdowns (Region → Province → City → Barangay), geocode buttons
- **Server Hooks**: Address Before Save (display_name, mail_code, geocoding)

## Source

Primary data from the [Philippine Standard Geographic Code (PSGC)](https://psa.gov.ph/classification/psgc) via `flores-jacob/philippine-regions-provinces-cities-municipalities-barangays`.

## Repositories

| Remote | URL | Purpose |
|--------|-----|---------|
| `origin` (citfj) | `https://git.comfac-it.net/cgg/comfac-ph-addresses.git` | Primary backup |
| `github` | `https://github.com/Comfac-Global-Group/comfac-ph-addresses.git` | Public mirror |
| `github-private` | `https://github.com/Comfac-Global-Group/comfac-ph-addresses-private.git` | Frappe Cloud deploy source |

## Related

- `work/comfac-erpnext/` — `address-location` branch: PSGC data, test suite, original server scripts
- `tools/IT-knowledge/skills/frappe-app-creation/SKILL.md` — Frappe app decision framework
