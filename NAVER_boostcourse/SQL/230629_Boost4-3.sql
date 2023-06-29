use PRACTICE;

/* view */

select A.*
        , A.SALES_QTY * B.PRICE as 결제금액
    from SALES as A
    left join PRODUCT as B 
    on A.PRODUCT_CODE = B.PRODUCT_CODE;

/* view 생성 */
create view SALES_PRODUCT as

-- (위 내용 동일)

/* view 실행 */
select * from SALES_PRODUCT;

/* view 수정 */
alter view SALES_PRODUCT as
select A.*
        , A.SALES_QTY * B.PRICE * 1.1 as 결제금액_수수료포함
    from SALES as A 
    left join product as B 
    on A.PRODUCT_CODE = B.PRODUCT_CODE;

/* 확인 */
select * from SALES_PRODUCT;

/* view 삭제 */
drop view SALES_PRODUCT;

/* 중복되는 열 저장 안됨 */



/* procedure 매개변수 활용하여 사용자가 정의한 작업을 저장 */

delimiter//  -- 여러 명령어들을 하나로 묶어줄 때 사용
create procedure /* 이름 (in 매개변수 varchar(20))*/
begin 
    select *
    from CUSTOMER
    where GENDER = '매개변수';
end
delimiter;

/* procedure 실행 */

call CST_GEN_ADDR_IN('MAN', 'SEOUL');
call CST_GEN_ADDR_IN('WOMAN', 'BUSAN');

/* procedure 삭제 */

drop procedure CST_GEN_ADDR_IN;

/* out 매개변수 : procedure 결괏값 반환 */

create procedure CST_GEN_ADDR_IN_CNT_MEM_OUT (in INPUT_A VARCHAR(20), OUT CNT_MEM int)
begin 
    select count(MEM_NO)
    into CNT_MEM
    from CUSTOMER
    where GENDER = INPUT_A
    and ADDR = INPUT_B;
end //

/* procedure 실행 */

call CST_GEN_ADDR_IN_CNT_MEM_OUT('MAN', 'SEOUL', @CNT_MEM);
select @CNT_MEM;


/* IN/OUT 매개변수 */

delimiter //
create procedure IN_OUT_PARAMETER( inout count INT)
begin 
    set count = count +10;
end //
delimiter;
