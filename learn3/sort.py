
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

# 1、数组排序
def arr_sort(arr):
    new_arr = sorted(arr)
    print("排序后：" )
    print(new_arr)

# 2、根据空格分割数组
def arr_split(arr):
    new_arr = dbname_list_2.split(" ")
    print("分割后：")
    print(new_arr)
    arr_sort(new_arr)


if __name__ == '__main__':
    print('dbname_list_1')
    arr_sort(dbname_list_1)
    print('\n')

    print('dbname_list_2')
    arr_split(dbname_list_2)
    print('\n')