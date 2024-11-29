from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_type = fields.Selection(selection=[
                                                ('customer','Customer'),
                                                ('vendor','Vendor'),
                                                ('customer_vendor','Customer and Vendor'),
                                                ('employee','Employee')
                                                ],string="Partner Type",required=True)
    contact_person_id = fields.Many2one('res.partner',string="Contact Person")
    commercial_register = fields.Char(string="Commercial Register")
    tax_card = fields.Char(string="Tax Card")
    commercial_expiration = fields.Date('Commercial Expiration')
    tax_card_expiration = fields.Date('Tax Card Expiration')

    commercial_regeister_attachment_ids = fields.Many2many(
        'ir.attachment',
        'commercial_reg_rel',
        string="Commercial Register",
        help="Upload files as attachments.",
    )

    company_profile_attachment_ids = fields.Many2many(
        'ir.attachment',
        'company_profile_rel',
        string="Company Profile",
        help="Upload files as attachments.",
    )
    tax_card_attachment_ids = fields.Many2many(
        'ir.attachment',
        'tax_card_rel',
        string="Card Attachment",
        help="Upload files as attachments.",
    )
    vat_card_attachment_ids = fields.Many2many(
        'ir.attachment',
        'vat_card_rel',
        string="Vat Card",
        help="Upload files as attachments.",
    )
    trade_license_attachment_ids = fields.Many2many(
        'ir.attachment',
        'trade_license_rel',
        string="Copy Trade License",
        help="Upload files as attachments.",
    )

    has_commercial_register = fields.Boolean(
        string="Has Commercial Register",
        compute="_compute_attachment_flags",
        store=True
    )
    has_company_profile = fields.Boolean(
        string="Has Company Profile",
        compute="_compute_attachment_flags",
        store=True
    )
    has_tax_card = fields.Boolean(
        string="Has Tax Card",
        compute="_compute_attachment_flags",
        store=True
    )
    has_vat_card = fields.Boolean(
        string="Has VAT Card",
        compute="_compute_attachment_flags",
        store=True
    )
    has_trade_license = fields.Boolean(
        string="Has Trade License",
        compute="_compute_attachment_flags",
        store=True
    )

    @api.depends(
        'commercial_regeister_attachment_ids',
        'company_profile_attachment_ids',
        'tax_card_attachment_ids',
        'vat_card_attachment_ids',
        'trade_license_attachment_ids'
    )
    def _compute_attachment_flags(self):
        for record in self:
            record.has_commercial_register = bool(record.commercial_regeister_attachment_ids)
            record.has_company_profile = bool(record.company_profile_attachment_ids)
            record.has_tax_card = bool(record.tax_card_attachment_ids)
            record.has_vat_card = bool(record.vat_card_attachment_ids)
            record.has_trade_license = bool(record.trade_license_attachment_ids)



    @api.model
    def create(self,vals):
        res = super().create(vals)
        '''
            Check That bank account has one line at least
        '''
        if len(res.bank_ids) == 0 and res.partner_type in ('vendor','customer_vendor'):
            raise ValidationError("You must enter at least one bank account!")

        return res


    def write(self,vals):
        res = super().write(vals)
        '''
            Check That bank account has one line at least
        '''
        for rec in self:
            if len(rec.bank_ids) == 0 and rec.partner_type in ('vendor','customer_vendor'):
                raise ValidationError("You must enter at least one bank account!")

        return res
