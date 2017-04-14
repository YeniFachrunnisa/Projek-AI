def moveTower(tinggi,kutubawal, kutubtujuan, kutubpersinggahan):
    if tinggi >= 1:
        moveTower(tinggi-1,kutubawal,kutubpersinggahan,kutubtujuan)
        moveDisk(kutubawal,kutubtujuan)
        moveTower(tinggi-1,kutubpersinggahan,kutubtujuan,kutubawal)

def moveDisk(fp,tp):
    print("Berpindah dari",fp,"Menuju",tp)


