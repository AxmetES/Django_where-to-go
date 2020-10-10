first_creation = ['4a59e3e9f0b18fd2590b513316e99c93.jpg',
                  '8cc32eb5f72ba6ac4ed34c85bd953ec0.jpg',
                  '116218d98e6bc3ba4e8075b2552c3929.jpg',
                  'c481ed4f66bd6481c6c63738f2f5ae2d.jpg',
                  'fc55f45d7c9bddc7f3272149cc3a27c5.jpg',
                  'c2490d80275d743caeeda4b09d7d5e7a.jpg', ]

from_db = ['4a59e3e9f0b18fd2590b513316e99c93_5U9IyeP.jpg',
           '8cc32eb5f72ba6ac4ed34c85bd953ec0_EBvtJT4.jpg',
           '116218d98e6bc3ba4e8075b2552c3929_D30k68Y.jpg',
           'c481ed4f66bd6481c6c63738f2f5ae2d_9y2Fsch.jpg',
           'fc55f45d7c9bddc7f3272149cc3a27c5_TRDWVJF.jpg',
           'c2490d80275d743caeeda4b09d7d5e7a_QNrpgtp.jpg',
           ]


def replace_bd_id(images):
    names = []
    for image in images:
        name_id, extend = image.split('.')
        name, bd_id = name_id.split('_')
        file_name = name + '.' + extend
        names.append(file_name)
    return names


list_names = replace_bd_id(from_db)
for i in list_names:
    print(i)