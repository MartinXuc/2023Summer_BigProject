drop table if exists `package_item`;
create table `package_item` (
    `id` int(0) unsigned not null auto_increment,
    `member_id` int(0) not null default 0 comment '会员id',
    `package_id` int(0) not null default 0 comment '卡券id',
    `number` int(0) not null default 1 comment '卡券数量',
    `effective_date` datetime(0) not null comment '生效日期',
    `valid_period` int(0) not null default 7 comment '有效期',
    `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后更新时间',
    `created_time` timestamp(0) not null default current_timestamp(0) comment '最后插入时间',
    primary key (`id`) using btree,
    index `idx_member_id`(`member_id`) using btree
)engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci row_format = dynamic;
