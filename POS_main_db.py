import POS_schema_create
import insert_category
import insert_product
import insert_customer
import insert_employee
import insert_sale
import insert_sale_item

connection = POS_schema_create.pos_create_schema()

insert_category.category_insert(connection)

insert_product.product_insert(connection)

insert_customer.customer_insert(connection)

insert_employee.employee_insert(connection)

insert_sale.sale_insert(connection)

insert_sale_item.sale_item_insert(connection)