from django.urls import path
from.import views

urlpatterns = [
    path("admin_login/",views.admin_login),
    path("",views.index),
    path("checklogin/",views.check_login),
    path("admin_homepage/",views.admin_homepage),
    path("add_category/",views.add_category),
    path("save_category/",views.save_category),
    path("view_category/",views.view_category),
    path("edit_category/<id>",views.edit_category),
    path("update_category/<id>",views.update_category),
    path("delete_category/<id>",views.delete_category),
    path("add_subcategory/",views.add_subcategory),
    path("save_subcategory/",views.save_subcategory),
    path("view_subcategory/",views.view_subcategory),
    path("edit_subcategory/<id>",views.edit_subcategory),
    path("update_subcategory/<id>",views.update_subcategory),
    path("delete_subcategory/<id>",views.delete_subcategory),
    path("add_products/",views.add_products),
    path("save_products/",views.save_products),
    path("view_products/",views.view_products),
    path("edit_products/<id>",views.edit_products),
    path("update_products/<id>",views.update_products),
    path("delete_products/<id>",views.delete_products),
    path("products/",views.products),
    path("items/<id>",views.items),
    path("sub_items/<id>",views.sub_items),
    path("buy_now/<id>",views.buy_now,name="buy_now"),
    path("sign_up/<id>",views.sign_up,name="sign_up"),
    path("save_sign_up/<id>",views.save_sign_up),
    path("logincheck/<id>",views.logincheck),
    path("payment_handler/<id>", views.payment_handler),
    path("add_to_cart/<id>",views.add_to_cart),
    path("cart/",views.cart),
    path("decrease_quantity/<id>",views.decrease_quantity,name="decrease_quantity"),
    path("remove_cart/<id>",views.remove_cart),
    path("proceed_to_checkout/<cart_total>",views.proceed_to_checkout,name="proceed_to_checkout"),
    path("logincheck_cart/<cart_total>",views.logincheck_cart,name="logincheck_cart"),
    path("process_checkout/",views.process_checkout),
    path("single_products/",views.single_products),
    path("multiple_products/",views.multiple_products),
    path("checkout_products/<id>",views.checkout_products),
    path("contact/",views.contact),
    path("about/",views.about),
    path("save_contact/",views.save_contact),
    path("view_list/",views.view_list),
    path("blog/",views.blog),
    path("add_blog/",views.add_blog),
    path("save_blog/",views.save_blog),
    path("view_blog/",views.view_blog),
    path("edit_blog/<id>",views.edit_blog),
    path("update_blog/<id>",views.update_blog),
    path("delete_blog/<id>",views.delete_blog)









]
