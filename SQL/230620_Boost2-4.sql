/* 트랜젝션 제어어 (DCL)*/
/* DML 명령어의 실행, 취소, 임시저장할 때 */

/* 트랜젝션(Transaction) 분할할 수 없는 최소 단위, 
                       논리적인 작업 단위*/
/* 약간 세포 혹은 원자! 같은 느낌? */

/* 트랜젝션 시작 (BEGIN) >> 데이터 삽입 (INSERT) >> 실행/취소 */
/* 실행 (COMMIT) : 모든 작업을 최종 실행 */ 
/* 취소 (ROLLBACK) : 모든 작업을 되돌리기 */ 

use Practice;

drop table 회원테이블;

create 회원테이블 (
    회원번호 int primary key,
    이름 varchar(20),
    가입일자 date not null,
    수신동의 bit
);

/* 회원테이블 조회 */
select * from 회원테이블;

/* begin + rollback (취소) */
begin;

insert into 회원테이블 values (1001, '나', '2023-06-20', 1);

select * from 회원테이블;

rollback;

/* begin + commit (취소) */
begin;

insert into 회원테이블 values (1001, '나', '2023-06-20', 1);

commit;

select * from 회원테이블;
