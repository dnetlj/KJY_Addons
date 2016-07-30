# -*- coding: utf-8 -*-
import openerp
import openerp.modules.registry
from openerp.addons.base.ir.ir_qweb import AssetsBundle, QWebTemplateNotFound
from openerp.modules import get_resource_path
from openerp.tools import topological_sort
from openerp.tools.translate import _
from openerp.tools import ustr
from openerp import http
from openerp.http import request, serialize_exception as _serialize_exception
from openerp.exceptions import AccessError

_logger = logging.getLogger(__name__)

