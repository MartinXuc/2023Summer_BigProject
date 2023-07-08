## 接口文档
http://highvorz.website.com:5000

#### 前端接口
http://highvorz.website.com:5000/api

###### 餐品列表
http://highvorz.website.com:5000/api/food/index

**请求方式**
GET

**返回数据**
| key | value | description |
| --- | --- | --- |
| code | 200 | 状态码200表示正常 |
| msg |  success | 含义 |
| data | {<br>&emsp;'1':{<br>&emsp;"classfy_list":[{},{},...],<br>&emsp;"tag":"人气热卖"<br>&emsp;},<br>} | 数据 |
