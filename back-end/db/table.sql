create table task
(
    id            int auto_increment
        primary key,
    c_title       varchar(255)     not null,
    c_description text             not null,
    c_user_id     int              not null,
    c_status      int(1) default 0 not null comment '0是未完成,1是未完成'
);

create table user
(
    id         int auto_increment
        primary key,
    c_username varchar(32)  not null,
    c_passwd   varchar(255) not null
);

