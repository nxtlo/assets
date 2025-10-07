# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SimcardAssets(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		additional_notes: DF.SmallText | None
		asset_cost: DF.Currency
		asset_serial: DF.Barcode
		asset_status: DF.Autocomplete
		covenant: DF.Attach | None
		height: DF.Float
		image: DF.AttachImage | None
		invoice: DF.Attach | None
		line_number: DF.Phone | None
		name1: DF.Literal["STC", "Mobily", "Zain"]
		number_of_units: DF.Int
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		pin_1: DF.Int
		pin_2: DF.Int
		puk1_key: DF.Int
		puk2_key: DF.Int
		width: DF.Float
	# end: auto-generated types
	pass
