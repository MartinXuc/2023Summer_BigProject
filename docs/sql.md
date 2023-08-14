database: order

粗体代表新设计, 具体内容不详细描述



**user**

``` sql
create table user{

}
```



**food**

``` sql
create table food{
	name
	price
	img
}
```









#### food

food_cat	餐品类别 ->  FoodCat



food_sale_change_log -> FoodSaleChangeLog



food_stock_change_log -> FoodStockChangeLog



food -> Food



#### log
登录记录表

app_access_log -> AppAccessLog



app_error_log -> AppErrorLog



#### member
用户表
member -> Member
用户购物车表
member_cart -> MemberCart

oauth_member_bind -> OauthMemberBind



#### pay

oauth_access_token -> OauthAccessToken

pay_order -> PayOrder

pay_order_callback_data -> PayOrderCallbackData

pay_order_item -> PayOrderItem



#### image

images -> Image



#### user

user -> User



#### none

member_address

member_comments

queue_list

stat_daily_food

stat_daily_member

stat_daily_site

wx_share_history





















