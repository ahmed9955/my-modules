from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    phone = fields.Char(related="partner_id.phone",string="Phone")
    mobile = fields.Char(related="partner_id.mobile",string="Mobile")    
    address = fields.Char(string="Address", compute="compute_address")

    @api.depends('partner_id')
    def compute_address(self):
        address = ''

        if self.partner_id.street:
            address += self.partner_id.street + ' - '
        if self.partner_id.state_id:
            address += self.partner_id.state_id.name + ' - '
        if self.partner_id.country_id:
            address += self.partner_id.country_id.name

        self.address = address