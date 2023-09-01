drop table if exists `food`;
create table `food`  (
  `id` int(0) unsigned not null auto_increment, -- 食品ID，自增主键
  `cat_id` int(0) not null default 0 comment '分类id', -- 分类ID，表示食品所属的分类
  `name` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment 'foodname', -- 食品名称
  `price` decimal(10, 2) not null comment '售卖金额', -- 售卖金额，保留两位小数
  `main_image` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '主图', -- 食品的主图
  `summary` varchar(10000) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '描述', -- 食品的描述摘要
  `stock` int(0) not null default 0 comment '库存量', -- 食品的库存量
  `tags` varchar(200) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment 'tag关键字，以\",\"连接', -- 食品的标签关键字，多个标签用逗号分隔
  `status` tinyint(1) not null default 1 comment '状态 1:有效 0:无效', -- 食品的状态，1表示有效，0表示无效
  `month_count` int(0) not null default 0 comment '月销售数量', -- 食品的月销售数量
  `total_count` int(0) not null default 0 comment '总销售量', -- 食品的总销售数量
  `view_count` int(0) not null default 0 comment '总浏览次数', -- 食品的总浏览次数
  `comment_count` int(0) not null default 0 comment '总评论量', -- 食品的总评论数量
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后更新时间', -- 最后一次更新食品信息的时间
  `created_time` timestamp(0) not null default current_timestamp(0) comment '最后插入时间', -- 最后一次插入食品信息的时间
  primary key (`id`) using btree -- 主键定义为id字段，使用btree索引方式
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '食品表' row_format = dynamic; -- 使用InnoDB引擎，字符集为utf8mb4，校对规则为utf8mb4_general_ci，行格式为动态