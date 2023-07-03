-- 3월에 태어난 여성 회원 목록 출력하기

-- 태어난 월 확인
select MEMBER_NAME, MONTH(DATE_OF_BIRTH) as 태어난월
     from MEMBER_PROFILE;

-- 1차 시도 : 아래 주의 사항 추가 필요
-- DATE_OF_BIRTH의 데이트 포맷이 예시('yyyy-mm-dd')와 동일해야 정답처리 됩니다.
select MEMBER_ID
        , MEMBER_NAME
        -- , GENDER, DATE_OF_BIRTH
        -- cast(DATE_OF_BIRTH as DATE) as DATE_OF_BIRTH
        -- date_format(DATE_OF_BIRTH, '%y-%m-%d')       >> yy-mm-dd 형태
        date_format(DATE_OF_BIRTH, '%Y-%m-%d')          -- yyyy-mm-dd 형태
    from MEMBER_PROFILE
    where MONTH(DATE_OF_BIRTH) = 3
        and GENDER = 'W'
        -- 특정 데이터가 null 인 row 제거하는 방법 1
        and TLNO is not null
    order by MEMBER_ID asc;
