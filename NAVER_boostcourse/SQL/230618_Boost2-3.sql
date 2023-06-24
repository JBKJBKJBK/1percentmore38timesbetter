/* 데이터 제어어 (DCL, control) */
/* 관리자가 특정 사용자에게 데이터 접근 권한 부여 & 제거할 때 사용 */

USE MYSQL;

/* 사용자 확인 */
SELECT * FROM USER;

/* 사용자 비밀번호 변경 */
create user 'TEST' @LOCALHOST = '1234';

/* 권한
create
alter
drop
insert
delete
update
select
*/

/* 특정 권한 부여 */
grant select, delete on PRACTICE.회원테이블 to 'TEST'@LOCALHOST;

/* 특정 권한 제거 */
revoke delete on PRACTICE.회원테이블 from 'TEST'@LOCALHOST;

/* 모든 권한 부여 */
grant all on PRACTICE.회원테이블 to 'TEST'@LOCALHOST;

/* 모든 권한 제거 */
revoke all on PRACTICE.회원테이블 FROM 'TEST'@LOCALHOST;