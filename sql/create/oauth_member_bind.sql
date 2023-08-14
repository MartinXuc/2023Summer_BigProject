drop table if exists `oauth_member_bind`;
create table `oauth_member_bind`  (
  `id` int(0) unsigned not null auto_increment,
  `member_id` int(0) not null default 0 comment '会员id',
  `client_type` varchar(20) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '客户端来源类型。qq,weibo,weixin',
  `type` tinyint(0) not null default 0 comment '类型 type 1:wechat ',
  `openid` varchar(80) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '第三方id',
  `unionid` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '',
  `extra` text character set utf8mb4 collate utf8mb4_general_ci not null comment '额外字段',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_type_openid`(`type`, `openid`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '第三方登录绑定关系' row_format = dynamic;
