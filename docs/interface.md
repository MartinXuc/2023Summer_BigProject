# 接口文档

**domain**

http://highvorz.website.com 

**port**

80



## 前端接口

**url**

/api



#### 餐品列表

###### **url**

/api/food/index



###### **请求方式**

GET



###### **返回数据**

**code**

200



**msg**

success



**data**

序列

``` json
"1": {
    "categorized_list": [
        {
         "id": 4,
         "img_url": "http://highvorz.website/static/upload/food.jpg",
         "name": "劲爆鸡米花",
         "price": "12.00",
         "status": 1,
         "tag_id": 1
        }
     ],
     "tag": "人气热卖"
}
```



| key | value | nullable | description |
| --- | --- | --- | --- |
| categorized_list | [] |          | 分类的菜品列表 |
| tag              | "人气热卖" |  | 种类标签 |



#### 创建订单



###### **功能**

创建订单, 但还未支付状态



###### **url**

/api/order/create



###### **请求方式**

POST



###### **请求数据**

| key                | valueType | nullable | description |
| :----------------- | :-------- | :------- | ----------- |
| type               |           |          |             |
| note               | string    |          |             |
| express_address_id | int       |          |             |
| goods              | {}        |          | 商品列表    |



###### **返回数据**

**code**

200 表示正常

**msg**

success

**data**

| key         | value | description |
| ----------- | ----- | ----------- |
| id          |       | 订单id      |
| order_sn    |       | 订单号      |
| total_price |       | 总金额      |





#### 支付订单

###### **功能**

发起支付, 查询支付结果

###### **url**

/api/order/pay

###### **请求方式**

POST

###### **请求数据**

| key      | value | nullable | description |
| -------- | ----- | -------- | ----------- |
| order_sn |       | 必填     | 订单编号    |



###### 返回数据

| key      | value | description |
| -------- | ----- | ----------- |
| pay_info |       | 支付信息    |





#### 支付回调

功能
