drop table if exists `food`;
create table `food`  (
  `id` int(0) unsigned not null auto_increment,
  `cat_id` int(0) not null default 0 comment '分类id',
  `name` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment 'foodname',
  `price` decimal(10, 2) not null comment '售卖金额',
  `main_image` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '主图',
  `summary` varchar(10000) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '描述',
  `stock` int(0) not null default 0 comment '库存量',
  `tags` varchar(200) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment 'tag关键字，以\",\"连接',
  `status` tinyint(1) not null default 1 comment '状态 1:有效 0:无效',
  `month_count` int(0) not null default 0 comment '月销售数量',
  `total_count` int(0) not null default 0 comment '总销售量',
  `view_count` int(0) not null default 0 comment '总浏览次数',
  `comment_count` int(0) not null default 0 comment '总评论量',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '最后插入时间',
  primary key (`id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '食品表' row_format = dynamic;
