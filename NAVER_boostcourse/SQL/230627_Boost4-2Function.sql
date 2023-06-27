/*
    단일 행 함수 : 숫자, 문자, 날짜, 형변환, 일반
    복수 행 함수 : 집계형, 그룹형 (group by 와 같이)
    윈도우 함수 : 순위, 집계, 누적
*/

/*
    단일 행 함수
    _ 모든 행에 각각
    _ 숫자형 : abs(), 반올림 round(숫자, N), sqrt()
    _ 문자형 : lower()/upper(), left(문자, N)/right(문자, N), length()
    _ 날짜형 : year/month/day(), date_add(날짜, interval), datediff(날짜1, 날짜2)
    _ 형변환 : date_format('2023-06-27', '%m-%d-%y')
             cast(형식1, 형식2) >> cast('2023-06-27 12:00:00' as DATE)
    _ 일반 : ifnull(A, B) >> A가 Null이면 B, 아니면 A >> ifnull(NUll, 0)
            case when (조건1) then (반환1)
                 when (조건2) then (반환2)
                 else (나머지) end
*/

/*
    복수 행 함수 : 여러 행이 하나의 값 / group by와 많이 사용
    _집계함수 _ count(열) * distinct 중복제거
            _ sum(열)
            _ avg(열)
            _ max/min(열)
    _그룹함수 _ with rollup : group by 열들을 오른쪽에서 왼쪽순으로 그룹
                          >> group by (열1, 열2) with rollup
*/

select year(JOIN_DATE) as 가입연도
        , ADDR
        , count(MEM_NO) as 회원수
    from CUSTOMER
    group by year(JOIN_DATE), ADDR
    with rollup;

/*  ROLL UP
     가입연도\ADDR | 경기 | 강원 | 대구 | ... | 소계
    -------------------------------------------
        2020     | 가입 | 가입 | 가입 | ... | 소계
        2021     | 가입 | 가입 | 가입 | ... | 소계
        2022     | 가입 | 가입 | 가입 | ... | 소계
        2023     | 가입 | 가입 | 가입 | ... | 소계
    -------------------------------------------
        소 계     | 가입 | 가입 | 가입 | ... | 합계
*/