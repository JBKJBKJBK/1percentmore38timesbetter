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
             cast(형식1, 형식2) >> cast('2023-06-27')
*/