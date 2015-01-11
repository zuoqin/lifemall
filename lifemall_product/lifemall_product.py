from openerp.osv import fields, osv, orm
import logging

#for sale order cancel
from openerp import netsvc
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class lifemall_product_product(orm.Model):
    _name = 'lifemall.product.product'
    _inherit = 'product.product'
    _description = 'Lifemall Product'


    _logger.info('LLLLLLLLLL   lifemall_product')

    #_columns = {
    #    'purchase_ok': fields.boolean('Can be Purchased'),
    #}

    #_defaults = {
    #    'purchase_ok': 1,
    #}
    #product_product()

    def confirmed(self, cr, uid, context=None):
        """ Creates confirmation for selected product.
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param ids: List of IDs selected
        @param context: A standard dictionary
        @return: A dictionary which loads Procurement form view.
        """
        _logger.info('ZZZZZZZZZZ  Calling lifemall.product.product confirm_product')

        # magento_obj = self.pool.get('magento.product.product')

        #_logger.info("Printing magento object:")
        #_logger.info(magento_obj)
        #str1 = "Product_id = " + str(rec_id)
        #_logger.info(str1)
        #_logger.info('ZZZZZZZZZZZ   ids:')
        #ids = res_original.magento_bind_ids
        #print(context)


        # ids = self.pool.get('magento.product.product').search(cr, uid, [('openerp_id', '=', rec_id)])
        # for id in ids:

            

        #     #str1 = "Magento_id = " + str(ids)
        #     str1 = "Magento_id = " + str(id)
        #     _logger.info(str1)
        #     magento_obj.recompute_magento_qty(cr, uid, id,
        #                                           context=context)        







# class stock_return_picking(osv.osv_memory):
#     _inherit = 'stock.return.picking'
#     _description = 'Return Picking'
#     _logger.info('ZZZZZZZZZZZ   product_product - Lifemall')

#     def create_returns(self, cr, uid, ids, context=None):



class sale_order(osv.osv):
    _inherit = "sale.order"
    _description = 'Return Picking'
    _logger.info('ZZZZZZZZZZZ   product_product - Lifemall')



    def action_cancel(self, cr, uid, ids, context=None):
        wf_service = netsvc.LocalService("workflow")
        if context is None:
            context = {}
        sale_order_line_obj = self.pool.get('sale.order.line')
        proc_obj = self.pool.get('procurement.order')
        for sale in self.browse(cr, uid, ids, context=context):
            for pick in sale.picking_ids:
                if pick.state not in ('draft', 'cancel'):



                    #raise osv.except_osv(
                    #    _('Cannot cancel sales order!'),
                    #    _('We will cancel all deliveries for you!!!'))
                    #    _('You must first cancel all delivery order(s) attached to this sales order.'))

                    _logger.info('Action cancel, pick_id = %s', pick.id)
                if pick.state == 'cancel':
                    for mov in pick.move_lines:
                        proc_ids = proc_obj.search(cr, uid, [('move_id', '=', mov.id)])
                        if proc_ids:
                            for proc in proc_ids:
                                wf_service.trg_validate(uid, 'procurement.order', proc, 'button_check', cr)
            for r in self.read(cr, uid, ids, ['picking_ids']):
                for pick in r['picking_ids']:
                    wf_service.trg_validate(uid, 'stock.picking', pick, 'button_cancel', cr)
        return super(sale_order, self).action_cancel(cr, uid, ids, context=context)



#     def create_returns(self, cr, uid, ids, context=None):
#         """ 
#          Creates return picking.
#          @param self: The object pointer.
#          @param cr: A database cursor
#          @param uid: ID of the user currently logged in
#          @param ids: List of ids selected
#          @param context: A standard dictionary
#          @return: A dictionary which of fields with values.
#         """
#         if context is None:
#             context = {} 
#         record_id = ids #context and context.get('active_id', False) or False
#         move_obj = self.pool.get('stock.move')
#         pick_obj = self.pool.get('stock.picking')
#         uom_obj = self.pool.get('product.uom')
#         data_obj = self.pool.get('stock.return.picking.memory')
#         act_obj = self.pool.get('ir.actions.act_window')
#         model_obj = self.pool.get('ir.model.data')
#         wf_service = netsvc.LocalService("workflow")
#         pick = pick_obj.browse(cr, uid, record_id, context=context)
#         print("Pick:")
#         print(pick)
#         data ={}
#         data.update({
#             'invoice_state': pick_obj.invoice_state
#         })        #data = self.read(cr, uid, ids[0], context=context)
#         date_cur = time.strftime('%Y-%m-%d %H:%M:%S')
#         set_invoice_state_to_none = True
#         returned_lines = 0
        
# #        Create new picking for returned products

#         seq_obj_name = 'stock.picking'
#         new_type = 'internal'
#         if pick.type =='out':
#             new_type = 'in'
#             seq_obj_name = 'stock.picking.in'
#         elif pick.type =='in':
#             new_type = 'out'
#             seq_obj_name = 'stock.picking.out'

#         return
#         new_pick_name = self.pool.get('ir.sequence').get(cr, uid, seq_obj_name)
#         new_picking = pick_obj.copy(cr, uid, pick.id, {
#                                         'name': _('%s-%s-return') % (new_pick_name, pick.name),
#                                         'move_lines': [], 
#                                         'state':'draft', 
#                                         'type': new_type,
#                                         'date':date_cur, 
#                                         'invoice_state': data['invoice_state'],
#         })
        
#         val_id = data['product_return_moves']
#         for v in val_id:
#             data_get = data_obj.browse(cr, uid, v, context=context)
#             mov_id = data_get.move_id.id
#             if not mov_id:
#                 raise osv.except_osv(_('Warning !'), _("You have manually created product lines, please delete them to proceed"))
#             new_qty = data_get.quantity
#             move = move_obj.browse(cr, uid, mov_id, context=context)
#             new_location = move.location_dest_id.id
#             returned_qty = move.product_qty
#             for rec in move.move_history_ids2:
#                 returned_qty -= rec.product_qty

#             if returned_qty != new_qty:
#                 set_invoice_state_to_none = False
#             if new_qty:
#                 returned_lines += 1
#                 new_move=move_obj.copy(cr, uid, move.id, {
#                                             'product_qty': new_qty,
#                                             'product_uos_qty': uom_obj._compute_qty(cr, uid, move.product_uom.id, new_qty, move.product_uos.id),
#                                             'picking_id': new_picking, 
#                                             'state': 'draft',
#                                             'location_id': new_location, 
#                                             'location_dest_id': move.location_id.id,
#                                             'date': date_cur,
#                                             'prodlot_id': data_get.prodlot_id.id,
#                 })
#                 move_obj.write(cr, uid, [move.id], {'move_history_ids2':[(4,new_move)]}, context=context)
#         if not returned_lines:
#             raise osv.except_osv(_('Warning!'), _("Please specify at least one non-zero quantity."))

#         if set_invoice_state_to_none:
#             pick_obj.write(cr, uid, [pick.id], {'invoice_state':'none'}, context=context)
#         wf_service.trg_validate(uid, 'stock.picking', new_picking, 'button_confirm', cr)
#         pick_obj.force_assign(cr, uid, [new_picking], context)
#         # Update view id in context, lp:702939
#         model_list = {
#                 'out': 'stock.picking.out',
#                 'in': 'stock.picking.in',
#                 'internal': 'stock.picking',
#         }
#         return {
#             'domain': "[('id', 'in', ["+str(new_picking)+"])]",
#             'name': _('Returned Picking'),
#             'view_type':'form',
#             'view_mode':'tree,form',
#             'res_model': model_list.get(new_type, 'stock.picking'),
#             'type':'ir.actions.act_window',
#             'context':context,
#         }













class product_product(orm.Model):
    _inherit = 'product.product'
    _logger.info('ZZZZZZZZZZZ   product_product - Lifemall')

    def confirmed(self, cr, uid, ids, context=None):
        """ Creates confirmation for selected product.
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param ids: List of IDs selected
        @param context: A standard dictionary
        @return: A dictionary which loads Procurement form view.
        """
        _logger.info('ZZZZZZZZZZ  Calling confirm_product111')
        print ("context:")
        print(context)
        print ("ids:")
        print(ids)

        prod_obj_pool = self.pool.get('product.product')

        product = prod_obj_pool.browse(cr, uid, ids[0], context=context)

        #product = self.pool.get('product.product').search(cr, uid, [('id', '=', ids[0])])



        print("product_product:")
        print(product)
        
        print("product type:")
        print(product.type)
        

        categ_obj_pool = self.pool.get('product.category')

        category = categ_obj_pool.browse(cr, uid, product.categ_id, context=context)
        _logger.info('product category: %s. %s', product.categ_id, category.name)


        _logger.info('product name: %s. product description: %s', product.name, product.description)
        _logger.info('product short description: %s.', product.description_sale)


        magento_obj = self.pool.get('magento.product.product')
        magento_ids = self.pool.get('magento.product.product').search(cr, uid, [('openerp_id', '=', ids[0])])
        _logger.info('magento_ids: %s.', magento_ids[0])

        _logger.info('Calling magento_obj.write, magento_id: %s ', product.magento_bind_ids[0].magento_id)
        
        if product.magento_bind_ids[0].magento_id:
            magento_obj.write(cr, uid, magento_ids[0],
                                   {'magento_id': product.magento_bind_ids[0].magento_id},
                                   context=context)
        else:
            magento_obj.write(cr, uid, magento_ids[0],
                                   {'openerp_id': ids[0]},
                                   context=context)

        #_logger.info('magento_id after Calling magento_obj.write: %s', magento_id)
        #return True
