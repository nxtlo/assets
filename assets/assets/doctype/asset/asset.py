# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Asset(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.assets.doctype.connectivity.connectivity import Connectivity
		from frappe.assets.doctype.simcard_assets.simcard_assets import SimcardAssets
		from frappe.model.document import Document
		from frappe.types import DF

		additional_notes: DF.SmallText | None
		asset_category: DF.Link
		asset_cost: DF.Currency
		asset_location: DF.Literal["HO", "BDC", "HTC", "OCC", "Blue Square", "Jaffai", "Valet"]
		asset_name: DF.Data
		asset_owner: DF.Link
		asset_serial: DF.Barcode
		asset_status: DF.Literal["Active", "Inactive", "Unused", "In Repair", "Unknown"]
		computer_type: DF.Literal["PC", "All-in-One", "Laptop", "Local Server", "VPS"]
		covenant: DF.Attach | None
		image: DF.AttachImage | None
		invoice: DF.Attach | None
		manufacturer: DF.Link
		model: DF.Link | None
		network_device_type: DF.Literal["Switch", "Router", "Server", "Access Point", "None"]
		sim_cards: DF.Table[SimcardAssets]
		table_dvaq: DF.Table[Document]
		table_eyir: DF.Table[Connectivity]
	# end: auto-generated types
	pass
