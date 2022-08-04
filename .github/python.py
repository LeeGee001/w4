friend = ['Korkai','khorkai','Somchai','Somsri']

friend2 = {'korkai':'ก.ไก่',
          'khorkai':'ข.ไข่',
          'Somchai':'สมชาย',
          'Somsri':'สมศรี'}
visitor = 'Somsri'

if visitor in friend or visitor.title() in friend:
    print('ยินดีต้องรับ')
    if visitor in friend2 or visitor.title() in friend2:
        print('สวัสดี' + friend2[visitor.title()])
    else:
        print('สวัสดีคุณลูกค้า')
else:
    print('ผมไม่รู้จักคุณ')
