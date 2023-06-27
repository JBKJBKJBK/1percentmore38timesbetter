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

/*  ROLL UP : 가입, 소계, 합계 나옴
     가입연도\ADDR | 경기 | 강원 | 대구 | ... | 소계
    -------------------------------------------
        2020     | 가입 | 가입 | 가입 | ... | 소계
        2021     | 가입 | 가입 | 가입 | ... | 소계
        2022     | 가입 | 가입 | 가입 | ... | 소계
        2023     | 가입 | 가입 | 가입 | ... | 소계
    -------------------------------------------
        소 계     | 가입 | 가입 | 가입 | ... | 합계
*/

select MEM_NO
        , sum(SALES_QTY) as 구매수량
    from SALES
    group by MEM_NO;

/*
    윈도우 함수 : 행과 행간의 관계 >> 순위나 누적 집계
    _ 순위 함수 _ row_number : 고유한 순위 반환
              _ rank       : 동일한 값이면 동일한 순위 반환 >> 1, 2, 2, 4, ...
              _ dense_rank : 동일한 값이면 동일한 순위 반환, 하나의 등수로 >> 1, 2, 2, 3, ...
    _ 집계 함수 _ count
      (누적    _ sum
              _ avg
              _ max/min

    over(order by 열/ partition by 열)
*/

select ORDER_DATE
        , row_number() over (order by ORDER_DATE asc) as 고유한_순위_변환
        , rank()       over (order by ORDER_DATE asc) as 동일한_순위_변환
        , dense_rank() over (order by ORDER_DATE asc) as 동일한_순위_변환, 숫자 바로 이어서
    from SALES;

select ORDER_DATE
        , row_number() over (partition by ORDER_DATE asc) as 고유한_순위_변환
        , rank()       over (partition by ORDER_DATE asc) as 동일한_순위_변환
        , dense_rank() over (partition by ORDER_DATE asc) as 동일한_순위_변환, 숫자 바로 이어서
    from SALES;

-- ?? order / partition 차이 ??
-- >> ORDER_DATE 여러 개 / ORDER_DATE 하나로 합침

select ORDER_DATE
        , SALES_QTY
        , '-' as 구분
        -- 날짜가 증가함에 따라 count 누적 
        , count(ORDER_NO) over (order by ORDER_DATE asc) as 누적_구매횟수
        , sum(SALES_QTY)  over (order by ORDER_DATE asc) as 누적_구매수량
        , avg(SALES_QTY)  over (order by ORDER_DATE asc) as 누적_평균구매수량
        , max(SALES_QTY)  over (order by ORDER_DATE asc) as 
        , min(SALES_QTY)  over (order by ORDER_DATE asc) as 
    from SALES;