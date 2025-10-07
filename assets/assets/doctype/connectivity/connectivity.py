# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Connectivity(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		anydesk_address: DF.Data | None
		gateway: DF.Data | None
		ip_address: DF.Data | None
		mac: DF.Data | None
		network_type: DF.Literal["LAN", "WAN", "VPN"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		password: DF.Password | None
		port: DF.Int
		protocol: DF.Literal["IP Address", "Remote Desktop", "SSH", "FTP", "AnyDesk", "Webserver"]
		url: DF.Data | None
		username: DF.Data | None
		vpn_ip_address: DF.Data | None
	# end: auto-generated types
	pass
