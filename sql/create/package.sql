drop table if exists `package`;
create table `package` (
    `id` int(0) unsigned not null auto_increment,
    `food_id` int(0) not null default 0 comment '菜品id',
    `discount` int(0) not null default 0 comment '折扣优惠',
    `type` int(0) not null default 1 comment '0: 游客优惠券 1: 用户优惠券',
    `status` tinyint(1) not null default 1 comment '状态 1:有效 0:无效',
    `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后更新时间',
    `created_time` timestamp(0) not null default current_timestamp(0) comment '最后插入时间',
    primary key (`id`) using btree
)engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci row_format = dynamic;

