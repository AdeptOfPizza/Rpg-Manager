# Copyright (c) 2024, roman zyryanov and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RpgPlayer(Document):
	def autoname(self):
		if self.nickname:
			self.name = f'{self.first_name} "{self.nickname}" {self.last_name}'
		else:
			self.name = f'{self.first_name} {self.last_name}'