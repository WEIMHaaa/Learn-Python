
dbname_list_1=(
"ats",
"amp",
"aut",
"bcs",
"bsf",
"bss",
"cfg",
"css",
"ctr",
"cts",
"dst",
"ell",
"irs",
"jos",
"mds",
"mfs",
"mqa",
"nps",
"ntf",
"pts",
"rcf",
"res",
"tcs",
"uts",
"gow",
"tcb",
)

dbname_list_2=('test2_demo test2_gdp test2_wcs test2_yht test2_cfg test2_tcb test2_amp test2_aut test2_bcs test2_bsf '
               'test2_bss test2_css test2_ctr test2_cts test2_dst test2_ell test2_irs test2_jos test2_mfs test2_mqa '
               'test2_nps test2_ntf test2_pts test2_phs test2_rcf test2_res test2_tcs test2_uts tcb wcs test2_gow '
               'test2_lms test2_ocr test2_mds')

dbname_list_3=('dev1_demo dev1_gdp dev1_wcs dev1_yht dev1_cfg dev1_tcb dev1_amp dev1_aut dev1_bcs dev1_bsf dev1_bss dev1_css dev1_ctr dev1_cts dev1_dst dev1_ell dev1_irs dev1_jos dev1_mfs dev1_mqa dev1_nps dev1_ntf dev1_pts dev1_phs dev1_rcf dev1_res dev1_tcs dev1_uts wcs dev1_gow dev1_lms dev1_ocr dev1_mds')

app_list_1=('ats sso ams aws app-front aus b2b-front irs mfs cts mos mbs wcs aut bsf bss mqx ntf scheduler amp pts ell jos res phs gow')

app_list=('disconf cts aut ams bss scheduler ccs eam rms cts bsf sso app-front b2b-front ntf')
dbname_list_4=('test1_demo test1_gdp test1_wcs test1_yht test1_cfg test1_tcb test1_amp test1_aut test1_bcs test1_bsf test1_bss test1_css test1_ctr test1_cts test1_dst test1_ell test1_irs test1_jos test1_mfs test1_mqa test1_nps test1_ntf test1_pts test1_phs test1_rcf test1_res test1_tcs test1_uts test1_gow test1_lms test1_ocr test1_mds')

dbname_list_5=('test2_demo test2_gdp test2_wcs test2_yht test2_cfg test2_tcb test2_amp test2_aut test2_bcs test2_bsf test2_bss test2_css test2_ctr test2_cts test2_dst test2_ell test2_irs test2_jos test2_mfs test2_mqa test2_nps test2_ntf test2_pts test2_phs test2_rcf test2_res test2_tcs test2_uts test2_gow test2_lms test2_ocr test2_mds')


app_list=('ats sso ams app-front aus b2b-front irs mfs cts mos mbs wcs aut bsf bss mqx ntf scheduler amp pts ell jos res phs gow')

# 1、数组排序
def arr_sort(arr):
    new_arr = sorted(arr)
    print("排序后：" )
    print(new_arr)

# 2、根据空格分割数组
def arr_split(arr):
    new_arr = arr.split(" ")
    print("分割后：")
    print(new_arr)
    arr_sort(new_arr)


if __name__ == '__main__':
    print('app_list:')
    arr_split(app_list)
    print('\n')
