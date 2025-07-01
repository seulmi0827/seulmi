-- 코드를 입력하세요
select my_ap.apnt_no,pt.pt_name,pt.pt_no,my_ap.mcdp_cd,my_ap.dr_name, my_ap.apnt_ymd
from (SELECT Ap.pt_no, Ap.apnt_no, Ap.mcdp_cd, Ap.apnt_ymd, Dr.dr_name
from appointment as Ap
left join doctor as Dr
on Ap.mddr_id = Dr.dr_id
where Ap.mcdp_cd like 'cs' and
      Ap.apnt_ymd like '2022-04-13%' and
      Ap.apnt_cncl_yn like 'N') as my_ap
left join patient as pt
on pt.pt_no = my_ap.pt_no
order by my_ap.apnt_ymd