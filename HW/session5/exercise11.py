def is_inside(diem,hcn):
    if hcn[0] <= diem[0] <= hcn[0] + hcn[2] and hcn[1] <= diem[1] <= hcn[1] + hcn[3]:
        return True
    else:
        return False
is_inside([200, 120], [140, 60, 100, 200])
