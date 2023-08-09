import os
import xlwt
from django.conf import settings
from src.products.models import Product
from src.common.services import Service


class ProductService(Service):
    model = Product

    @classmethod
    def get_file(cls):
        file = xlwt.Workbook(encoding='utf-8')
        products_sheet = file.add_sheet('Список продуктов', cell_overwrite_ok=False)

        font_style = xlwt.easyxf('pattern: pattern solid, fore_colour light_green')
        alignment = xlwt.Alignment()
        alignment.wrap = True
        alignment.horz = xlwt.Alignment.HORZ_DISTRIBUTED
        alignment.vert = xlwt.Alignment.VERT_DISTRIBUTED
        font_style.alignment = alignment
        font_style.font.bold = True
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        font_style.borders = borders

        products_sheet.col(0).width = 5500
        products_sheet.row(0).height = 800
        products_sheet.col(1).width = 5000
        products_sheet.row(1).height = 800

        products_sheet.write(0, 0, 'Наименование', font_style)
        products_sheet.write(0, 1, 'Описание',font_style)
        products_sheet.write(0, 2, 'Цена', font_style)
        products_sheet.write(0, 3, 'Категория', font_style)
        products_sheet.write(0, 4, 'Теги', font_style)

        products = cls.filter(is_deleted=False)
        row_num = 1
        for product in products:
            font_style = xlwt.XFStyle()
            borders = xlwt.Borders()
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            font_style.borders = borders
            products_sheet.write(row_num, 0, product.name, font_style)
            products_sheet.write(row_num, 1, product.description, font_style)
            products_sheet.write(row_num, 2, product.price, font_style)
            products_sheet.write(row_num, 3, product.category.name, font_style)
            products_sheet.write(row_num, 4, ', '.join([tag.name for tag in product.tags.all()]), font_style)
            row_num += 1
        file.save('back_media/Report.xlsx')
        return os.path.join(settings.MEDIA_URL, 'Report.xlsx')

