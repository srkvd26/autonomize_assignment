import openpyxl

class ExcelWriter:
    @staticmethod
    def write(file_path, products):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Products List"
        sheet.append(["Title", "Price", "Rating", "Reviews"])

        for product in products:
            sheet.append([product["title"], product["price"], product["rating"], product["reviews"]])

        workbook.save(file_path)
