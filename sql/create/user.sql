drop table if exists `user`;
create table `user`  (
  `uid` bigint(0) not null auto_increment comment '用户uid',
  `name` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '用户名',
  `mobile` varchar(20) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '手机号码',
  `email` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '邮箱地址',
  `sex` tinyint(1) not null default 0 comment '1:男 2:女 0:没填写',
  `avatar` varchar(64) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '头像',
  `login_name` varchar(20) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '登录用户名',
  `login_pwd` varchar(32) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '登录密码',
  `login_salt` varchar(32) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '登录密码的随机加密秘钥',
  `status` tinyint(1) not null default 1 comment '1:有效 0:无效',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`uid`) using btree,
  unique index `login_name`(`login_name`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '用户表（管理员）' row_format = dynamic;
