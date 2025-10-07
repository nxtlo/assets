# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Manufacturer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		gps_location: DF.SmallText | None
		manufacturer_image: DF.AttachImage | None
		manufacturer_name: DF.Data
		manufacturer_phone: DF.Phone | None
		manufacturer_website: DF.Data | None
	# end: auto-generated types
	pass
