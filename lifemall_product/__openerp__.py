# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2013-2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{'name': 'Lifemall',
 'version': '1.1.1',
 'author': 'Lifemall',
 'website': 'http://lifemall.com',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """
Customisation for Lifemall Backend
=========

This application designed and supported by
ZuoQin, zuoqinr@163.com
""",
 'depends': ['sale',
             'purchase',
             'procurement'
             ],
 'data': ['lifemall_product.xml',
          ],
 'installable': True,
 'application': True,
 }
