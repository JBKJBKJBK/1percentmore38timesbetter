-- 테이블은 각 열마다 반드시 1가지 데이터 타입
-- : 숫자형, 문자형, 날짜형, 숫자형(논리형)
/* 
    숫자형 / 바이트 수 / 숫자 범위
    bit    / 1 /
    int    / 4 / 
    bigint / 8 /
    float  / 4 /
    double / 8 / 
*/
/*
    문자형 / 바이트 수 / 설명
    char()
    nchar()
    varchar()
    nvarchar()
*/
/*
    날짜형 / 바이트 수 / 설명
    datetime  / 8 / YYYY-MM-DD hh:mm:ss
    date      / 3 / YYYY-MM-DD
    time      / 5 / hh:mm:ss
*/

/*
    PK(Primary Key) : 중복안됨 & not null
    not null
*/

create database PRACTICE;

use PRACTICE;

create table 회원테이블(
회원번호 int primary key,
이름 varchar(20),
가입일자 date not null,
수신동의 bit
);

select * from 회원테이블;

-- 열 추가
alter table 회원테이블 add 성별 varchar(2);

select * from 회원테이블;

-- 열 데이터 타입 변경
alter table 회원테이블 modify 성별 varchar(20);
alter table 회원테이블 change 성별 성 varchar(2);

select * from 회원테이블;

-- 테이블명 변경
alter table 회원테이블 rename 회원정보;

select * from 회원정보;

-- 테이블 삭제
drop table 회원정보;

select * from 회원테이블;
