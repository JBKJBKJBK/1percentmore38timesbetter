/* 흉부외과 또는 일반외과 의사 목록 출력하기 */

select DR_NAME, DR_ID, MCDP_CD, ynd(HIRE_YMD)  
                                -- 날짜 코드 YMD만 나와야하는데 뒤에 시간없애야 함
    from DOCTOR
    where MCDP_CD in ('CS', 'GS')
    order by HIRE_YMD desc, DR_NAME;

/* 12세 이하인 여자 환자 목록 출력하기 */    
-- select PT_NAME, PT_NO, GEND_CD, AGE, TLNO
select *
-- 전화번호가 NULL이면 'NONE'으로 출력
/* 1) 
    case 
        when tlno is null then 'none'
        else tlno
    end as tlno
*/
/* 2)
    IF(TLNO IS NULL, 'NONE', TLNO) AS TLNO 
*/
    from PATIENT
    where GEND_CD = 'W' and 
          AGE <= 12
    order by AGE desc, PT_NAME asc;