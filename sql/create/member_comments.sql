drop table if exists `member_comments`;
create table `member_comments`  (
  `id` int(0) unsigned not null auto_increment,
  `member_id` int(0) not null default 0 comment '会员id',
  `food_ids` varchar(200) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '商品ids',
  `pay_order_id` int(0) not null default 0 comment '订单id',
  `score` tinyint(0) not null default 0 comment '评分',
  `content` varchar(200) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '评论内容',
  `created_time` timestamp(0) not null default current_timestamp(0) on update current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_member_id`(`member_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '会员评论表' row_format = dynamic;
